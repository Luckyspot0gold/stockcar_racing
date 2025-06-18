import ccxt
import time
import threading
from config import EXCHANGE, REFRESH_INTERVAL

class MarketEngine:
    def __init__(self):
        self.exchange = getattr(ccxt, EXCHANGE)()
        self.market_data = {
            "BTC/USDT": {"momentum": 0, "volatility": 0, "volume_delta": 0},
            "ETH/USDT": {"momentum": 0, "volatility": 0, "volume_delta": 0},
            "SOL/USDT": {"momentum": 0, "volatility": 0, "volume_delta": 0},
            "AVAX/USDT": {"momentum": 0, "volatility": 0, "volume_delta": 0}
        }
        self.running = True
        self.thread = threading.Thread(target=self.update_market_data)
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()

    def update_market_data(self):
        while self.running:
            try:
                for symbol in self.market_data.keys():
                    ohlcv = self.exchange.fetch_ohlcv(symbol, '5m', limit=10)
                    closes = [x[4] for x in ohlcv]
                    # Momentum: (current - open) / open
                    momentum = (closes[-1] - closes[0]) / closes[0] * 100
                    
                    # Volatility: (high - low) / low for last candle
                    last_candle = ohlcv[-1]
                    volatility = (last_candle[2] - last_candle[3]) / last_candle[3] * 100
                    
                    # Volume delta: current volume vs 5-candle average
                    volumes = [x[5] for x in ohlcv]
                    avg_volume = sum(volumes[:-1]) / len(volumes[:-1])
                    volume_delta = (volumes[-1] - avg_volume) / avg_volume * 100
                    
                    self.market_data[symbol] = {
                        "momentum": momentum,
                        "volatility": volatility,
                        "volume_delta": volume_delta
                    }
            except Exception as e:
                print(f"Market data error: {e}")
            time.sleep(REFRESH_INTERVAL)

    def get_car_performance(self, car_index):
        symbols = list(self.market_data.keys())
        symbol = symbols[car_index]
        data = self.market_data[symbol]
        
        # Map market data to car performance
        # Base speed: 5 + momentum%
        # Handling: 1.0 - volatility% (higher volatility reduces handling)
        # Nitro chance: volume_delta > 10% gives nitro
        return {
            "speed": 5 + data['momentum'] / 10,
            "handling": max(0.5, 1.0 - data['volatility'] / 100),
            "nitro_chance": data['volume_delta'] > 10
        }
