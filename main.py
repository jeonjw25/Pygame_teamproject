#import screen #screen(image, option) option 0:menu, 1:help, 2:complete, 3:gameover
import pygame
from stage import *
from start import *
from f_screen import *
from sound import *
import marco


if __name__ == "__main__":
    g = start.game()
    screen = pygame.display.set_mode((1000,736))
    pygame.display.set_caption("METAL SLUG")
    menu(screen)
    while g.running:
        if g.play(screen, stage1()):
            g.all_sprites.empty()
            g.enemy_bullets.empty()
            g.enemys.empty()
            g.stage_no = 1
            shootmode = g.player.shootMode
            score = g.player.score
            hp = g.player.hp
            g.player = marco.rossi(shootmode, score, hp)
            g.all_sprites.add(g.player)
            if g.play(screen, boss_stage()):
                if complete(screen) == 1: #게임재시작
                    sound.intro_music(0.3)
                    g = start.game()
                    screen = pygame.display.set_mode((1000, 736))
                    pygame.display.set_caption("METAL SLUG")
            else:
                screen = pygame.display.set_mode((1000,600)) 
                marco_die(0.3)
                if gameover(screen)== 1: #게임 재시작
                    sound.intro_music(0.3)
                    g = start.game()
                    screen = pygame.display.set_mode((1000, 736))
                    pygame.display.set_caption("METAL SLUG")
        else:
            screen = pygame.display.set_mode((1000,600))
            marco_die(0.3)
            if gameover(screen)== 1:
                sound.intro_music(0.3)
                g = start.game()
                screen = pygame.display.set_mode((1000, 736))
                pygame.display.set_caption("METAL SLUG")
    pygame.quit() 
