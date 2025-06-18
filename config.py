# Wyoming Protocol 7 Configuration

GAME_CONFIG = {
    'SCREEN_WIDTH': 1200,
    'SCREEN_HEIGHT': 800,
    'FPS': 60,
    'TRACK_LENGTH': 1000,  # Virtual track length
    'LAPS_TO_WIN': 3,
    'MARKET_UPDATE_INTERVAL': 15,  # 15 seconds - Wyoming Protocol 7 requirement
}

# StoneVerse Color Scheme - Gold and Purple
WYOMING_COLORS = {
    'GOLD': (255, 215, 0),
    'PURPLE': (128, 0, 128),
    'DARK_BLUE': (25, 25, 112),
    'LIGHT_PURPLE': (186, 85, 211),
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'GREEN': (0, 255, 0),
    'RED': (255, 0, 0),
    'YELLOW': (255, 255, 0),
    'ORANGE': (255, 165, 0),
    'GRAY': (128, 128, 128),
    'DARK_GRAY': (64, 64, 64),
    'PANEL_BG': (30, 30, 60, 200),  # Semi-transparent
}

# Car Configuration
CAR_CONFIG = {
    'WIDTH': 60,
    'HEIGHT': 30,
    'START_X': 100,
    'START_Y': 120,
    'LANE_HEIGHT': 80,
    'BASE_SPEED': 5.0,
    'MIN_SPEED': 1.0,
    'MAX_SPEED': 15.0,
}

# Cryptocurrency Configuration
CRYPTO_CONFIG = {
    'SYMBOLS': ['BTC/USDT', 'SOL/USDT', 'AVAX/USDT', 'DOGE/USDT'],
    'UPDATE_INTERVAL': 15,  # seconds
    'CACHE_DURATION': 300,  # 5 minutes
}

# Market Data Fallback
FALLBACK_DATA = {
    'BTC/USDT': {
        'price': 65000,
        'momentum': 1.2,
        'volatility': 2.5,
        'volume_delta': 5.0,
        'sentiment': 0.3
    },
    'SOL/USDT': {
        'price': 150,
        'momentum': -0.8,
        'volatility': 4.2,
        'volume_delta': -2.1,
        'sentiment': 0.1
    },
    'AVAX/USDT': {
        'price': 40,
        'momentum': 0.5,
        'volatility': 3.1,
        'volume_delta': 8.3,
        'sentiment': 0.6
    },
    'DOGE/USDT': {
        'price': 0.15,
        'momentum': 2.1,
        'volatility': 5.8,
        'volume_delta': 12.4,
        'sentiment': 0.8
    }
}