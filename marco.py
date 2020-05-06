import pygame
from sound import *

class rossi(pygame.sprite.Sprite): #주인공
    def __init__(self, bullet = None, score = 0, hp = 10):
        super(rossi, self).__init__()
        self.image = pygame.image.load('resources/images/movement/walk/1.gif')
        self.org_size = self.image.get_size()
        self.mask = pygame.mask.from_surface(self.image)
        self.size = (120, 230)
        self.image = pygame.transform.scale(self.image,self.size)
        self.posx = 50
        self.posy = 400
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.move_ip(self.posx,self.posy)
        self.isjump = False
        self.isshoot = False
        self.iswalk = False
        self.v = 8
        self.m = 2
        self.index = 0
        self.hp = hp
        self.speed = 10
        if bullet == True:
            self.shootMode = True
        else:
            self.shootMode = False
        self.score = score
        self.isup = False
        self.delay = 0

    def update(self, x=0, y=0): #주인공 위치이동함수
        self.posx +=x
        self.posy +=y
        self.rect.move_ip(x, y)
        if self.isjump:
            F = (1/2) *self.m*(self.v**2)
            self.rect.move_ip(0, -F)
            self.posy -= F
            self.v -= 1
            if self.v<0:
                self.m = -2
            if self.v == -9:
                self.isjump = False
                self.v, self.m = 8,2

    def motion(self,option = 0): #주인공 행동모션함수
        walk_image = ['resources/images/movement/walk/1.gif', 'resources/images/movement/walk/2.gif','resources/images/movement/walk/3.gif', 'resources/images/movement/walk/4.gif',
                      'resources/images/movement/walk/5.gif','resources/images/movement/walk/6.gif', 'resources/images/movement/walk/7.gif',
                      'resources/images/movement/walk/8.gif', 'resources/images/movement/walk/9.gif','resources/images/movement/walk/10.gif', 'resources/images/movement/walk/11.gif']
        if self.shootMode == False:
            shoot_image_stand = ['resources/images/movement/shoot/1.png','resources/images/movement/shoot/2.png','resources/images/movement/shoot/3.png']
            shoot_image_walk = ['resources/images/movement/shoot/walk2/1.png','resources/images/movement/shoot/walk2/2.png','resources/images/movement/shoot/walk2/3.png','resources/images/movement/shoot/walk2/4.png',
                                'resources/images/movement/shoot/walk2/5.png','resources/images/movement/shoot/walk2/6.png','resources/images/movement/shoot/walk2/7.png','resources/images/movement/shoot/walk2/8.png',
                                'resources/images/movement/shoot/walk2/9.png']
            shoot_up = ['resources/images/movement/shoot/walk_up/1.gif','resources/images/movement/shoot/walk_up/2.gif','resources/images/movement/shoot/walk_up/3.gif','resources/images/movement/shoot/walk_up/4.gif',
                        'resources/images/movement/shoot/walk_up/5.gif','resources/images/movement/shoot/walk_up/6.gif','resources/images/movement/shoot/walk_up/7.gif']
            up_image = ['resources/images/movement/shoot/4.gif','resources/images/movement/shoot/5.gif','resources/images/movement/shoot/6.gif']
            if option == 0 and self.isshoot != True:
                if self.isjump == False:
                    if self.delay % 2 == 0:
                        self.index += 1
                    self.delay += 1
                    self.index = self.index%len(walk_image)
                    self.image = pygame.image.load(walk_image[self.index])
                    self.image = pygame.transform.scale(self.image,self.size)
                else:
                    self.image = pygame.image.load(walk_image[3])
                    self.image = pygame.transform.scale(self.image,self.size)
            elif option == 2:
                if self.iswalk == True:
                    self.index = (self.index+1) % len(shoot_image_walk)
                    self.image = pygame.image.load(shoot_image_walk[self.index])
                else:
                    self.index = (self.index+1)%len(shoot_image_stand)
                    self.image = pygame.image.load(shoot_image_stand[self.index])
                size = self.imagesize(self.image)
                self.image = pygame.transform.scale(self.image, size)
            elif option == 1:
                self.image = pygame.image.load(walk_image[0])
                self.image = pygame.transform.scale(self.image,self.size)
            elif option == 3:
                if self.isshoot == True and self.iswalk == True:
                    self.index = (self.index + 1) % len(shoot_up)
                    self.image = pygame.image.load(shoot_up[self.index])
                    self.image = pygame.transform.scale(self.image, self.size)
                elif self.isshoot == True:
                    self.index = (self.index + 1) % len(up_image)
                    self.image = pygame.image.load(up_image[self.index])
                    self.image = pygame.transform.scale(self.image, self.size)
                else:
                    self.image = pygame.image.load('resources/images/movement/shoot/13.gif')
                    self.image = pygame.transform.scale(self.image, self.size)
        else:
            shoot_image_stand = ['resources/images/movement/shoot/7.png','resources/images/movement/shoot/8.png']
            shoot_image_walk = ['resources/images/movement/shoot/walk1/1.png','resources/images/movement/shoot/walk1/2.png','resources/images/movement/shoot/walk1/3.png','resources/images/movement/shoot/walk1/4.png',
                                'resources/images/movement/shoot/walk1/5.png','resources/images/movement/shoot/walk1/6.png','resources/images/movement/shoot/walk1/7.png','resources/images/movement/shoot/walk1/8.png']
            shoot_up = ['resources/images/movement/shoot/walk_up2/1.png','resources/images/movement/shoot/walk_up2/2.png','resources/images/movement/shoot/walk_up2/3.png','resources/images/movement/shoot/walk_up2/4.png',
                        'resources/images/movement/shoot/walk_up2/5.png','resources/images/movement/shoot/walk_up2/6.png','resources/images/movement/shoot/walk_up2/7.png']
            up_image = ['resources/images/movement/shoot/9.gif','resources/images/movement/shoot/10.gif','resources/images/movement/shoot/11.gif','resources/images/movement/shoot/12.gif']
            if option == 0 and self.isshoot != True:
                if self.isjump == False:
                    if self.delay % 2 == 0:
                        self.index += 1
                    self.delay += 1
                    self.index = self.index%len(walk_image)
                    self.image = pygame.image.load(walk_image[self.index])
                    self.image = pygame.transform.scale(self.image,self.size)
                else:
                    self.image = pygame.image.load(walk_image[3])
                    self.image = pygame.transform.scale(self.image,self.size)
            elif option == 2:
                if self.iswalk == True:
                    self.index = (self.index+1) % len(shoot_image_walk)
                    self.image = pygame.image.load(shoot_image_walk[self.index])
                else:
                    self.index = (self.index+1)%len(shoot_image_stand)
                    self.image = pygame.image.load(shoot_image_stand[self.index])
                size = self.imagesize(self.image)
                self.image = pygame.transform.scale(self.image, size)
            elif option == 1:
                self.image = pygame.image.load(walk_image[0])
                self.image = pygame.transform.scale(self.image,self.size)
            elif option == 3:
                if self.isshoot == True and self.iswalk == True:
                    self.index = (self.index + 1) % len(shoot_up)
                    self.image = pygame.image.load(shoot_up[self.index])
                    size = self.imagesize(self.image)
                    self.image = pygame.transform.scale(self.image, size)
                elif self.isshoot == True:
                    self.index = (self.index + 1) % len(up_image)
                    self.image = pygame.image.load(up_image[self.index])
                    self.image = pygame.transform.scale(self.image, self.size)
                else:
                    self.image = pygame.image.load('resources/images/movement/shoot/9.gif')
                    self.image = pygame.transform.scale(self.image, self.size)

    def imagesize(self, change_img): #주인공 이미지 바뀔때 사이즈조정함수
        change_size = change_img.get_size()
        ratio = self.size[0] / self.org_size[0]
        return (int(change_size[0]*ratio), self.size[1])

    def hit(self, all_sprites, items, enemy_bullets): #주인공 다른객체와 충돌시 충돌객체 없애는 함수
        hits = pygame.sprite.spritecollide(self, items, True)
        if hits:
            if hits[0].itemno == 0:
                self.shootMode = True
            elif hits[0].itemno ==1:
                if self.hp<10:
                    self.hp += 1
            elif hits[0].itemno ==2:
                self.score += 5
            elif hits[0].itemno ==3:
                self.score += 10
            items.remove(hits[0])
            all_sprites.remove(hits[0])
        hits = pygame.sprite.spritecollide(self, enemy_bullets, False)
        if hits:
            self.hp -= 1
            all_sprites.remove(hits[0])
            enemy_bullets.remove(hits[0])
            # print(self.hp)
            return True
    
    def shoot(self, screen, all_sprites, bullets): #주인공 총발사시 총알궤적 함수
        gun = bullet()
        marco_shoot(0.3)
        if self.shootMode == True:
            gun.gun_change()
        if self.isup == True:
            gun.isup = True
            gun.change_dir()
            gun.posx = self.posx + 30
            gun.posy = self.posy
        else:
            gun.posx = self.posx + self.size[0]
            gun.posy = self.posy + 150
        # print(self.posx, gun.posx)
        gun.rect.move_ip(gun.posx, gun.posy)
        all_sprites.add(gun)
        bullets.add(gun)

    # def islive(self):
    #     if self.hp == 0:
    #         marco_die(0.3)
    #         return 0
    #     return 1




class bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(bullet, self).__init__()
        self.image = pygame.image.load('resources/images/bullet/bullet3.png')
        self.size = (100,20)
        self.image = pygame.transform.scale(self.image,self.size)
        self.posx = 0
        self.posy = 0
        self.damage = 0.5
        self.rect = pygame.Rect(self.image.get_rect())
        self.speed = 30
        self.isup = False

    def update(self):
        if self.isup == False:
            self.posx += self.speed
            self.rect.move_ip(self.speed,0)
        else:
            self.posy += self.speed
            self.rect.move_ip(0, -self.speed)

    def gun_change(self):
        self.image = pygame.image.load('resources/images/bullet/bullet2.png')
        self.size = (130, 40)
        self.image = pygame.transform.scale(self.image, self.size)
        self.damage = 1
        self.rect = pygame.Rect(self.image.get_rect())
        self.speed = 40

    def change_dir(self):
        if self.speed == 40:
            self.image = pygame.image.load('resources/images/bullet/bullet8.png')
            self.size = (40, 130)
            self.speed = 40
        else:
            self.image = pygame.image.load('resources/images/bullet/bullet7.png')
            self.size = (20, 100)
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = pygame.Rect(self.image.get_rect())