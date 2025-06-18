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
