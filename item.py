import pygame
import random

class ITEM(pygame.sprite.Sprite):
    def __init__(self):
        super(ITEM, self).__init__()
        self.itemno = random.choices(range(0,4), weights=[1,2,5,3])[0]
        print(self.itemno)
        img = ['resources/images/items/item4.png','resources/images/items/item1.png','resources/images/items/item2.png','resources/images/items/item3.png']
        print(self.itemno)
        self.image = pygame.image.load(img[self.itemno])
        self.size = (60,60)
        self.image = pygame.transform.scale(self.image,self.size)
        self.rect = pygame.Rect(self.image.get_rect())
        self.posx = 0
        self.posy = 0

    def update(self, x=0, y=0):
        self.posx += x
        self.posy += y
        self.rect.move_ip(x, y)

    def draw(self, screen):
        self.rect = pygame.Rect((self.posx, self.posy),self.size)
        screen.blit(self.image, self.rect)


            


