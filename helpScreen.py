import pygame, sys
from pygame.locals import *
import menu, sound

WHITE = (255, 255, 255)
width, height = 1024, 876
screen = pygame.display.set_mode((width, height))

def play(screen):
    pygame.init()

    backscreen = pygame.image.load("resources/images/helpscreen.png")
    backscreen = pygame.transform.scale(backscreen, (1024, 876))
    
    screen.blit(backscreen, (0, 0))
    
    font = pygame.font.SysFont("resources/font/나눔손글씨붓.ttf", 65)
    goback_button = font.render("Go Back", True, WHITE)
    goback_rect = goback_button.get_rect(x = 100, y = 700)
    screen.blit(goback_button, goback_rect)

    pygame.display.flip()
    
    running = True
    while running:
        for event in pygame.event.get():
            if goback_rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu.play(screen)
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    play(screen)
