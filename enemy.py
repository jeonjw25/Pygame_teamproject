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

    def gen(self, y): #적출현
        self.update(1000,y)

    def hit(self, all_sprites, bullets, player): #적이 총에맞았을때
        hits = pygame.sprite.spritecollide(self ,bullets ,False)
        if hits:
            self.ishit = True
            all_sprites.remove(hits[0])
            bullets.remove(hits[0])
            player.score += 5
            return True

    def update(self, x=0, y=0): #화면이동에따른 적위치이동
        if self.iswalk == True:
            self.posx -= self.speed
            self.rect.move_ip(-self.speed, 0)
        self.posx +=x
        self.posy +=y
        self.rect.move_ip(x, y)

    def shoot(self, all_sprites, enemy_bullets): #적 총발사
        self.delay += 1
        if self.isshoot == True and self.delay%25 == 0:
            gun = enemy_bullet()
            gun.rect.move_ip(self.posx, self.posy+20)
            enemy_bullets.add(gun)
            all_sprites.add(gun)

    def motion(self, all_sprites, enemys, items): #적 행동모션
        hit_image = ['resources/images/enemy/enemy2/soldier10.png','resources/images/enemy/enemy2/soldier11.png']
        walk_image = ['resources/images/enemy/enemy2/soldier1.png','resources/images/enemy/enemy2/soldier2.png','resources/images/enemy/enemy2/soldier3.png','resources/images/enemy/enemy2/soldier4.png']
        shoot_image = ['resources/images/enemy/enemy2/soldier8.png','resources/images/enemy/enemy2/soldier9.png']
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

class enemy_bullet(pygame.sprite.Sprite): #적총알
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
 
    def update(self, x=0, y=0): #적 총알 위치변경
        if self.mode == 0:
            self.posx -= self.speed
            self.rect.move_ip(-self.speed,0)
        elif self.mode == 1:
            self.posy += self.speed
            self.rect.move_ip(0, self.speed)
        self.posx +=x
        self.posy +=y
        self.rect.move_ip(x, y)

    def gun_change(self): #총알변경
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

    def hit(self, all_sprites, bullets, player): #적이 총에맞앗을때
        hits = pygame.sprite.spritecollide(self, bullets, False)
        if hits:
            self.ishit = True
            all_sprites.remove(hits[0])
            bullets.remove(hits[0])
            player.score += 10
            return True

    def gen(self, y): #적 생성위치
        self.posx = 1000
        self.posy = y
        self.rect.move_ip(1000, y)

    def update(self, x=0, y=0): #적 위치이동
        self.posx -= self.speed
        self.rect.move_ip(-self.speed, 0)
        self.posx += x
        self.posy += y
        self.rect.move_ip(x, y)

    def shoot(self, all_sprites, enemy_bullets): #적 총발사
        self.delay += 1
        if self.delay%25 == 0:
            gun = enemy_bullet()
            gun.gun_change()
            gun.rect.move_ip(self.posx, self.posy)
            enemy_bullets.add(gun)
            all_sprites.add(gun)

class boss(pygame.sprite.Sprite):
     def __init__(self):
         super(boss, self).__init__()
         self.image = pygame.image.load('resources/images/boss/boss1.png')
         self.size = (300,300)
         self.image = pygame.transform.scale(self.image, self.size)
         self.rect = self.image.get_rect()
         self.posx = 400
         self.posy = -400
         self.hp = 30
         self.speed = 7
         self.xdirection = 0
         self.ydirection = 0
         self.hit_size = (30,30)
         self.isshoot = True
         self.delay = 0
         self.endsig = False
         self.hit_effect = pygame.image.load('resources/images/ufo/ufo7.png')

     def motion(self, all_sprites =None, enemys = None, items = None):
         pass

     def hit(self, all_sprites, bullets, screen):
         hits = pygame.sprite.spritecollide(self, bullets, False)
         if hits:
             self.hp -= hits[0].damage
             all_sprites.remove(hits[0])
             bullets.remove(hits[0])
             if self.hp < 4:
                self.image = pygame.image.load('resources/images/boss/boss3.png')
                self.image = pygame.transform.scale(self.image, self.size)
                self.isshoot = False
             elif self.hp < 15:
                self.image = pygame.image.load('resources/images/boss/boss2.png')
                self.image = pygame.transform.scale(self.image, self.size)
             


     def shoot(self, all_sprites, enemy_bullets):
         self.delay += 1
         if self.delay %25 == 0:
             gun = enemy_bullet()
             gun.gun_change()
             gun.image = pygame.image.load('resources/images/boss/boss_bullet.png')
             gun.size = (40,40)
             gun.rect.move_ip(self.posx+150, self.posy+200)
             enemy_bullets.add(gun)
             all_sprites.add(gun)

     def update(self, x=0, y=0):
         if self.endsig == True:
             self.ydirection += self.speed
             self.rect.move_ip(0,self.speed)

         if self.ydirection<0:
             self.ydirection += self.speed
             self.rect.move_ip(0,self.speed)
         else:
             if self.xdirection == 0: #오른쪽으로 이동
                 self.posx += self.speed
                 if self.posx > 700:
                     self.xdirection = 1
             else: #왼쪽으로 이동
                 self.posx -= self.speed
                 if self.posx < 0:
                     self.xdirection = 0
             if self.ydirection == 0: #위로 이동
                 self.posy -= self.speed
                 if self.posy < 0:
                     self.ydirection = 1
             else: #아래로 이동
                 self.posy += self.speed
                 if self.posy > 150:
                     self.ydirection = 0
             self.posx += x
             self.posy += y
             self.rect = pygame.Rect((self.posx,self.posy),self.size)