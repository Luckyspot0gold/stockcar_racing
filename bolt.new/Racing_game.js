// Bolt prompt: "Create PyGame-style stockcar racing with:
// - Crypto-themed cars (BTC, ETH, SOL, AVAX)
// - Supabase leaderboard integration
// - Wyoming Protocol 7 color scheme
// - Real-time position tracking"

// Generated Bolt code:
class CryptoRacer {
  constructor() {
    this.cars = [
      { id: 'btc', name: 'Bitcoin', color: '#F7931A', position: 0 },
      { id: 'eth', name: 'Ethereum', color: '#627EEA', position: 0 },
      { id: 'sol', name: 'Solana', color: '#00FFA3', position: 0 },
      { id: 'avax', name: 'Avalanche', color: '#E84142', position: 0 }
    ];
    this.raceDistance = 100;
  }

  async startRace() {
    // Wyoming Protocol 7 race algorithm
    while (!this.isRaceFinished()) {
      await this.updatePositions();
      await this.saveToSupabase();
      await new Promise(r => setTimeout(r, 1000));
    }
    this.declareWinner();
  }

  async updatePositions() {
    this.cars.forEach(car => {
      // Market-based movement algorithm
      const marketFactor = this.getMarketFactor(car.id);
      car.position += Math.random() * 3 * marketFactor;
    });
  }

  getMarketFactor(cryptoId) {
    // Placeholder for real market data
    const factors = { btc: 1.2, eth: 1.1, sol: 1.3, avax: 1.25 };
    return factors[cryptoId];
  }

  async saveToSupabase() {
    const { error } = await supabase
      .from('races')
      .insert(this.cars.map(car => ({
        car_id: car.id,
        position: car.position,
        timestamp: new Date()
      })));
    
    if (error) console.error('Supabase error:', error);
  }

  isRaceFinished() {
    return this.cars.some(car => car.position >= this.raceDistance);
  }

  declareWinner() {
    const winner = this.cars.reduce((a, b) => 
      a.position > b.position ? a : b
    );
    console.log(`🏁 ${winner.name} WINS!`);
    return winner;
  }
}
