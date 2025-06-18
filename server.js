const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const cors = require('cors');
const axios = require('axios');
require('dotenv').config();

const app = express();
const server = http.createServer(app);
const io = socketIo(server, {
  cors: {
    origin: "*",
    methods: ["GET", "POST"]
  }
});

app.use(cors());
app.use(express.json());
app.use(express.static('public'));

// Game state
const gameState = {
  isRacing: false,
  cars: [],
  raceStartTime: null,
  trackLength: 1000,
  updateInterval: 5000, // 5 seconds
  marketData: {}
};

// Cryptocurrency configuration
const cryptocurrencies = [
  { id: 'bitcoin', symbol: 'BTC', name: 'Bitcoin', color: '#F7931A' },
  { id: 'ethereum', symbol: 'ETH', name: 'Ethereum', color: '#627EEA' },
  { id: 'solana', symbol: 'SOL', name: 'Solana', color: '#00FFA3' },
  { id: 'avalanche-2', symbol: 'AVAX', name: 'Avalanche', color: '#E84142' },
  { id: 'litecoin', symbol: 'LTC', name: 'Litecoin', color: '#BEBEBE' },
  { id: 'ripple', symbol: 'XRP', name: 'XRP', color: '#23292F' },
  { id: 'dogecoin', symbol: 'DOGE', name: 'Dogecoin', color: '#C2A633' },
  { id: 'chainlink', symbol: 'LINK', name: 'Chainlink', color: '#2A5ADA' }
];

// Initialize cars
function initializeCars() {
  gameState.cars = cryptocurrencies.map((crypto, index) => ({
    id: crypto.id,
    symbol: crypto.symbol,
    name: crypto.name,
    color: crypto.color,
    position: 0,
    speed: 0,
    lane: index,
    lastPrice: 0,
    priceChange: 0,
    laps: 0
  }));
}

// Fetch real-time crypto prices
async function fetchCryptoPrices() {
  try {
    const coinIds = cryptocurrencies.map(c => c.id).join(',');
    const response = await axios.get(`https://api.coingecko.com/api/v3/simple/price`, {
      params: {
        ids: coinIds,
        vs_currencies: 'usd',
        include_24hr_change: true,
        include_last_updated_at: true
      }
    });

    return response.data;
  } catch (error) {
    console.error('Error fetching crypto prices:', error.message);
    // Return mock data if API fails
    return generateMockPrices();
  }
}

// Generate mock prices for fallback
function generateMockPrices() {
  const mockData = {};
  cryptocurrencies.forEach(crypto => {
    const basePrice = {
      'bitcoin': 65000,
      'ethereum': 3500,
      'solana': 150,
      'avalanche-2': 40,
      'litecoin': 85,
      'ripple': 0.6,
      'dogecoin': 0.15,
      'chainlink': 18
    }[crypto.id] || 100;

    const change = (Math.random() - 0.5) * 10; // -5% to +5%
    mockData[crypto.id] = {
      usd: basePrice * (1 + change / 100),
      usd_24h_change: change
    };
  });
  return mockData;
}

// Update car positions based on market data
function updateCarPositions(marketData) {
  gameState.cars.forEach(car => {
    const coinData = marketData[car.id];
    if (coinData) {
      const currentPrice = coinData.usd;
      const priceChange = coinData.usd_24h_change || 0;
      
      // Calculate speed based on price change
      // 1% change = 10 pixels per update
      const speedMultiplier = 10;
      const baseSpeed = 5; // Minimum speed
      car.speed = baseSpeed + (priceChange * speedMultiplier);
      
      // Ensure minimum speed (cars always move forward)
      car.speed = Math.max(car.speed, 1);
      
      // Update position
      car.position += car.speed;
      
      // Check for lap completion
      if (car.position >= gameState.trackLength) {
        car.laps += 1;
        car.position = car.position % gameState.trackLength;
      }
      
      // Update car data
      car.lastPrice = currentPrice;
      car.priceChange = priceChange;
    }
  });
}

// Check for race winner
function checkRaceWinner() {
  const winner = gameState.cars.find(car => car.laps >= 3); // 3 laps to win
  if (winner) {
    gameState.isRacing = false;
    io.emit('raceFinished', { winner, finalStandings: [...gameState.cars].sort((a, b) => b.laps - a.laps || b.position - a.position) });
    return true;
  }
  return false;
}

// Main game loop
async function gameLoop() {
  if (!gameState.isRacing) return;
  
  try {
    // Fetch latest market data
    const marketData = await fetchCryptoPrices();
    gameState.marketData = marketData;
    
    // Update car positions
    updateCarPositions(marketData);
    
    // Check for winner
    if (!checkRaceWinner()) {
      // Emit updated game state
      io.emit('gameUpdate', {
        cars: gameState.cars,
        marketData: gameState.marketData,
        raceTime: Date.now() - gameState.raceStartTime
      });
    }
  } catch (error) {
    console.error('Game loop error:', error);
  }
}

// Socket.IO connection handling
io.on('connection', (socket) => {
  console.log('Client connected:', socket.id);
  
  // Send current game state to new client
  socket.emit('gameState', {
    isRacing: gameState.isRacing,
    cars: gameState.cars,
    marketData: gameState.marketData
  });
  
  // Handle start race
  socket.on('startRace', () => {
    if (!gameState.isRacing) {
      initializeCars();
      gameState.isRacing = true;
      gameState.raceStartTime = Date.now();
      
      io.emit('raceStarted', { cars: gameState.cars });
      console.log('Race started!');
    }
  });
  
  // Handle reset race
  socket.on('resetRace', () => {
    gameState.isRacing = false;
    initializeCars();
    io.emit('raceReset', { cars: gameState.cars });
    console.log('Race reset!');
  });
  
  socket.on('disconnect', () => {
    console.log('Client disconnected:', socket.id);
  });
});

// API Routes
app.get('/api/prices', async (req, res) => {
  try {
    const prices = await fetchCryptoPrices();
    res.json(prices);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch prices' });
  }
});

app.get('/api/game-state', (req, res) => {
  res.json(gameState);
});

// Start game loop
setInterval(gameLoop, gameState.updateInterval);

// Initialize cars on startup
initializeCars();

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`🏎️  Crypto Racing Server running on port ${PORT}`);
  console.log(`🚀 Game ready! Visit http://localhost:${PORT}`);
});