import pygame, sys
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
import helpScreen, sound


width, height = 1024, 876
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Metalslug")

sound.music(0.3)

def play(screen):
    pygame.init()

    backscreen = pygame.image.load("resources/images/backscreen.png")
    backscreen = pygame.transform.scale(backscreen, (1024, 876))
    screen.blit(backscreen, (0, 0))
    
    font = pygame.font.SysFont("resources/font/나눔손글씨붓.ttf", 65)
    start_button = font.render("START", True, WHITE)
    start_rect = start_button.get_rect(x = 180, y = 700)
    help_button = font.render("HELP", True, WHITE)
    help_rect = help_button.get_rect(x = 450, y = 700)
    close_button = font.render("CLOSE", True, WHITE)
    close_rect = close_button.get_rect(x = 700, y = 700)
    
    screen.blit(start_button, start_rect)
    screen.blit(help_button, help_rect)
    screen.blit(close_button, close_rect)

    pygame.display.flip()


    running = True
    while running:
        for event in pygame.event.get():
            if start_rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
            if help_rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    helpScreen.play(screen)
            if close_rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    sys.exit()
                    
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
if __name__ == "__main__":
    play(screen)