#import screen #screen(image, option) option 0:menu, 1:helf, 2:complete, 3:gameover
import pygame
import stage, start

if __name__ == "__main__":
    pygame.init()
    g = start.game()
    screen = pygame.display.set_mode((1000,657))
    pygame.display.set_caption("METAL SLUG")
    #screen.menu(image, 0)
    if g.play(screen, stage.stage1()) == 1:
        print('complete')
        #if game.play(image, stage.boss_stage()) == 1:
            #screen.menu(image,2)a
        #else:
            #screen.menu(image,3)a
    #else:
        #screen.menu(image, 3)
    pygame.quit()