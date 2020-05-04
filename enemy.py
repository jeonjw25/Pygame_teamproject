import pygame
import item
import random

class soldier(pygame.sprite.Sprite):
    def __init__(self):
        super(soldier, self).__init__()
        self.image = pygame.image.load('resources/images/enemy/enemy2/soldier1.png')
        self.size = 120
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
        self.posx, self.posy = 0, 0
        self.rect = pygame.Rect((self.image.get_rect()))
        self.rect.move_ip(self.posx, self.posy)
        self.ishit = False
        self.hitno = 0
        self.iswalk = False
        self.speed = 5
        self.index = 0
        self.walk_index = 0
        self.shoot_index = 0
        self.isshoot = False
        self.delay = 0

    def gen(self, y):
        self.update(1000,y)

    def hit(self, all_sprites, bullets):
        hits = pygame.sprite.spritecollide(self ,bullets ,False)
        if hits:
            self.ishit = True
            all_sprites.remove(hits[0])
            bullets.remove(hits[0])
            return True

    def update(self, x=0, y=0):
        if self.iswalk == True:
            self.posx -= self.speed
            self.rect.move_ip(-self.speed, 0)
        self.posx +=x
        self.posy +=y
        self.rect.move_ip(x, y)

    def shoot(self, all_sprites, enemy_bullets):
        self.delay += 1
        if self.isshoot == True and self.delay%25 == 0:
            gun = enemy_bullet()
            gun.rect.move_ip(self.posx, self.posy+20)
            enemy_bullets.add(gun)
            all_sprites.add(gun)

    def motion(self, all_sprites, enemys, items):
        hit_image = ['resources/images/enemy/enemy2/soldier8.png','resources/images/enemy/enemy2/soldier9.png']
        walk_image = ['resources/images/enemy/enemy2/soldier1.png','resources/images/enemy/enemy2/soldier2.png','resources/images/enemy/enemy2/soldier3.png','resources/images/enemy/enemy2/soldier4.png']
        shoot_image = ['resources/images/enemy/enemy2/soldier5.png','resources/images/enemy/enemy2/soldier6.png','resources/images/enemy/enemy2/soldier7.png']
        if self.hitno == 2:
            new_item = item.ITEM()
            new_item.rect.move_ip(self.posx, self.posy+60)
            items.add(new_item)
            all_sprites.add(new_item)
            all_sprites.remove(self)
            enemys.remove(self)
        if self.ishit and self.hitno<2:
            self.index = (self.hitno)%len(hit_image)
            self.image = pygame.image.load(hit_image[self.hitno])
            self.image = pygame.transform.scale(self.image,(self.size,self.size))
            self.hitno += 1
        elif self.iswalk == True:
            self.walk_index = (self.walk_index+1) % len(walk_image)
            self.image = pygame.image.load(walk_image[self.walk_index])
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
        else:
            self.image = pygame.image.load('resources/images/enemy/enemy2/soldier1.png')
            self.image = pygame.transform.scale(self.image,(self.size,self.size))
        if self.isshoot ==True and self.delay%25 == 0:
            self.shoot_index = (self.shoot_index + 1) % len(shoot_image)
            self.image = pygame.image.load(shoot_image[self.shoot_index])
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
        elif self.isshoot ==True:
            self.image = pygame.image.load(shoot_image[0])
            self.image = pygame.transform.scale(self.image, (self.size, self.size))

class enemy_bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(enemy_bullet, self).__init__()
        self.image = pygame.image.load('resources/images/bullet/bullet6.png')
        self.size = (40,40)
        self.image = pygame.transform.scale(self.image,self.size)
        self.posx = 0
        self.posy = 0
        self.damage = 0.5
        self.rect = pygame.Rect(self.image.get_rect())
        self.speed = 30
        self.mode = 0

    def update(self, x=0, y=0):
        if self.mode == 0:
            self.posx -= self.speed
            self.rect.move_ip(-self.speed,0)
        elif self.mode == 1:
            self.posy += self.speed
            self.rect.move_ip(0, self.speed)
        self.posx +=x
        self.posy +=y
        self.rect.move_ip(x, y)

    def gun_change(self):
        self.mode = 1
        self.image = pygame.image.load('resources/images/bullet/bullet9.png')
        self.size = (100, 120)
        self.image = pygame.transform.scale(self.image, self.size)
        self.damage = 1
        self.speed = 15



class UFO(pygame.sprite.Sprite):
    def __init__(self):
        super(UFO, self).__init__()
        self.image = pygame.image.load('resources/images/ufo/ufo1.png')
        self.size = 120
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.posx, self.posy = 0,0
        self.rect = pygame.Rect((self.image.get_rect()))
        self.rect.move_ip(self.posx, self.posy)
        self.ishit = False
        self.hitno = 0
        self.delay = 0
        self.isshoot = True
        self.speed = 2

    def motion(self, all_sprites, enemys, items):
        hit_image = ['resources/images/ufo/ufo4.png', 'resources/images/ufo/ufo5.png', 'resources/images/ufo/ufo6.png']
        if self.hitno == 3:
            all_sprites.remove(self)
            enemys.remove(self)
        if self.ishit and self.hitno < 3:
            self.index = (self.hitno) % len(hit_image)
            self.image = pygame.image.load(hit_image[self.hitno])
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
            self.hitno += 1
        else:
            self.image = pygame.image.load('resources/images/ufo/ufo1.png')
            self.image = pygame.transform.scale(self.image, (self.size, self.size))

    def hit(self, all_sprites, bullets):
        hits = pygame.sprite.spritecollide(self, bullets, False)
        if hits:
            self.ishit = True
            all_sprites.remove(hits[0])
            bullets.remove(hits[0])
            return True

    def gen(self, y):
        self.posx = 1000
        self.posy = y
        self.rect.move_ip(1000, y)

    def update(self, x=0, y=0):
        self.posx -= self.speed
        self.rect.move_ip(-self.speed, 0)
        self.posx += x
        self.posy += y
        self.rect.move_ip(x, y)

    def shoot(self, all_sprites, enemy_bullets):
        self.delay += 1
        if self.delay%25 == 0:
            gun = enemy_bullet()
            gun.gun_change()
            gun.rect.move_ip(self.posx, self.posy)
            enemy_bullets.add(gun)
            all_sprites.add(gun)

# class boss(pygame.sprite.Sprite):
#     def __init__(self):
#         super(boss, self).__init__()
#         self.image = pygame.image.load('resources/images/boss/boss1.png')
#         self.size = 200
#         self.image = pygame.transform.scale(self.image, (self.size, self.size))
#         self.rect = self.image.get_rect()
#         self.posx = 800  # 그냥 초기화값
#         self.posy = 300  # 그냥 초기화값
#         self.ishit = False
#         self.hitno = 0
#         self.mode = 0

#     def motion(self, all_sprites, enemys, items):
#         hit_image = ['resources/images/boss/boss1.png']
#         if self.hitno == 50:
#             all_sprites.remove(self)
#             enemys.remove(self)
#         if self.ishit and self.hitno < 45:
#             self.index = (self.hitno) % len(hit_image)
#             self.image = pygame.image.load(hit_image[0])
#             self.image = pygame.transform.scale(self.image, (self.size, self.size))
#             self.hitno += 1
#         elif self.ishit and self.hitno < 45:  # 마지막 다섯대 맞을동안 폭발하는이미지출력
#             self.image = pygame.image.load('resources/images/boss/boss_die.png')
#             self.image = pygame.transform.scale(self.image, (self.size, self.size))
#             self.hitno += 1

#         else:
#             self.image = pygame.image.load('resources/images/boss/boss1.png')
#             self.image = pygame.transform.scale(self.image, (self.size, self.size))

#     def hit(self, all_sprites, bullets, enemys):
#         hits = pygame.sprite.spritecollide(self, bullets, False)
#         if hits:
#             self.ishit = True
#             all_sprites.remove(hits[0])
#             bullets.remove(hits[0])
#             return True

#     def update(self, x=0, y=0):
#         self.posx += x
#         self.posy += y
#         self.rect.move_ip(x, y)