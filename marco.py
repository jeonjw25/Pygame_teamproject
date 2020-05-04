import pygame

class rossi(pygame.sprite.Sprite):
    def __init__(self):
        super(rossi, self).__init__()
        self.image = pygame.image.load('resources/images/marco/marco1.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.size = 120
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
        self.posx = 50
        self.posy = 500
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.move_ip(self.posx,self.posy)
        self.isjump = False
        self.isshoot = False
        self.v = 8
        self.m = 2
        self.index = 0
        self.hp = 5
        self.speed = 10
        self.shootMode = False
        self.score = 0
        self.isup = False

    def update(self, x=0, y=0):
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

    def motion(self,option = 0):
        walk_image = ['resources/images/marco/marco2.png','resources/images/marco/marco3.png','resources/images/marco/marco4.png','resources/images/marco/marco5.png','resources/images/marco/marco6.png',
                            'resources/images/marco/marco7.png','resources/images/marco/marco8.png','resources/images/marco/marco2.png']
        shoot_image = ['resources/images/marco/marco11.png','resources/images/marco/marco9.png','resources/images/marco/marco10.png']                 
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
        elif option == 3:
            self.image = pygame.image.load('resources/images/marco/marco13.gif')
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
        elif option == 2:
            self.index = (self.index+1)%len(shoot_image)
            self.image = pygame.image.load(shoot_image[self.index])
            self.image = pygame.transform.scale(self.image,(self.size,self.size))

    def hit(self, all_sprites, items, enemy_bullets):
        hits = pygame.sprite.spritecollide(self, items, True)
        if hits:
            if hits[0].itemno == 0:
                self.shootMode = True
            elif hits[0].itemno ==1:
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
            print(self.hp)
            return True
    
    def shoot(self, screen, all_sprites, bullets):
        gun = bullet()
        if self.shootMode == True:
            gun.gun_change()
        if self.isup == True:
            gun.isup = True
            gun.change_dir()
            gun.posx = self.posx + 50
            gun.posy = self.posy
        else:
            gun.posx = self.posx + 50
            gun.posy = self.posy + 130
        print(self.posx, gun.posx)
        gun.rect.move_ip(gun.posx, gun.posy)
        all_sprites.add(gun)
        bullets.add(gun)

    def islive(self):
        if self.hp == 0:
            return 0
        return 1




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