import pygame
import enemy

class item(pygame.sprite.Sprite):
    def __init__(self):
        super(item, self).__init__()
        self.size = (100, 20)
        self.image = pygame.image.load("resources/images/items/item4.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = pygame.Rect(self.image.get_rect())
        self.centerx = enemy.soldier().centerx
        self.centery = enemy.soldier().centery

    def update(self):
        if enemy.soldier().islive = False:
            