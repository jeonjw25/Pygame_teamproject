import pygame
import marco
import time

pygame.init()
clock = pygame.time.Clock()
FPS = 30
keys = [False,False,False] #화살표 키 값의 상태를 저장해 놓는 배열

screen = pygame.display.set_mode((1000,657))
buf = 0
w1, h1, w2, h2 = 0, 0, 400, 400
rect = pygame.Rect(((w1,h1),(w2,h2)))
image = pygame.image.load("./map1.png").convert_alpha()
image = pygame.transform.scale(image,(3510,657))
width, height = 200, 200
player = marco.rossi()
player.centerx, player.centery = 50, 400
player.rect = (player.centerx,player.centery,width,height)
running = True
shooting = marco.bullets()
while running:
    clock.tick(FPS)
    rect = pygame.Rect((w1,h1),(w2,h2))
    for event in pygame.event.get():
        key_event = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                keys[0] = True
            elif event.key == pygame.K_a:
                player.isshoot = True
            elif event.key == pygame.K_LEFT:
                keys[1] = True
            elif event.key == pygame.K_UP:
                player.isjump = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                keys[0] = False
            elif event.key == pygame.K_LEFT:
                keys[1] = False
            elif event.key == pygame.K_a:
                player.isshoot = False

    player.update()
    if keys[0] == True and player.centerx >= 500:
        w1 -= 10
        w2 -= 10
        player.motion()
    elif keys[1] == True and player.centerx < 50:
        player.motion()
        pass
    elif keys[0] == True:
        player.motion()
        player.change_pos(10,0)
    elif keys[1] == True:
        player.motion()
        player.change_pos(-10,0)
    else:
        player.motion(1)
    if player.isshoot == True:
        buf = (buf +1) %5
        player.motion(2)
        if buf == 0:
            player.shoot(screen, shooting)
    screen.blit(image,rect)
    for i in shooting.gun_list:
        screen.blit(i.image,i.rect)
        i.centerx += 30
        i.rect = pygame.Rect(((i.centerx,i.centery),(i.centerx+50,i.centery+30)))
    screen.blit(player.image,player.rect)
    pygame.display.update()

pygame.quit()