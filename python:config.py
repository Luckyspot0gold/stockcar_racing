import os
from dotenv import load_dotenv

load_dotenv()

# Game settings
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

# Racing settings
NUM_LAPS = 3
CARS = [
    {"name": "BTC", "color": (255, 215, 0)},  # Gold
    {"name": "ETH", "color": (140, 86, 255)}, # Purple
    {"name": "SOL", "color": (0, 216, 214)},  # Cyan
    {"name": "AVAX", "color": (232, 65, 66)}  # Red
]

# Market settings
EXCHANGE = os.getenv("EXCHANGE", "binance")
REFRESH_INTERVAL = 15  # seconds
