import pygame, sys


width, height = 1024, 876
screen = pygame.display.set_mode((width, height))

def play(screen):
    pygame.init()

    backscreen = pygame.image.load("resources/images/backscreen.png")
    backscreen = pygame.transform.scale(backscreen, (1024, 876))
    screen.blit(backscreen, (0, 0))

    pygame.display.flip()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    play(screen)
