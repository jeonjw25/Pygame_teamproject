import pygame
import time
from pygame import *

def intro_music(sound):
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load("resources/sound/intro_music.mp3")
    pygame.mixer.music.play(-1)

def complete_music(sound):
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load("resources/sound/victory.ogg")
    pygame.mixer.music.play(-1)

def gameover_music(sound):
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load("resources/sound/GameOver.ogg")
    pygame.mixer.music.play(-1)
