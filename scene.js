// In race-scene.js
class RaceScene extends Phaser.Scene {
  constructor() {
    super({ key: 'RaceScene' });
    this.cars = []; // array of car objects
    this.speeds = {}; // speeds for each car (by symbol)
  }

  preload() {
    // Load car images and track
    this.load.image('track', 'assets/track.png');
    this.load.image('btc-car', 'assets/btc-car.png');
    // ... other cars
  }

  create() {
    // Create track
    this.add.image(400, 300, 'track');

    // Create cars at starting line
    this.cars.push(this.add.image(100, 200, 'btc-car'));
    // ... other cars

    // Start data updates (from server via WebSocket or interval to fetch)
    this.setupDataUpdates();
  }

  setupDataUpdates() {
    // Every 5 seconds, get new data and update speeds
    setInterval(() => {
      // Fetch data from our backend (which gets from CoinGecko)
      fetch('/api/prices')
        .then(res => res.json())
        .then(data => {
          // data = { btc: { change: 0.5 }, eth: { change: -0.2 }, ... }
          this.speeds = data;
        });
    }, 5000);
  }

  update() {
    // Move cars: use the speed from this.speeds
    this.cars.forEach(car => {
      const symbol = car.texture.key.split('-')[0]; // e.g., 'btc'
      const change = this.speeds[symbol] ? this.speeds[symbol].change : 0;
      // Move right by change * some factor
      car.x += change * 10;
    });
  }
}
