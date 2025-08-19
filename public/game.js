class CryptoRacingGame {
    constructor() {
        this.socket = io();
        this.gameState = {
            isRacing: false,
            cars: [],
            marketData: {},
            raceStartTime: null
        };
        this.chart = null;
        this.raceTimer = null;
        
        this.initializeEventListeners();
        this.initializeChart();
        this.setupSocketListeners();
    }

    initializeEventListeners() {
        document.getElementById('startRace').addEventListener('click', () => {
            this.startRace();
        });

        document.getElementById('resetRace').addEventListener('click', () => {
            this.resetRace();
        });
    }

    setupSocketListeners() {
        this.socket.on('gameState', (data) => {
            this.gameState = { ...this.gameState, ...data };
            this.updateDisplay();
        });

        this.socket.on('raceStarted', (data) => {
            this.gameState.isRacing = true;
            this.gameState.cars = data.cars;
            this.gameState.raceStartTime = Date.now();
            this.updateRaceStatus('🏁 Race in Progress!');
            this.startRaceTimer();
            this.createCarElements();
            document.getElementById('startRace').disabled = true;
        });

        this.socket.on('gameUpdate', (data) => {
            this.gameState.cars = data.cars;
            this.gameState.marketData = data.marketData;
            this.updateCarPositions();
            this.updateMarketData();
            this.updateLeaderboard();
            this.updateChart();
        });

        this.socket.on('raceFinished', (data) => {
            this.gameState.isRacing = false;
            this.updateRaceStatus(`🏆 Winner: ${data.winner.name} (${data.winner.symbol})!`);
            this.stopRaceTimer();
            this.highlightWinner(data.winner);
            document.getElementById('startRace').disabled = false;
            
            // Show celebration effect
            this.showCelebration(data.winner);
        });

        this.socket.on('raceReset', (data) => {
            this.gameState.isRacing = false;
            this.gameState.cars = data.cars;
            this.updateRaceStatus('Ready to Race');
            this.resetDisplay();
            document.getElementById('startRace').disabled = false;
        });
    }

    startRace() {
        this.socket.emit('startRace');
    }

    resetRace() {
        this.socket.emit('resetRace');
    }

    createCarElements() {
        const raceTrack = document.getElementById('raceTrack');
        
        // Remove existing cars
        const existingCars = raceTrack.querySelectorAll('.car');
        existingCars.forEach(car => car.remove());

        // Create new car elements
        this.gameState.cars.forEach((car, index) => {
            const carElement = document.createElement('div');
            carElement.className = `car ${car.symbol.toLowerCase()}`;
            carElement.id = `car-${car.id}`;
            carElement.style.top = `${80 + index * 60}px`;
            carElement.style.left = '60px';
            
            carElement.innerHTML = `
                ${car.symbol}
                <div class="car-info">
                    <div>${car.name}</div>
                    <div class="car-stats">
                        Speed: <span class="car-speed">0</span> | 
                        Laps: <span class="car-laps">0</span>
                    </div>
                </div>
            `;
            
            raceTrack.appendChild(carElement);
        });
    }

    updateCarPositions() {
        this.gameState.cars.forEach(car => {
            const carElement = document.getElementById(`car-${car.id}`);
            if (carElement) {
                const trackWidth = document.getElementById('raceTrack').offsetWidth - 160; // Account for margins
                const positionPercent = (car.position % 1000) / 1000; // Normalize to track length
                const leftPosition = 60 + (positionPercent * trackWidth);
                
                carElement.style.left = `${leftPosition}px`;
                
                // Update car info
                const speedElement = carElement.querySelector('.car-speed');
                const lapsElement = carElement.querySelector('.car-laps');
                if (speedElement) speedElement.textContent = car.speed.toFixed(1);
                if (lapsElement) lapsElement.textContent = car.laps;
                
                // Add racing animation class
                if (this.gameState.isRacing) {
                    carElement.classList.add('racing');
                } else {
                    carElement.classList.remove('racing');
                }
            }
        });
    }

    updateMarketData() {
        const cryptoGrid = document.getElementById('cryptoGrid');
        cryptoGrid.innerHTML = '';

        this.gameState.cars.forEach(car => {
            const marketData = this.gameState.marketData[car.id];
            if (marketData) {
                const cardElement = document.createElement('div');
                cardElement.className = 'crypto-card';
                
                const price = marketData.usd;
                const change = marketData.usd_24h_change || 0;
                const changeClass = change >= 0 ? 'change-up' : 'change-down';
                const changeSymbol = change >= 0 ? '▲' : '▼';
                
                cardElement.innerHTML = `
                    <div class="crypto-symbol">${car.symbol}</div>
                    <div class="crypto-price">$${price.toLocaleString('en-US', {
                        minimumFractionDigits: 2,
                        maximumFractionDigits: car.symbol === 'BTC' ? 0 : 4
                    })}</div>
                    <div class="crypto-change ${changeClass}">
                        ${changeSymbol} ${Math.abs(change).toFixed(2)}%
                    </div>
                `;
                
                cryptoGrid.appendChild(cardElement);
            }
        });
    }

    updateLeaderboard() {
        const leaderboard = document.getElementById('leaderboard');
        
        // Sort cars by laps and position
        const sortedCars = [...this.gameState.cars].sort((a, b) => {
            if (a.laps !== b.laps) return b.laps - a.laps;
            return b.position - a.position;
        });

        leaderboard.innerHTML = '';
        
        sortedCars.forEach((car, index) => {
            const itemElement = document.createElement('div');
            itemElement.className = 'leaderboard-item';
            
            const position = index + 1;
            const positionEmoji = position === 1 ? '🥇' : position === 2 ? '🥈' : position === 3 ? '🥉' : `${position}.`;
            
            itemElement.innerHTML = `
                <div class="leaderboard-position">${positionEmoji}</div>
                <div class="leaderboard-car">
                    <strong>${car.symbol}</strong>
                    <div style="font-size: 0.8rem; color: rgba(255,255,255,0.6);">${car.name}</div>
                </div>
                <div class="leaderboard-laps">
                    <div>Laps: ${car.laps}</div>
                    <div style="font-size: 0.8rem;">Speed: ${car.speed.toFixed(1)}</div>
                </div>
            `;
            
            leaderboard.appendChild(itemElement);
        });
    }

    initializeChart() {
        const ctx = document.getElementById('performanceChart').getContext('2d');
        this.chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: [],
                datasets: []
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        labels: {
                            color: 'rgba(255, 255, 255, 0.8)',
                            font: {
                                family: 'Orbitron'
                            }
                        }
                    }
                },
                scales: {
                    y: {
                        grid: {
                            color: 'rgba(255, 255, 255, 0.1)'
                        },
                        ticks: {
                            color: 'rgba(255, 255, 255, 0.7)'
                        },
                        title: {
                            display: true,
                            text: 'Position',
                            color: 'rgba(255, 255, 255, 0.8)'
                        }
                    },
                    x: {
                        grid: {
                            color: 'rgba(255, 255, 255, 0.1)'
                        },
                        ticks: {
                            color: 'rgba(255, 255, 255, 0.7)'
                        },
                        title: {
                            display: true,
                            text: 'Time',
                            color: 'rgba(255, 255, 255, 0.8)'
                        }
                    }
                }
            }
        });
    }

    updateChart() {
        if (!this.chart || !this.gameState.isRacing) return;

        const currentTime = new Date().toLocaleTimeString();
        
        // Initialize datasets if empty
        if (this.chart.data.datasets.length === 0) {
            this.gameState.cars.forEach(car => {
                this.chart.data.datasets.push({
                    label: car.symbol,
                    data: [],
                    borderColor: car.color,
                    backgroundColor: car.color + '20',
                    borderWidth: 2,
                    tension: 0.4
                });
            });
        }

        // Add new data point
        this.chart.data.labels.push(currentTime);
        
        this.gameState.cars.forEach((car, index) => {
            this.chart.data.datasets[index].data.push(car.position + (car.laps * 1000));
        });

        // Keep only last 20 data points
        if (this.chart.data.labels.length > 20) {
            this.chart.data.labels.shift();
            this.chart.data.datasets.forEach(dataset => {
                dataset.data.shift();
            });
        }

        this.chart.update('none');
    }

    startRaceTimer() {
        this.raceTimer = setInterval(() => {
            if (this.gameState.raceStartTime) {
                const elapsed = Date.now() - this.gameState.raceStartTime;
                const minutes = Math.floor(elapsed / 60000);
                const seconds = Math.floor((elapsed % 60000) / 1000);
                document.getElementById('raceTimer').textContent = 
                    `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
            }
        }, 1000);
    }

    stopRaceTimer() {
        if (this.raceTimer) {
            clearInterval(this.raceTimer);
            this.raceTimer = null;
        }
    }

    updateRaceStatus(status) {
        document.getElementById('raceStatus').textContent = status;
    }

    highlightWinner(winner) {
        const winnerElement = document.getElementById(`car-${winner.id}`);
        if (winnerElement) {
            winnerElement.classList.add('winner');
        }
    }

    showCelebration(winner) {
        // Create celebration overlay
        const celebration = document.createElement('div');
        celebration.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.8);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 1000;
            animation: fadeIn 0.5s ease;
        `;
        
        celebration.innerHTML = `
            <div style="text-align: center; color: white; font-family: Orbitron;">
                <h1 style="font-size: 3rem; margin-bottom: 20px; color: #FFD700;">🏆 RACE WINNER! 🏆</h1>
                <h2 style="font-size: 2rem; margin-bottom: 10px;">${winner.name}</h2>
                <h3 style="font-size: 1.5rem; color: #00d2ff;">${winner.symbol}</h3>
                <p style="margin-top: 20px; font-size: 1.2rem;">Completed ${winner.laps} laps!</p>
                <button onclick="this.parentElement.parentElement.remove()" 
                        style="margin-top: 30px; padding: 15px 30px; background: linear-gradient(to right, #6a11cb, #2575fc); 
                               border: none; color: white; border-radius: 50px; font-size: 1.1rem; cursor: pointer;">
                    Continue Racing
                </button>
            </div>
        `;
        
        document.body.appendChild(celebration);
        
        // Auto-remove after 5 seconds
        setTimeout(() => {
            if (celebration.parentElement) {
                celebration.remove();
            }
        }, 5000);
    }

    resetDisplay() {
        // Clear chart
        if (this.chart) {
            this.chart.data.labels = [];
            this.chart.data.datasets.forEach(dataset => {
                dataset.data = [];
            });
            this.chart.update();
        }
        
        // Reset timer
        this.stopRaceTimer();
        document.getElementById('raceTimer').textContent = '00:00';
        
        // Remove winner effects
        document.querySelectorAll('.car').forEach(car => {
            car.classList.remove('winner', 'racing');
        });
        
        // Update displays
        this.updateDisplay();
    }

    updateDisplay() {
        this.updateMarketData();
        this.updateLeaderboard();
        if (this.gameState.cars.length > 0) {
            this.createCarElements();
            this.updateCarPositions();
        }
    }
}

// Add CSS animation for fade in
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
`;
document.head.appendChild(style);
pip install --upgrade pygame
// Initialize the game when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new CryptoRacingGame();
});
