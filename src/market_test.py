import ccxt
import pygame
import numpy as np
from datetime import datetime

class CryptoRacingEngine:
    def __init__(self):
        self.exchange = ccxt.binance()
        self.assets = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT']
        self.velocity_cache = {}
        
    def get_market_velocity(self, symbol):
        """Get real-time market momentum (5m timeframe)"""
        try:
            ohlcv = self.exchange.fetch_ohlcv(symbol, '5m', limit=10)
            closes = [x[4] for x in ohlcv]
            return (closes[-1] - closes[0]) / closes[0] * 100
        except:
            return 0.0  # Fail-safe during market outages

    def map_to_car_performance(self, velocity):
        """Convert market velocity to car attributes"""
        return {
            'max_speed': 150 + abs(velocity * 10),
            'acceleration': 0.5 + (velocity / 100),
            'handling': 0.8 - (abs(velocity) / 500)
        }

# TESTING PROTOCOL
if __name__ == "__main__":
    print("🔥 Testing Market-to-Movement Integration")
    engine = CryptoRacingEngine()
    for asset in engine.assets:
        v = engine.get_market_velocity(asset)
        print(f"{asset} velocity: {v:.2f}% → {engine.map_to_car_performance(v)}")
