# data_ingest.py  
from stone_feed import MarketFeed  

feeds = {  
    'BTC': MarketFeed(source='coinbase', indicators=['candle', 'rsi', 'vwap']),  
    'ETH': MarketFeed(source='binance', indicators=['macd', 'bollinger'])  
}  

while racing:  
    for coin, feed in feeds.items():  
        broadcastToCars(coin, feed.get_update())  
