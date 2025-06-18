# Wyoming Protocol 7 - Cryptocurrency Racing Game

A real-time cryptocurrency racing game where car speeds are determined by live market data from major exchanges.

## 🏎️ Features

### Wyoming Protocol 7 Requirements ✅
- **Market Data Refresh**: Every 15 seconds using CCXT
- **Visual Jitter Effects**: Cars jitter during high volatility periods
- **StoneVerse Color Scheme**: Gold and purple Wyoming-themed design
- **Fallback System**: Cached data when API fails

### Car Performance Metrics
1. **BTC Car**: Speed based on 5-minute momentum
2. **SOL Car**: Speed based on volatility (with visual jitter)
3. **AVAX Car**: Speed based on volume delta
4. **DOGE Car**: Speed based on social sentiment simulation

## 🚀 Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Run the game
python main.py
```

## 🎮 Controls

- **SPACE**: Start/Stop Race
- **R**: Reset Race
- **ESC**: Exit Game

## 📊 Market Integration

The game uses CCXT to fetch real-time data from:
- Binance (primary)
- Coinbase Pro (backup)

### Data Sources:
- **BTC/USDT**: 5-minute OHLCV for momentum calculation
- **SOL/USDT**: 1-minute data for volatility analysis
- **AVAX/USDT**: 5-minute volume data for delta calculation
- **DOGE/USDT**: Ticker data for sentiment simulation

## 🎨 StoneVerse Design

- **Primary Colors**: Wyoming Gold (#FFD700) and Purple (#800080)
- **Background**: Deep blue gradient
- **UI Elements**: Semi-transparent panels with gold borders
- **Cars**: Crypto-specific color schemes with gold outlines

## 🔧 Configuration

Edit `config.py` to customize:
- Screen resolution
- Track length
- Update intervals
- Color schemes
- Car specifications

## 🛡️ Fallback System

When API calls fail, the game uses:
1. Cached market data (saved locally)
2. Realistic mock data generation
3. Graceful degradation with notifications

## 📈 Performance Metrics

Each car's speed is calculated using:

```python
# BTC: Momentum-based
speed = base_speed + (momentum * 2)

# SOL: Volatility-based (with jitter)
speed = base_speed + (abs(volatility) * 1.5)
jitter_intensity = volatility * 2

# AVAX: Volume delta-based
speed = base_speed + (volume_delta * 1.2)

# DOGE: Sentiment-based
speed = base_speed + (sentiment * 3)
```

## 🏁 Race Rules

- **Laps to Win**: 3 laps
- **Track Length**: 1000 virtual units
- **Speed Limits**: 1.0 to 15.0 units per frame
- **Update Frequency**: 60 FPS with 15-second market updates

## 🔍 Debug Mode

Set `DEBUG_MODE=true` in `.env` to enable:
- Console logging of market data
- Performance metrics display
- API call monitoring

## 🎯 Wyoming Protocol 7 Compliance

This implementation fully complies with Wyoming Protocol 7 requirements:
- ✅ 15-second market refresh cycle
- ✅ High volatility visual effects
- ✅ StoneVerse gold/purple color scheme
- ✅ Robust fallback mechanisms
- ✅ Real-time CCXT integration

## 🚨 Troubleshooting

### Common Issues:
1. **API Rate Limits**: Increase `MARKET_UPDATE_INTERVAL` in config
2. **Missing Dependencies**: Run `pip install -r requirements.txt`
3. **Display Issues**: Check screen resolution in `config.py`
4. **Market Data Errors**: Game will automatically use cached data

### Performance Optimization:
- Reduce FPS in config for slower systems
- Enable caching to reduce API calls
- Use fallback data during development

---

**StoneVerse Gaming** - Wyoming Protocol 7 Certified 🏆