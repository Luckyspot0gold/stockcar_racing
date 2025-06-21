# stockcar_racing_emergency.py
import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("STOCKCAR RACING - WYOMING PROTOCOL 7")

# Colors
BACKGROUND = (30, 30, 50)
TRACK_COLOR = (50, 50, 70)
GOLD = (255, 215, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 120, 255)

# Cars
cars = [
    {"x": 200, "y": 500, "color": RED, "name": "BTC", "speed": 0, "laps": 0},
    {"x": 400, "y": 500, "color": GREEN, "name": "ETH", "speed": 0, "laps": 0},
    {"x": 600, "y": 500, "color": BLUE, "name": "AVAX", "speed": 0, "laps": 0}
]

race_started = False
font = pygame.font.SysFont(None, 36)

def draw_track():
    # Draw oval track
    pygame.draw.rect(screen, TRACK_COLOR, (100, 100, 600, 400), 0)
    pygame.draw.rect(screen, GOLD, (100, 100, 600, 400), 4)
    # Start/finish line
    pygame.draw.rect(screen, (255, 255, 255), (390, 480, 20, 20))

def main():
    global race_started
    
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not race_started:
                    race_started = True
                if event.key == pygame.K_r:
                    race_started = False
                    for car in cars:
                        car["y"] = 500
                        car["speed"] = 0
                        car["laps"] = 0
        
        screen.fill(BACKGROUND)
        draw_track()
        
        # Update cars
        if race_started:
            for car in cars:
                # Random speed for simplicity (replace with market data)
                car["speed"] = random.uniform(0.5, 2.5)
                car["y"] -= car["speed"]
                
                # Lap counting
                if car["y"] < 150:
                    car["y"] = 500
                    car["laps"] += 1
                    if car["laps"] >= 3:
                        win_text = font.render(f"{car['name']} WINS!", True, GOLD)
                        screen.blit(win_text, (WIDTH//2 - win_text.get_width()//2, 50))
                        race_started = False
        
        # Draw cars
        for car in cars:
            pygame.draw.rect(screen, car["color"], (car["x"]-20, car["y"]-10, 40, 20))
            name_text = font.render(car["name"], True, (255,255,255))
            screen.blit(name_text, (car["x"]-15, car["y"]-40))
            speed_text = font.render(f"{car['speed']:.1f} mph", True, GOLD)
            screen.blit(speed_text, (car["x"]-25, car["y"]+15))
            laps_text = font.render(f"Laps: {car['laps']}/3", True, (200,200,200))
            screen.blit(laps_text, (car["x"]-20, car["y"]-70))
        
        # Draw UI
        title = font.render("STOCKCAR RACING - WYOMING PROTOCOL 7", True, GOLD)
        screen.blit(title, (100, 20))
        
        if not race_started:
            start_text = font.render("PRESS SPACE TO START RACE", True, GREEN)
            screen.blit(start_text, (WIDTH//2 - start_text.get_width()//2, 550))
        
        reset_text = font.render("PRESS R TO RESET", True, (200,200,200))
        screen.blit(reset_text, (WIDTH//2 - reset_text.get_width()//2, 520))
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
