import pygame
class stage1:
    def __init__(self):
        self.w1, self.h1, self.w2, self.h2 = 0, 0, 1000, 657
        self.rect = pygame.Rect(((self.w1,self.h1),(self.w2,self.h2)))
        self.image = pygame.image.load("./images/map1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(3510,657))
        self.speed = 10 #map 이동속도
    
    def draw(self, screen):
        self.rect = pygame.Rect(((self.w1,self.h1),(self.w2,self.h2)))
        screen.blit(self.image,self.rect)

    def move(self, centerx):
        if centerx >= 500 and self.w2 < -1500:
            return self.speed
        elif centerx >= 500:
            self.w1 -= 10
            self.w2 -= 10
            return 0
        else:
            return self.speed

    def end(self,centerx):
        if centerx>1000:
            return 1
        return 0


""" def boss_stage():
    def __init__(self):
        self.w1, self.h1, self.w2, self.h2 = 0, 0, 1000, 657
        self.rect = pygame.Rect(((w1,h1),(w2,h2)))
    
    def draw(self):
        screen.blit(self.image,self.rect)

    def move(self, centerx):
        return self.speed

    def end(self):
     """