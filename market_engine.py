import ccxt
import time
import threading
import numpy as np
from datetime import datetime, timedelta
from config import CRYPTO_CONFIG, GAME_CONFIG
import json
import os

class CryptoMarketEngine:
    def __init__(self):
        # Initialize exchange connections
        self.exchanges = {
            'binance': ccxt.binance({'enableRateLimit': True}),
            'coinbase': ccxt.coinbasepro({'enableRateLimit': True})
        }
        
        # Market data storage
        self.market_data = {}
        self.price_history = {}
        self.cached_data = {}
        self.last_update = 0
        self.monitoring = False
        
        # Initialize cache
        self.load_cached_data()
        
        print("📊 Market Engine Initialized - Wyoming Protocol 7")
    
    def load_cached_data(self):
        """Load cached market data for fallback"""
        cache_file = 'market_cache.json'
        if os.path.exists(cache_file):
            try:
                with open(cache_file, 'r') as f:
                    self.cached_data = json.load(f)
                print("💾 Cached market data loaded")
            except:
                self.generate_fallback_data()
        else:
            self.generate_fallback_data()
    
    def save_cached_data(self):
        """Save current market data to cache"""
        try:
            with open('market_cache.json', 'w') as f:
                json.dump(self.market_data, f)
        except Exception as e:
            print(f"⚠️ Cache save failed: {e}")
    
    def generate_fallback_data(self):
        """Generate realistic fallback data"""
        base_prices = {
            'BTC/USDT': 65000,
            'SOL/USDT': 150,
            'AVAX/USDT': 40,
            'DOGE/USDT': 0.15
        }
        
        for symbol in CRYPTO_CONFIG['SYMBOLS']:
            self.cached_data[symbol] = {
                'price': base_prices.get(symbol, 100),
                'momentum': np.random.uniform(-2, 2),
                'volatility': np.random.uniform(0.5, 3.0),
                'volume_delta': np.random.uniform(-20, 20),
                'sentiment': np.random.uniform(-1, 1),
                'timestamp': time.time()
            }
    
    def fetch_btc_momentum(self):
        """Fetch BTC 5-minute momentum"""
        try:
            exchange = self.exchanges['binance']
            ohlcv = exchange.fetch_ohlcv('BTC/USDT', '5m', limit=10)
            
            if len(ohlcv) >= 2:
                current_price = ohlcv[-1][4]  # Close price
                previous_price = ohlcv[-2][4]
                momentum = ((current_price - previous_price) / previous_price) * 100
                
                return {
                    'price': current_price,
                    'momentum': momentum,
                    'timestamp': time.time()
                }
        except Exception as e:
            print(f"⚠️ BTC momentum fetch failed: {e}")
            return self.cached_data.get('BTC/USDT', {})
    
    def fetch_sol_volatility(self):
        """Fetch SOL volatility metrics"""
        try:
            exchange = self.exchanges['binance']
            ohlcv = exchange.fetch_ohlcv('SOL/USDT', '1m', limit=20)
            
            if len(ohlcv) >= 20:
                prices = [candle[4] for candle in ohlcv]
                volatility = np.std(prices) / np.mean(prices) * 100
                current_price = prices[-1]
                
                return {
                    'price': current_price,
                    'volatility': volatility,
                    'timestamp': time.time()
                }
        except Exception as e:
            print(f"⚠️ SOL volatility fetch failed: {e}")
            return self.cached_data.get('SOL/USDT', {})
    
    def fetch_avax_volume_delta(self):
        """Fetch AVAX volume delta"""
        try:
            exchange = self.exchanges['binance']
            ohlcv = exchange.fetch_ohlcv('AVAX/USDT', '5m', limit=5)
            
            if len(ohlcv) >= 2:
                current_volume = ohlcv[-1][5]  # Volume
                previous_volume = ohlcv[-2][5]
                volume_delta = ((current_volume - previous_volume) / previous_volume) * 100
                current_price = ohlcv[-1][4]
                
                return {
                    'price': current_price,
                    'volume_delta': volume_delta,
                    'timestamp': time.time()
                }
        except Exception as e:
            print(f"⚠️ AVAX volume delta fetch failed: {e}")
            return self.cached_data.get('AVAX/USDT', {})
    
    def fetch_doge_sentiment(self):
        """Fetch DOGE social sentiment (simulated)"""
        try:
            exchange = self.exchanges['binance']
            ticker = exchange.fetch_ticker('DOGE/USDT')
            
            # Simulate sentiment based on price change
            price_change = ticker.get('percentage', 0)
            sentiment = np.tanh(price_change / 10)  # Normalize to -1 to 1
            
            return {
                'price': ticker['last'],
                'sentiment': sentiment,
                'price_change': price_change,
                'timestamp': time.time()
            }
        except Exception as e:
            print(f"⚠️ DOGE sentiment fetch failed: {e}")
            return self.cached_data.get('DOGE/USDT', {})
    
    def update_market_data(self):
        """Update all market data - Wyoming Protocol 7"""
        print("📈 Updating market data...")
        
        # Fetch data for each car
        self.market_data['BTC/USDT'] = self.fetch_btc_momentum()
        self.market_data['SOL/USDT'] = self.fetch_sol_volatility()
        self.market_data['AVAX/USDT'] = self.fetch_avax_volume_delta()
        self.market_data['DOGE/USDT'] = self.fetch_doge_sentiment()
        
        # Update price history
        for symbol, data in self.market_data.items():
            if symbol not in self.price_history:
                self.price_history[symbol] = []
            
            self.price_history[symbol].append({
                'price': data.get('price', 0),
                'timestamp': data.get('timestamp', time.time())
            })
            
            # Keep only last 100 data points
            if len(self.price_history[symbol]) > 100:
                self.price_history[symbol] = self.price_history[symbol][-100:]
        
        # Save to cache
        self.save_cached_data()
        self.last_update = time.time()
        
        print("✅ Market data updated successfully")
    
    def start_monitoring(self):
        """Start continuous market monitoring"""
        self.monitoring = True
        print("🔄 Market monitoring started")
        
        while self.monitoring:
            try:
                self.update_market_data()
                time.sleep(GAME_CONFIG['MARKET_UPDATE_INTERVAL'])
            except Exception as e:
                print(f"⚠️ Market monitoring error: {e}")
                time.sleep(5)  # Short delay before retry
    
    def stop_monitoring(self):
        """Stop market monitoring"""
        self.monitoring = False
        print("⏹️ Market monitoring stopped")
    
    def get_latest_data(self):
        """Get latest market data with fallback"""
        if not self.market_data:
            print("📦 Using cached market data")
            return self.cached_data
        
        # Check if data is stale (older than 60 seconds)
        if time.time() - self.last_update > 60:
            print("⚠️ Market data stale, using cache")
            return self.cached_data
        
        return self.market_data
    
    def get_car_metrics(self, symbol):
        """Get specific metrics for a car"""
        data = self.get_latest_data().get(symbol, {})
        
        if symbol == 'BTC/USDT':
            return {
                'primary_metric': data.get('momentum', 0),
                'metric_name': '5min Momentum',
                'price': data.get('price', 0)
            }
        elif symbol == 'SOL/USDT':
            return {
                'primary_metric': data.get('volatility', 0),
                'metric_name': 'Volatility',
                'price': data.get('price', 0)
            }
        elif symbol == 'AVAX/USDT':
            return {
                'primary_metric': data.get('volume_delta', 0),
                'metric_name': 'Volume Delta',
                'price': data.get('price', 0)
            }
        elif symbol == 'DOGE/USDT':
            return {
                'primary_metric': data.get('sentiment', 0),
                'metric_name': 'Social Sentiment',
                'price': data.get('price', 0)
            }
        
        return {'primary_metric': 0, 'metric_name': 'Unknown', 'price': 0}