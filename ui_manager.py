import pygame
import time
from config import WYOMING_COLORS, GAME_CONFIG

class UIManager:
    def __init__(self, screen):
        self.screen = screen
        self.font_large = pygame.font.Font(None, 36)
        self.font_medium = pygame.font.Font(None, 24)
        self.font_small = pygame.font.Font(None, 18)
        
        # UI positions
        self.market_panel_rect = pygame.Rect(10, 10, 300, 200)
        self.race_info_rect = pygame.Rect(GAME_CONFIG['SCREEN_WIDTH'] - 310, 10, 300, 200)
        self.controls_rect = pygame.Rect(10, GAME_CONFIG['SCREEN_HEIGHT'] - 100, 
                                       GAME_CONFIG['SCREEN_WIDTH'] - 20, 80)
    
    def render_market_data(self, market_data):
        """Render real-time market data panel"""
        # Panel background
        pygame.draw.rect(self.screen, WYOMING_COLORS['PANEL_BG'], self.market_panel_rect)
        pygame.draw.rect(self.screen, WYOMING_COLORS['GOLD'], self.market_panel_rect, 2)
        
        # Title
        title = self.font_medium.render("📊 Live Market Data", True, WYOMING_COLORS['GOLD'])
        self.screen.blit(title, (self.market_panel_rect.x + 10, self.market_panel_rect.y + 10))
        
        # Market data for each car
        y_offset = 40
        for i, (symbol, data) in enumerate(market_data.items()):
            if symbol.endswith('/USDT'):
                crypto_symbol = symbol.split('/')[0]
                
                # Symbol and price
                symbol_text = self.font_small.render(f"{crypto_symbol}:", True, WYOMING_COLORS['WHITE'])
                self.screen.blit(symbol_text, (self.market_panel_rect.x + 10, 
                                             self.market_panel_rect.y + y_offset))
                
                price = data.get('price', 0)
                price_text = self.font_small.render(f"${price:.4f}", True, WYOMING_COLORS['GREEN'])
                self.screen.blit(price_text, (self.market_panel_rect.x + 80, 
                                            self.market_panel_rect.y + y_offset))
                
                # Specific metric
                if crypto_symbol == 'BTC':
                    metric = data.get('momentum', 0)
                    metric_text = f"Mom: {metric:.2f}%"
                elif crypto_symbol == 'SOL':
                    metric = data.get('volatility', 0)
                    metric_text = f"Vol: {metric:.2f}%"
                elif crypto_symbol == 'AVAX':
                    metric = data.get('volume_delta', 0)
                    metric_text = f"VΔ: {metric:.1f}%"
                elif crypto_symbol == 'DOGE':
                    metric = data.get('sentiment', 0)
                    metric_text = f"Sent: {metric:.2f}"
                else:
                    metric_text = "N/A"
                
                # Color based on metric value
                if isinstance(metric, (int, float)):
                    color = WYOMING_COLORS['GREEN'] if metric > 0 else WYOMING_COLORS['RED']
                else:
                    color = WYOMING_COLORS['WHITE']
                
                metric_surface = self.font_small.render(metric_text, True, color)
                self.screen.blit(metric_surface, (self.market_panel_rect.x + 160, 
                                                self.market_panel_rect.y + y_offset))
                
                y_offset += 25
        
        # Last update time
        update_time = time.strftime("%H:%M:%S")
        time_text = self.font_small.render(f"Updated: {update_time}", True, WYOMING_COLORS['GRAY'])
        self.screen.blit(time_text, (self.market_panel_rect.x + 10, 
                                   self.market_panel_rect.y + self.market_panel_rect.height - 25))
    
    def render_race_info(self, race_info):
        """Render race information panel"""
        # Panel background
        pygame.draw.rect(self.screen, WYOMING_COLORS['PANEL_BG'], self.race_info_rect)
        pygame.draw.rect(self.screen, WYOMING_COLORS['GOLD'], self.race_info_rect, 2)
        
        # Title
        title = self.font_medium.render("🏁 Race Status", True, WYOMING_COLORS['GOLD'])
        self.screen.blit(title, (self.race_info_rect.x + 10, self.race_info_rect.y + 10))
        
        # Race status
        status_text = self.font_small.render(f"Status: {race_info['status']}", True, WYOMING_COLORS['WHITE'])
        self.screen.blit(status_text, (self.race_info_rect.x + 10, self.race_info_rect.y + 40))
        
        # Race time
        race_time = race_info['time']
        time_str = f"{int(race_time // 60):02d}:{int(race_time % 60):02d}"
        time_text = self.font_small.render(f"Time: {time_str}", True, WYOMING_COLORS['WHITE'])
        self.screen.blit(time_text, (self.race_info_rect.x + 10, self.race_info_rect.y + 60))
        
        # Leader info
        if race_info['leader']:
            leader = race_info['leader']
            leader_text = self.font_small.render(f"Leader: {leader.symbol}", True, WYOMING_COLORS['YELLOW'])
            self.screen.blit(leader_text, (self.race_info_rect.x + 10, self.race_info_rect.y + 80))
            
            laps_text = self.font_small.render(f"Laps: {leader.laps_completed}/{GAME_CONFIG['LAPS_TO_WIN']}", 
                                             True, WYOMING_COLORS['WHITE'])
            self.screen.blit(laps_text, (self.race_info_rect.x + 10, self.race_info_rect.y + 100))
        
        # Leaderboard
        leaderboard_title = self.font_small.render("Leaderboard:", True, WYOMING_COLORS['GOLD'])
        self.screen.blit(leaderboard_title, (self.race_info_rect.x + 10, self.race_info_rect.y + 125))
        
        # Sort cars by position
        sorted_cars = sorted(race_info['cars'], 
                           key=lambda c: (c.laps_completed, c.position_on_track), 
                           reverse=True)
        
        for i, car in enumerate(sorted_cars[:4]):  # Show top 4
            position_text = f"{i+1}. {car.symbol} (L{car.laps_completed})"
            color = WYOMING_COLORS['GOLD'] if i == 0 else WYOMING_COLORS['WHITE']
            pos_surface = self.font_small.render(position_text, True, color)
            self.screen.blit(pos_surface, (self.race_info_rect.x + 20, 
                                         self.race_info_rect.y + 145 + (i * 15)))
        
        # Winner announcement
        if race_info.get('winner'):
            winner = race_info['winner']
            winner_text = self.font_medium.render(f"🏆 WINNER: {winner['symbol']}!", 
                                                True, WYOMING_COLORS['GOLD'])
            # Center the winner text
            text_rect = winner_text.get_rect(center=(GAME_CONFIG['SCREEN_WIDTH']//2, 50))
            
            # Background for winner text
            bg_rect = text_rect.inflate(20, 10)
            pygame.draw.rect(self.screen, WYOMING_COLORS['DARK_BLUE'], bg_rect)
            pygame.draw.rect(self.screen, WYOMING_COLORS['GOLD'], bg_rect, 2)
            
            self.screen.blit(winner_text, text_rect)
    
    def render_controls(self):
        """Render control instructions"""
        # Panel background
        pygame.draw.rect(self.screen, WYOMING_COLORS['PANEL_BG'], self.controls_rect)
        pygame.draw.rect(self.screen, WYOMING_COLORS['GOLD'], self.controls_rect, 2)
        
        # Title
        title = self.font_medium.render("🎮 Wyoming Protocol 7 Controls", True, WYOMING_COLORS['GOLD'])
        self.screen.blit(title, (self.controls_rect.x + 10, self.controls_rect.y + 10))
        
        # Control instructions
        controls = [
            "SPACE: Start/Stop Race",
            "R: Reset Race", 
            "ESC: Exit",
            "Market updates every 15 seconds"
        ]
        
        x_offset = 10
        for i, control in enumerate(controls):
            control_text = self.font_small.render(control, True, WYOMING_COLORS['WHITE'])
            x_pos = self.controls_rect.x + x_offset + (i * 200)
            self.screen.blit(control_text, (x_pos, self.controls_rect.y + 40))
        
        # Wyoming Protocol 7 indicator
        protocol_text = self.font_small.render("Wyoming Protocol 7: ACTIVE", True, WYOMING_COLORS['GREEN'])
        self.screen.blit(protocol_text, (self.controls_rect.x + 10, self.controls_rect.y + 60))
        ///
        import pygame
import math
from config import SCREEN_WIDTH, SCREEN_HEIGHT, CARS, NUM_LAPS

class Car:
    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0
        self.max_speed = 8
        self.acceleration = 0.1
        self.deceleration = 0.05
        self.handling = 4.0
        self.lap = 0
        self.nitro_active = False
        self.nitro_duration = 0
        self.color = CARS[index]["color"]
        self.name = CARS[index]["name"]
        self.rect = pygame.Rect(x, y, 40, 20)
        
    def update(self, performance):
        # Update car properties based on market performance
        self.max_speed = 8 + performance['speed']
        self.handling = 4.0 * performance['handling']
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.speed = min(self.speed + self.acceleration, self.max_speed)
        elif keys[pygame.K_DOWN]:
            self.speed = max(self.speed - self.deceleration, 0)
        else:
            self.speed = max(self.speed - self.deceleration/2, 0)
            
        if keys[pygame.K_LEFT]:
            self.angle += self.handling * (self.speed / self.max_speed)
        if keys[pygame.K_RIGHT]:
            self.angle -= self.handling * (self.speed / self.max_speed)
            
        # Nitro activation
        if keys[pygame.K_SPACE] and performance['nitro_chance'] and not self.nitro_active:
            self.nitro_active = True
            self.nitro_duration = 180  # 3 seconds at 60 FPS
            
        if self.nitro_active:
            self.speed = min(self.speed + 0.5, self.max_speed * 1.5)
            self.nitro_duration -= 1
            if self.nitro_duration <= 0:
                self.nitro_active = False
        
        # Update position
        rad = math.radians(self.angle)
        self.x += math.sin(rad) * self.speed
        self.y += math.cos(rad) * self.speed
        
        # Update rect for collision
        self.rect.x = self.x
        self.rect.y = self.y
        
    def draw(self, screen):
        # Draw car
        car_surface = pygame.Surface((40, 20), pygame.SRCALPHA)
        pygame.draw.rect(car_surface, self.color, (0, 0, 40, 20))
        pygame.draw.rect(car_surface, (30, 30, 30), (35, 5, 5, 10))
        rotated = pygame.transform.rotate(car_surface, self.angle)
        screen.blit(rotated, (self.x - rotated.get_width() // 2, self.y - rotated.get_height() // 2))
        
        # Draw nitro effect if active
        if self.nitro_active:
            nitro_surface = pygame.Surface((20, 10), pygame.SRCALPHA)
            pygame.draw.ellipse(nitro_surface, (0, 191, 255), (0, 0, 20, 10))
            nitro_rad = math.radians(self.angle + 180)
            nitro_x = self.x - math.sin(nitro_rad) * 25
            nitro_y = self.y - math.cos(nitro_rad) * 25
            nitro_rotated = pygame.transform.rotate(nitro_surface, self.angle)
            screen.blit(nitro_rotated, (nitro_x - nitro_rotated.get_width() // 2, nitro_y - nitro_rotated.get_height() // 2))

class RacingEngine:
    def __init__(self):
        self.cars = []
        self.track = self.generate_track()
        
    def generate_track(self):
        # Simple oval track
        track = pygame.Rect(100, 100, SCREEN_WIDTH - 200, SCREEN_HEIGHT - 200)
        return track
        
    def add_car(self, index):
        start_x = SCREEN_WIDTH // 2
        start_y = SCREEN_HEIGHT - 100 - index * 50
        self.cars.append(Car(index, start_x, start_y))
        
    def update(self, market_performances):
        for i, car in enumerate(self.cars):
            car.update(market_performances[i])
            
    def draw(self, screen):
        # Draw track
        pygame.draw.rect(screen, (50, 50, 50), self.track, 2)
        
        # Draw cars
        for car in self.cars:
            car.draw(screen)
