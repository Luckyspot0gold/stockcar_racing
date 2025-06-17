pip install pygame pandas ccxt websockets numpy
# test_engine.py
import pygame
import pandas as pd
from datetime import datetime

print("PYGAME VERSION:", pygame.__version__)
print("PANDAS VERSION:", pd.__version__)
print("CURRENT TIME:", datetime.now())

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ENGINE TEST")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((30, 30, 70))
    pygame.draw.circle(screen, (220, 20, 60), (400, 300), 50)
    pygame.display.flip()
