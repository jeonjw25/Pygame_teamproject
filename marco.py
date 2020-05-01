import pygame
import math
vec = pygame.math.Vector2
#all_sprites = pygame.sprite.Group()

class rossi(pygame.sprite.Sprite):
    def __init__(self):
        super(rossi, self).__init__()
        self.image = pygame.image.load('./images/marco1.png')
        self.size = 120
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
        self.rect = self.image.get_rect()
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery
        self.isjump = False
        self.isshoot = False
        self.v = 8
        self.m = 2
        self.index = 0

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
        walk_image = ['./images/marco1.png','./images/marco2.png','./images/marco3.png','./images/marco4.png','./images/marco5.png',
                            './images/marco6.png','./images/marco7.png','./images/marco8.png']
        shoot_image = ['./images/marco9.png','./images/marco10.png','./images/marco11.png','./images/marco12.png']                 
        if option == 0:
            if self.isjump == False:
                self.index = (self.index+1)%len(walk_image)
                self.image = pygame.image.load(walk_image[self.index])
                self.image = pygame.transform.scale(self.image,(self.size,self.size))
            else:
                self.image = pygame.image.load(walk_image[4])
                self.image = pygame.transform.scale(self.image,(self.size,self.size))
        elif option == 1:
            self.image = pygame.image.load(walk_image[1])
            self.image = pygame.transform.scale(self.image,(self.size,self.size))
        elif option == 2:
            self.index = (self.index+1)%len(shoot_image)
            self.image = pygame.image.load(shoot_image[self.index])
            self.image = pygame.transform.scale(self.image,(self.size,self.size))
    
    def shoot(self, screen, bullets):
        gun = bullet()
        gun.centerx = self.centerx+50
        gun.centery = self.centery+30
        bullets.gun_list.append(gun)
        
class bullets:
    def __init__(self):
        self.gun_list = []

class bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(bullet, self).__init__()
        self.image = pygame.image.load('./images/bullet.png')
        self.image = pygame.transform.scale(self.image,(100,20))
        self.damage = 0.5
        self.rect = self.image.get_rect()
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery
        self.speed = 20
