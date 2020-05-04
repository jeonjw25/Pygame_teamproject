import pygame

import marco, enemy
import stage

class game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.running = True
        #event buffer
        self.keys = [False, False, False]
        self.score = 0
        #sprite group
        self.all_sprites = pygame.sprite.Group()
        self.enemys = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.player = marco.rossi()
        self.items = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.FPS = 20
        self.stage_no = 0
        # health
        self.health_img = pygame.image.load("resources/images/health/health.png")
        self.healthbar_img = pygame.image.load("resources/images/health/healthbar.png")
        self.healthbar_img = pygame.transform.scale(self.healthbar_img, (195, 20))
        self.a = 0
        # score
        self.score = 0
        self.font = pygame.font.SysFont("resources/font/metal1.ttf", 35)
        self.text = self.font.render(("SCORE : " ), True, (0, 0, 0))


    
    def events(self):
        for event in pygame.event.get():
            key_event = pygame.key.get_pressed()

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.isup = True
                    self.keys[2] = True
                elif event.key == pygame.K_RIGHT:
                    self.keys[0] = True
                elif event.key == pygame.K_a:
                    self.player.isshoot = True
                elif event.key == pygame.K_LEFT:
                    self.keys[1] = True
                elif event.key == pygame.K_SPACE:
                    self.player.isjump = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.keys[0] = False
                elif event.key == pygame.K_LEFT:
                    self.keys[1] = False
                elif event.key == pygame.K_UP:
                    self.player.isup = False
                    self.keys[2] = False
                elif event.key == pygame.K_a:
                    self.player.isshoot = False

    def play(self, screen, stage):
        #stage 정보 load
        stage_info = stage
        image = stage_info.image
        rect = stage_info.rect
        buf = 0
        self.player.posx, self.player.posy = 50, 400 #player 시작 위치

        
        while self.running:
            if self.player.hp == 0:
                return 0
            if self.stage_no == 0:
                stage_info.generation_soldier(self.all_sprites, self.enemys)
                stage_info.generation_movesoldier(self.all_sprites, self.enemys)
                stage_info.generation_shootsoldier(self.all_sprites, self.enemys, self.enemy_bullets)
                stage_info.generation_ufo(self.all_sprites, self.enemys, self.enemy_bullets)
            self.clock.tick(self.FPS)
            #isend로 화면전환
            self.events()
            self.player.update() #player jump
            #player move
            if self.keys[0] == True:
                movement = stage_info.move(self.player)
                if movement == 0:
                    self.enemys.update(-self.player.speed)
                    self.items.update(-self.player.speed)
                elif movement == -1:
                    break
                if self.keys[0] and self.keys[2] == True:
                    self.player.motion(3)
                else:
                    self.player.motion()
                self.player.update(movement,0)
            elif self.keys[1] == True:
                if self.keys[1] == True and self.keys[2] == True:
                    self.player.motion(3)
                else:
                    self.player.motion()
                if self.player.posx > 30:
                    self.player.update(-stage_info.speed,0)
            elif self.keys[2] == True:
                self.player.motion(3)
            else:
                self.player.motion(1)
            #적 생성
            for i in self.enemys:
                if i.isshoot == True:
                    i.shoot(self.all_sprites, self.enemy_bullets)
            #player shoot
            if self.player.isshoot == True:
                buf = (buf +1) %4
                if self.keys[2] is True:
                    self.player.motion(3)
                else:
                    self.player.motion(2)
                if buf == 0:
                    self.player.shoot(screen, self.all_sprites, self.bullets)
            for i in self.bullets:
                if i.posx > 1000:
                    self.all_sprites.remove(i)
                    self.bullets.remove(i)
            #츙돌처리
            for i in self.enemys:
                i.hit(self.all_sprites, self.bullets)
                i.motion(self.all_sprites, self.enemys, self.items)
            self.player.hit(self.all_sprites, self.items, self.enemy_bullets)
            #image draw
            self.draw(stage_info, screen)
        return 1

    def draw(self, stage, screen):
        self.all_sprites.update()
        stage.draw(screen)
        self.all_sprites.draw(screen)
        screen.blit(self.healthbar_img, (25, 25))
        for i in range(self.player.hp*19):
            screen.blit(self.health_img, (i+28, 28))
        screen.blit(self.text, (30, 50))
        pygame.display.update()

    