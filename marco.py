import pygame
import math
vec = pygame.math.Vector2
#all_sprites = pygame.sprite.Group()

class rossi(pygame.sprite.Sprite):
    def __init__(self):
        super(rossi, self).__init__()
        self.image = pygame.image.load('resources/images/marco1.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.size = 120
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
        self.centerx = 50
        self.centery = 400
        self.rect = self.image.get_rect()
        self.isjump = False
        self.isshoot = False
        self.v = 8
        self.m = 2
        self.index = 0
        self.hp = 10

    def change_pos(self,x,y):
        self.centerx = self.centerx +x
        self.centery = self.centery +y
        self.rect = pygame.Rect(((self.centerx,self.centery),(self.centerx+self.size,self.centery+self.size)))

    def update(self):
        if self.isjump:
            F = (1/2) *self.m*(self.v**2)
            self.centery -= F
            self.v -= 1
            if self.v<0:
                self.m = -2
            if self.v == -9:
                self.isjump = False
                self.v, self.m = 8,2
        self.rect = pygame.Rect(((self.centerx,self.centery),(self.centerx+self.size,self.centery+self.size)))

    def motion(self,option = 0):
        walk_image = ['resources/images/marco1.png','resources/images/marco3.png','resources/images/marco4.png','resources/images/marco5.png','resources/images/marco6.png',
                            'resources/images/marco7.png','resources/images/marco8.png','resources/images/marco2.png']
        shoot_image = ['resources/images/marco11.png','resources/images/marco9.png','resources/images/marco10.png']                 
        if option == 0:
            if self.isjump == False:
                self.index = (self.index+1)%len(walk_image)
                self.image = pygame.image.load(walk_image[self.index])
                self.image = pygame.transform.scale(self.image,(self.size,self.size))
            else:
                self.image = pygame.image.load(walk_image[6])
                self.image = pygame.transform.scale(self.image,(self.size,self.size))
        elif option == 1:
            self.image = pygame.image.load(walk_image[0])
            self.image = pygame.transform.scale(self.image,(self.size,self.size))
        elif option == 2:
            self.index = (self.index+1)%len(shoot_image)
            self.image = pygame.image.load(shoot_image[self.index])
            self.image = pygame.transform.scale(self.image,(self.size,self.size))
    
    def shoot(self, screen, all_sprites, bullets):
        gun = bullet()
        gun.centerx = self.centerx+50
        gun.centery = self.centery+30
        gun.rect = pygame.Rect((gun.centerx, gun.centery),(gun.centerx+gun.size[0], gun.centery+gun.size[1]))
        all_sprites.add(gun)
        bullets.add(gun)

    def islive(self):
        if self.hp == 0:
            return 0
        return 1

class bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(bullet, self).__init__()
        self.image = pygame.image.load('resources/images/bullet.png')
        self.size = (100,20)
        self.image = pygame.transform.scale(self.image,self.size)
        self.damage = 0.5
        self.rect = pygame.Rect(self.image.get_rect())
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery
        self.speed = 30
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.centerx += self.speed
        print(self.centerx)
        self.rect = pygame.Rect((self.centerx, self.centery),(self.centerx+self.size[0], self.centery+self.size[1]))
