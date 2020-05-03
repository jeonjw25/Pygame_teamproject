#import screen #screen(image, option) option 0:menu, 1:help, 2:complete, 3:gameover
import pygame
from stage import *
from start import *
from f_screen import *

if __name__ == "__main__":
    pygame.init()
    g = start.game()
    screen = pygame.display.set_mode((1000,657))
    pygame.display.set_caption("METAL SLUG")
    menu(screen)

    if g.play(screen, stage.stage1()) == 1:
        print('complete')
        # if g.play(screen, stage.stage1.boss_stage()) == 1:
            # screen.menu(image,2)a
            # complete(screen)
        # else:
            # screen.menu(image,3)aaa
            # gameover(screen)
    else:
        #screen.menu(image, 3)
        gameover(screen)
    pygame.quit()
