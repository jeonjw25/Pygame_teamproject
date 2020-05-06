import pygame
import time

def intro_music(sound): 
    pygame.mixer.init()
    pygame.mixer.music.load("resources/sound/intro_music.mp3")
    pygame.mixer.music.play(-1)

def complete_music(sound):
    pygame.mixer.init()
    pygame.mixer.music.load("resources/sound/Victory.ogg")
    pygame.mixer.music.play(-1)

def mission_complete(sound):
    pygame.mixer.music.load()

def gameover_music(sound):
    pygame.mixer.init()
    pygame.mixer.music.load("resources/sound/GameOver.ogg")
    pygame.mixer.music.play(-1)

def marco_shoot(sound):
    #pygame.mixer.init()
    ch = pygame.mixer.Sound("resources/sound/marco_attack.ogg")
    pygame.mixer.Sound.play(ch)

def marco_die(sound):
    #pygame.mixer.init()
    die = pygame.mixer.Sound("resources/sound/marco_die.ogg")
    pygame.mixer.Sound.play(die)