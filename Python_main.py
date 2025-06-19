# StoneVerse Stockcar Racing - Wyoming Protocol 7
import pygame
import sys
import math
import random

# Initialize pygame
pygame.init()
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CRYPTO CLASHERS RACING")
clock = pygame.time.Clock()

# Wyoming Protocol 7 colors
STONE_GOLD = (255, 215, 0)
WYOMING_PURPLE = (128, 0, 128)
TRACK_COLOR = (50, 50, 70)

class Car:
    def __init__(self, x, y, color, name):
        self.x = x
        self.y = y
        self.color = color
        self.name = name
        self.speed = 0
        self.max_speed = 8 + random.randint(0, 5)
        self.angle = 0
        self.laps = 0
        
    def draw(self):
        # Draw car body
        car_rect = pygame.Rect(self.x - 20, self.y - 10, 40, 20)
        pygame.draw.rect(screen, self.color, car_rect)
        
        # Draw car details
        pygame.draw.rect(screen, (30, 30, 30), (self.x + 10, self.y - 5, 10, 10))
        font = pygame.font.SysFont(None, 24)
        text = font.render(self.name, True, (255, 255, 255))
        screen.blit(text, (self.x - 15, self.y - 30))
        
        # Draw speed indicator
        speed_text = font.render(f"{self.speed:.1f} MPH", True, STONE_GOLD)
        screen.blit(speed_text, (self.x - 25, self.y + 15))

def draw_track():
    # Outer track
    pygame.draw.rect(screen, TRACK_COLOR, (100, 100, WIDTH-200, HEIGHT-200), 2)
    
    # Start/finish line
    pygame.draw.rect(screen, STONE_GOLD, (WIDTH//2 - 50, HEIGHT - 150, 100, 10))
    
    # Wyoming branding
    font = pygame.font.SysFont(None, 48)
    title = font.render("CRYPTO CLASHERS RACING", True, WYOMING_PURPLE)
    screen.blit(title, (WIDTH//2 - title.get_width()//2, 20))
    
    subtitle = font.render("WHERE MARKETS MOVE RACING", True, STONE_GOLD)
    screen.blit(subtitle, (WIDTH//2 - subtitle.get_width()//2, 70))

def main():
    # Create cars
    cars = [
        Car(WIDTH//2, HEIGHT - 200, (255, 0, 0), "BTC"),
        Car(WIDTH//2 + 50, HEIGHT - 200, (0, 255, 0), "ETH"),
        Car(WIDTH//2 - 50, HEIGHT - 200, (0, 0, 255), "SOL"),
        Car(WIDTH//2 + 100, HEIGHT - 200, (255, 165, 0), "AVAX")
    ]
    
    race_started = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    race_started = True
                if event.key == pygame.K_r:
                    # Reset race
                    for i, car in enumerate(cars):
                        car.x = WIDTH//2 - 150 + i * 100
                        car.y = HEIGHT - 200
                        car.speed = 0
                        car.laps = 0
        
        screen.fill((30, 30, 50))  # StoneVerse dark background
        
        # Draw track and UI
        draw_track()
        
        # Move cars if race started
        if race_started:
            for car in cars:
                car.speed = min(car.speed + 0.05, car.max_speed)
                car.y -= car.speed
                
                # Lap detection
                if car.y < 150:
                    car.y = HEIGHT - 150
                    car.laps += 1
                    if car.laps >= 3:
                        print(f"{car.name} WINS!")
                        race_started = False
        
        # Draw cars
        for car in cars:
            car.draw()
        
        # Draw controls
        font = pygame.font.SysFont(None, 36)
        if not race_started:
            start_text = font.render("PRESS SPACE TO START RACE", True, STONE_GOLD)
            screen.blit(start_text, (WIDTH//2 - start_text.get_width()//2, HEIGHT - 50))
        
        reset_text = font.render("PRESS R TO RESET", True, (200, 200, 200))
        screen.blit(reset_text, (WIDTH//2 - reset_text.get_width()//2, HEIGHT - 100))
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
python main.py
pip install -r requirements.txt
python main.py
# AGE VERIFICATION SCREEN
def age_verification():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.SysFont(None, 48)
    
    while True:
        screen.fill((30, 30, 50))  # StoneVerse dark
        title = font.render("STONEVERSE STOCKCAR RACING", True, (255, 215, 0))
        warning = font.render("You must be 21+ to enter", True, (255, 100, 100))
        prompt = font.render("Press Y to confirm age", True, (200, 200, 255))
        
        screen.blit(title, (400 - title.get_width()//2, 150))
        screen.blit(warning, (400 - warning.get_width()//2, 250))
        screen.blit(prompt, (400 - prompt.get_width()//2, 350))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return  # Age confirmed
def main():
    age_verification()  # FIRST LINE
    # Rest of game...
