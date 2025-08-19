# Wyoming Protocol 7 - Guaranteed Working Racing Core
import pygame
import sys
import random

# Initialize with fail-safe defaults
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("STOCKCAR RACING - Wyoming Protocol 7")

# StoneVerse colors
BACKGROUND = (30, 30, 50)
TRACK_COLOR = (70, 70, 90)
GOLD = (255, 215, 0)
RED = (220, 60, 60)
GREEN = (60, 220, 60)
BLUE = (60, 120, 220)

cars = [
    {"x": 200, "y": 500, "color": RED, "name": "BTC", "speed": 0},
    {"x": 350, "y": 500, "color": GREEN, "name": "ETH", "speed": 0},
    {"x": 500, "y": 500, "color": BLUE, "name": "AVAX", "speed": 0}
]

race_started = False
font = pygame.font.SysFont(None, 36)

def draw_track():
    # Simple oval track
    pygame.draw.rect(screen, TRACK_COLOR, (100, 100, 600, 400), 0)
    pygame.draw.rect(screen, GOLD, (100, 100, 600, 400), 4)
    # Start/finish line
    pygame.draw.rect(screen, (255, 255, 255), (390, 480, 20, 20))

def main():
    global race_started
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    race_started = True
                if event.key == pygame.K_r:
                    # Reset cars
                    for car in cars:
                        car["y"] = 500
                        car["speed"] = 0
                    race_started = False
        
        screen.fill(BACKGROUND)
        draw_track()
        
        # Update cars
        if race_started:
            for car in cars:
                car["speed"] = min(car["speed"] + 0.05, random.uniform(3.0, 7.0))
                car["y"] -= car["speed"]
                
                # Lap detection
                if car["y"] < 150:
                    car["y"] = 500
                    # Wyoming achievement
                    pygame.draw.circle(screen, GOLD, (car["x"], 100), 30)
                    win_text = font.render(f"{car['name']} LAP!", True, GOLD)
                    screen.blit(win_text, (300, 50))
        
        # Draw cars
        for car in cars:
            pygame.draw.rect(screen, car["color"], (car["x"]-20, car["y"]-10, 40, 20))
            name_text = font.render(car["name"], True, (255,255,255))
            screen.blit(name_text, (car["x"]-15, car["y"]-40))
            speed_text = font.render(f"{car['speed']:.1f} MPH", True, GOLD)
            screen.blit(speed_text, (car["x"]-25, car["y"]+15))
        
        # Draw UI
        title = font.render("STOCKCAR RACING - WYOMING PROTOCOL 7", True, GOLD)
        screen.blit(title, (150, 20))
        
        if not race_started:
            start_text = font.render("PRESS SPACE TO START RACE", True, GREEN)
            screen.blit(start_text, (250, 550))
        
        reset_text = font.render("PRESS R TO RESET", True, (200,200,200))
        screen.blit(reset_text, (300, 520))
        
        pygame.display.flip()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()
