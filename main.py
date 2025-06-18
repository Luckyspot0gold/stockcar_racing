import pygame
import sys
import asyncio
import threading
import time
from datetime import datetime, timedelta
from market_engine import CryptoMarketEngine
from racing_engine import WyomingRacingEngine
from ui_manager import UIManager
from config import GAME_CONFIG, WYOMING_COLORS

class QuantumRacingGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((GAME_CONFIG['SCREEN_WIDTH'], GAME_CONFIG['SCREEN_HEIGHT']))
        pygame.display.set_caption("Wyoming Protocol 7 - Crypto Racing")
        self.clock = pygame.time.Clock()
        
        # Initialize game components
        self.market_engine = CryptoMarketEngine()
        self.racing_engine = WyomingRacingEngine()
        self.ui_manager = UIManager(self.screen)
        
        # Game state
        self.running = True
        self.race_active = False
        self.last_market_update = 0
        
        # Start market data thread
        self.market_thread = threading.Thread(target=self.market_engine.start_monitoring, daemon=True)
        self.market_thread.start()
        
        print("🏎️ Wyoming Protocol 7 Racing Engine Initialized")
        print("🔥 StoneVerse Quantum Core: ACTIVE")
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.toggle_race()
                elif event.key == pygame.K_r:
                    self.reset_race()
                elif event.key == pygame.K_ESCAPE:
                    self.running = False
    
    def toggle_race(self):
        if not self.race_active:
            self.start_race()
        else:
            self.stop_race()
    
    def start_race(self):
        self.race_active = True
        self.racing_engine.start_race()
        print("🚀 RACE STARTED - Wyoming Protocol 7 Active")
    
    def stop_race(self):
        self.race_active = False
        self.racing_engine.stop_race()
        print("🏁 RACE STOPPED")
    
    def reset_race(self):
        self.race_active = False
        self.racing_engine.reset_race()
        print("🔄 RACE RESET")
    
    def update(self):
        current_time = time.time()
        
        # Update market data every 15 seconds (Wyoming Protocol 7)
        if current_time - self.last_market_update >= GAME_CONFIG['MARKET_UPDATE_INTERVAL']:
            market_data = self.market_engine.get_latest_data()
            self.racing_engine.update_car_performance(market_data)
            self.last_market_update = current_time
        
        # Update racing engine
        if self.race_active:
            self.racing_engine.update()
        
        # Check for race completion
        winner = self.racing_engine.check_winner()
        if winner:
            self.race_active = False
            print(f"🏆 WINNER: {winner['name']} ({winner['symbol']})")
    
    def render(self):
        # Fill background with StoneVerse colors
        self.screen.fill(WYOMING_COLORS['DARK_BLUE'])
        
        # Render racing track and cars
        self.racing_engine.render(self.screen)
        
        # Render UI elements
        market_data = self.market_engine.get_latest_data()
        self.ui_manager.render_market_data(market_data)
        self.ui_manager.render_race_info(self.racing_engine.get_race_info())
        self.ui_manager.render_controls()
        
        # Update display
        pygame.display.flip()
    
    def run(self):
        print("🎮 Starting Wyoming Racing Protocol...")
        
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(GAME_CONFIG['FPS'])
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = QuantumRacingGame()
    game.run()