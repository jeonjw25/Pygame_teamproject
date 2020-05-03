import pygame
import marco, enemy
import stage

class game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.running = True
        #event buffer
        self.keys = [False, False]
        self.score = 0
        #sprite group
        self.all_sprites = pygame.sprite.Group()
        self.enemys = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.player = marco.rossi()
        self.item = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.FPS = 30
    
    def events(self):
        for event in pygame.event.get():
            key_event = pygame.key.get_pressed()

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.keys[0] = True
                elif event.key == pygame.K_a:
                    self.player.isshoot = True
                elif event.key == pygame.K_LEFT:
                    self.keys[1] = True
                elif event.key == pygame.K_UP:
                    self.player.isjump = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.keys[0] = False
                elif event.key == pygame.K_LEFT:
                    self.keys[1] = False
                elif event.key == pygame.K_a:
                    self.player.isshoot = False

    def play(self, screen, stage):
        #stage 정보 load
        stage_info = stage
        image = stage_info.image
        rect = stage_info.rect
        buf = 0
        self.player.centerx, self.player.centery = 50, 400 #player 시작 위치


        sol = enemy.soldier()
        self.all_sprites.add(sol)
        self.enemys.add(sol)

        
        while self.running:
            self.clock.tick(self.FPS)

            self.events()

            self.player.update() #player jump
            #player move
            if self.keys[0] == True:
                movement = stage_info.move(self.player.centerx)
                self.player.motion()
                self.player.change_pos(movement,0)
            elif self.keys[1] == True:
                self.player.motion()
                if self.player.centerx > 30:
                    self.player.change_pos(-stage_info.speed,0)
            else:
                self.player.motion(1)

            #player shoot
            if self.player.isshoot == True:
                buf = (buf +1) %4
                self.player.motion(2)
                if buf == 0:
                    self.player.shoot(screen, self.all_sprites, self.bullets)
                    
            #image draw
            stage_info.draw(screen)
            self.draw(stage_info, screen)
        pygame.quit()

    def draw(self, stage, screen):
        self.all_sprites.update()
        stage.draw(screen)
        self.all_sprites.draw(screen)
        self.bullets.draw(screen)
        self.item.draw(screen)
        print(self.all_sprites)
        pygame.display.update()