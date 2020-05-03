import pygame

class soldier(pygame.sprite.Sprite):
    def __init__(self):
        super(soldier, self).__init__()
        self.image = pygame.image.load('resources/images/soldier1.png')
        self.size = 120
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
        self.centerx = 800
        self.centery = 400
        self.rect = pygame.Rect(((self.centerx,self.centery),(self.centerx+self.size,self.centery+self.size)))
        self.mask = pygame.mask.from_surface(self.image)

    def hit(self, all_sprites, bullets, enemy):
        print(self.rect)
        for i in bullets:
            if pygame.sprite.collide_mask(self.mask, i.mask):
                all_sprites.remove(self)

        

        
# class boss(pygame.sprite.Sprite):
#     def __init__(self):
#         super(soldier, self).__init__()
#         self.image = pygame.image.load('resources/images/marco1.png')
#         self.size = 120
#         self.image = pygame.transform.scale(self.image,(self.size,self.size))
#         self.rect = self.image.get_rect()
#         self.centerx = self.rect.centerx
#         self.centery = self.rect.centery

# class arabe(pygame.sprite.Sprite):
#     def __init__(self):
#         super(soldier, self).__init__()
#         self.image = pygame.image.load('resources/images/marco1.png')
#         self.size = 120
#         self.image = pygame.transform.scale(self.image,(self.size,self.size))
#         self.rect = self.image.get_rect()
#         self.centerx = self.rect.centerx
#         self.centery = self.rect.centery

# def enemy_load