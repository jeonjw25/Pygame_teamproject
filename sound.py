import pygame
import time
from pygame import *

def music(sound):
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load("resources/sound/intro_music.mp3")
    pygame.mixer.music.play(-1)