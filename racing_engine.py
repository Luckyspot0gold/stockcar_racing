import pygame
import math
import time
import numpy as np
from config import GAME_CONFIG, WYOMING_COLORS, CAR_CONFIG

class RaceCar:
    def __init__(self, symbol, name, color, lane):
        self.symbol = symbol
        self.name = name
        self.color = color
        self.lane = lane
        
        # Position and movement
        self.x = CAR_CONFIG['START_X']
        self.y = CAR_CONFIG['START_Y'] + (lane * CAR_CONFIG['LANE_HEIGHT'])
        self.speed = 0
        self.base_speed = CAR_CONFIG['BASE_SPEED']
        self.position_on_track = 0  # 0 to 1 (full lap)
        self.laps_completed = 0
        
        # Visual effects
        self.jitter_intensity = 0
        self.jitter_offset_x = 0
        self.jitter_offset_y = 0
        self.last_jitter_update = 0
        
        # Performance metrics
        self.market_metric = 0
        self.metric_name = ""
        self.price = 0
        
        # Car sprite
        self.width = CAR_CONFIG['WIDTH']
        self.height = CAR_CONFIG['HEIGHT']
        
    def update_market_data(self, market_engine):
        """Update car performance based on market data"""
        metrics = market_engine.get_car_metrics(f"{self.symbol}/USDT")
        self.market_metric = metrics['primary_metric']
        self.metric_name = metrics['metric_name']
        self.price = metrics['price']
        
        # Calculate speed based on metric
        if self.symbol == 'BTC':
            # Momentum-based speed (momentum can be negative)
            self.speed = self.base_speed + (self.market_metric * 2)
        elif self.symbol == 'SOL':
            # Volatility-based speed (higher volatility = higher speed)
            self.speed = self.base_speed + (abs(self.market_metric) * 1.5)
            self.jitter_intensity = min(self.market_metric * 2, 10)  # Jitter during high volatility
        elif self.symbol == 'AVAX':
            # Volume delta-based speed
            self.speed = self.base_speed + (self.market_metric * 1.2)
        elif self.symbol == 'DOGE':
            # Sentiment-based speed (-1 to 1 sentiment)
            self.speed = self.base_speed + (self.market_metric * 3)
        
        # Ensure minimum speed
        self.speed = max(self.speed, CAR_CONFIG['MIN_SPEED'])
        self.speed = min(self.speed, CAR_CONFIG['MAX_SPEED'])
    
    def update_jitter(self):
        """Update jitter effects for high volatility - Wyoming Protocol 7"""
        current_time = time.time()
        
        if current_time - self.last_jitter_update > 0.1:  # Update jitter 10 times per second
            if self.jitter_intensity > 0:
                self.jitter_offset_x = np.random.uniform(-self.jitter_intensity, self.jitter_intensity)
                self.jitter_offset_y = np.random.uniform(-self.jitter_intensity/2, self.jitter_intensity/2)
                self.jitter_intensity *= 0.95  # Decay jitter over time
            else:
                self.jitter_offset_x = 0
                self.jitter_offset_y = 0
            
            self.last_jitter_update = current_time
    
    def update_position(self, dt):
        """Update car position on track"""
        # Move forward based on speed
        distance_moved = self.speed * dt / 60.0  # Normalize for 60 FPS
        self.position_on_track += distance_moved / GAME_CONFIG['TRACK_LENGTH']
        
        # Check for lap completion
        if self.position_on_track >= 1.0:
            self.laps_completed += 1
            self.position_on_track -= 1.0
        
        # Update visual position
        track_width = GAME_CONFIG['SCREEN_WIDTH'] - 200
        self.x = 100 + (self.position_on_track * track_width)
        
        # Apply jitter
        self.update_jitter()
    
    def render(self, screen):
        """Render the car with Wyoming Protocol 7 styling"""
        # Calculate render position with jitter
        render_x = self.x + self.jitter_offset_x
        render_y = self.y + self.jitter_offset_y
        
        # Car body (rounded rectangle)
        car_rect = pygame.Rect(render_x, render_y, self.width, self.height)
        pygame.draw.rect(screen, self.color, car_rect, border_radius=8)
        
        # Car outline (StoneVerse gold)
        pygame.draw.rect(screen, WYOMING_COLORS['GOLD'], car_rect, width=2, border_radius=8)
        
        # Car symbol
        font = pygame.font.Font(None, 24)
        text = font.render(self.symbol, True, WYOMING_COLORS['WHITE'])
        text_rect = text.get_rect(center=(render_x + self.width//2, render_y + self.height//2))
        screen.blit(text, text_rect)
        
        # Speed indicator (small bar above car)
        speed_bar_width = 40
        speed_bar_height = 4
        speed_ratio = min(self.speed / CAR_CONFIG['MAX_SPEED'], 1.0)
        speed_bar_fill = speed_ratio * speed_bar_width
        
        # Background bar
        pygame.draw.rect(screen, WYOMING_COLORS['DARK_GRAY'], 
                        (render_x + (self.width - speed_bar_width)//2, render_y - 10, 
                         speed_bar_width, speed_bar_height))
        
        # Fill bar (color based on speed)
        if speed_ratio > 0.7:
            speed_color = WYOMING_COLORS['GREEN']
        elif speed_ratio > 0.4:
            speed_color = WYOMING_COLORS['YELLOW']
        else:
            speed_color = WYOMING_COLORS['RED']
        
        pygame.draw.rect(screen, speed_color,
                        (render_x + (self.width - speed_bar_width)//2, render_y - 10,
                         speed_bar_fill, speed_bar_height))

class WyomingRacingEngine:
    def __init__(self):
        self.cars = []
        self.race_active = False
        self.race_start_time = 0
        self.winner = None
        
        # Initialize cars
        car_configs = [
            ('BTC', 'Bitcoin', WYOMING_COLORS['ORANGE'], 0),
            ('SOL', 'Solana', WYOMING_COLORS['PURPLE'], 1),
            ('AVAX', 'Avalanche', WYOMING_COLORS['RED'], 2),
            ('DOGE', 'Dogecoin', WYOMING_COLORS['YELLOW'], 3)
        ]
        
        for symbol, name, color, lane in car_configs:
            self.cars.append(RaceCar(symbol, name, color, lane))
        
        print("🏎️ Racing Engine Initialized - 4 Cars Ready")
    
    def start_race(self):
        """Start the race"""
        self.race_active = True
        self.race_start_time = time.time()
        self.winner = None
        
        # Reset all cars
        for car in self.cars:
            car.position_on_track = 0
            car.laps_completed = 0
            car.x = CAR_CONFIG['START_X']
    
    def stop_race(self):
        """Stop the race"""
        self.race_active = False
    
    def reset_race(self):
        """Reset the race"""
        self.race_active = False
        self.winner = None
        
        for car in self.cars:
            car.position_on_track = 0
            car.laps_completed = 0
            car.x = CAR_CONFIG['START_X']
            car.speed = 0
    
    def update_car_performance(self, market_engine):
        """Update all cars based on market data"""
        for car in self.cars:
            car.update_market_data(market_engine)
    
    def update(self):
        """Update racing engine"""
        if not self.race_active:
            return
        
        dt = 1.0  # Delta time (assuming 60 FPS)
        
        # Update all cars
        for car in self.cars:
            car.update_position(dt)
        
        # Check for winner
        self.check_winner()
    
    def check_winner(self):
        """Check if any car has won the race"""
        for car in self.cars:
            if car.laps_completed >= GAME_CONFIG['LAPS_TO_WIN']:
                if not self.winner:
                    self.winner = {
                        'symbol': car.symbol,
                        'name': car.name,
                        'laps': car.laps_completed,
                        'time': time.time() - self.race_start_time
                    }
                    self.race_active = False
                return self.winner
        return None
    
    def render(self, screen):
        """Render the racing track and cars"""
        # Draw track background
        track_rect = pygame.Rect(50, 100, GAME_CONFIG['SCREEN_WIDTH'] - 100, 400)
        pygame.draw.rect(screen, WYOMING_COLORS['DARK_GRAY'], track_rect)
        pygame.draw.rect(screen, WYOMING_COLORS['GOLD'], track_rect, width=3)
        
        # Draw lane dividers
        for i in range(1, 4):
            y = 100 + (i * CAR_CONFIG['LANE_HEIGHT'])
            pygame.draw.line(screen, WYOMING_COLORS['WHITE'], 
                           (50, y), (GAME_CONFIG['SCREEN_WIDTH'] - 50, y), 1)
        
        # Draw start/finish line
        finish_x = GAME_CONFIG['SCREEN_WIDTH'] - 80
        pygame.draw.line(screen, WYOMING_COLORS['WHITE'], 
                        (finish_x, 100), (finish_x, 500), 4)
        
        # Draw checkered pattern on finish line
        for i in range(0, 400, 20):
            color = WYOMING_COLORS['WHITE'] if (i // 20) % 2 == 0 else WYOMING_COLORS['BLACK']
            pygame.draw.rect(screen, color, (finish_x - 2, 100 + i, 8, 20))
        
        # Render all cars
        for car in self.cars:
            car.render(screen)
    
    def get_race_info(self):
        """Get current race information"""
        if not self.race_active and not self.winner:
            return {
                'status': 'Ready to Race',
                'time': 0,
                'leader': None,
                'cars': self.cars
            }
        
        # Find current leader
        leader = max(self.cars, key=lambda c: (c.laps_completed, c.position_on_track))
        
        race_time = time.time() - self.race_start_time if self.race_active else 0
        
        return {
            'status': 'Racing' if self.race_active else 'Finished',
            'time': race_time,
            'leader': leader,
            'cars': self.cars,
            'winner': self.winner
        }
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
