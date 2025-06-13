// server.js
const express = require('express');
const app = express();
const port = 3000;

app.use(express.static('public'));
app.use(express.json());

// In-memory storage for bets
let bets = [];

// Endpoint to get cryptocurrency data (we'll cache CoinGecko data)
app.get('/api/prices', (req, res) => {
  // For now, mock data
  res.json({
    btc: { change: Math.random() * 2 - 1 }, // between -1 and 1
    eth: { change: Math.random() * 2 - 1 },
    sol: { change: Math.random() * 2 - 1 }
  });
});

// Endpoint to place a bet
app.post('/api/bet', (req, res) => {
  const { user, car, amount } = req.body;
  bets.push({ user, car, amount });
  res.json({ success: true });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
