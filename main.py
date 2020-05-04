#import screen #screen(image, option) option 0:menu, 1:help, 2:complete, 3:gameover
import pygame
from stage import *
from start import *
from f_screen import *

if __name__ == "__main__":
    g = start.game()
    screen = pygame.display.set_mode((1000,736))
    pygame.display.set_caption("METAL SLUG")
    menu(screen)
    if g.play(screen, stage.stage1()):
        print('complete')
        pygame.quit()
        # if g.play(screen, stage.stage1.boss_stage()) == 1:
            # screen.menu(image,2)a
            # complete(screen)
        # else:
            # screen.menu(image,3)aaa
            # gameover(screen)
    else:
        screen = pygame.display.set_mode((1000,600))
        gameover(screen)
    pygame.quit()