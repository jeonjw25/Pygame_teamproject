import pygame, enemy

class item(pygame.sprite.Sprite):
    def __init__(self):
        super(item, self).__init__()
        self.image = pygame.image.load('resources/images/items/item4.png')
        self.size = (30,30)
        self.image = pygame.transform.scale(self.image,self.size)
        self.rect = pygame.Rect(self.image.get_rect())
        self.centerx = enemy.soldier().centerx
        self.centery = enemy.soldier().centery


    def appear(self, screen):
        if enemy.soldier().islive == True:
            self.rect = pygame.Rect((self.centerx, self.centery),(self.centerx+self.size[0], self.centery+self.size[1]))
            screen.blit(self.image, self.rect)
            


