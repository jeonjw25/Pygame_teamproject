import pygame
import enemy


class stage1: #스테이지 
    def __init__(self):
        self.w1, self.h1, self.w2, self.h2 = 0, 0, 1000, 736
        self.rect = pygame.Rect(((self.w1,self.h1),(self.w2,self.h2)))
        self.image = pygame.image.load("resources/images/map2.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(3072,736))
        self.speed = 10 #map 이동속도
    
    def draw(self, screen): #스테이지 화면에 출력
        self.rect = pygame.Rect(((self.w1,self.h1),(self.w2,self.h2)))
        screen.blit(self.image,self.rect)

    def generation_soldier(self, all_sprites, enemys): #적생성
        gen_position = [(-500,500), (-850,265) ,(-1000,500) ,(-1700,500)]
        for i in gen_position:
            if self.w1 == i[0]:
                enm = enemy.soldier()
                enm.gen(i[1])
                all_sprites.add(enm)
                enemys.add(enm)

    def generation_movesoldier(self, all_sprites, enemys): #이동하는 적생성
        gen_position = [(-400,500),(-800,500), (-1200,500) ,(-1600,500)]
        for i in gen_position:
            if self.w1 == i[0]:
                enm = enemy.soldier()
                enm.iswalk = True
                enm.gen(i[1])
                all_sprites.add(enm)
                enemys.add(enm)

    def generation_shootsoldier(self, all_sprites, enemys,enemy_bullets): #적 총알 생성
        gen_position = [(-1400,500),(-1800,257)]
        for i in gen_position:
            if self.w1 == i[0]:
                enm = enemy.soldier()
                enm.isshoot = True
                enm.gen(i[1])
                all_sprites.add(enm)
                enemys.add(enm)
                enm.shoot(all_sprites, enemy_bullets)

    def generation_ufo(self, all_sprites, enemys, enemy_bullets): #ufo적 생성
        gen_position = [(-1000, 100), (-1500, 120),(-2000, 110)]
        for i in gen_position:
            if self.w1 == i[0]:
                enm = enemy.UFO()
                enm.gen(i[1])
                all_sprites.add(enm)
                enemys.add(enm)
                enm.shoot(all_sprites, enemy_bullets)

    def move(self, player): #주인공 위치에 따른 화면조정
        if player.posx >= 300 and self.w2 < -1000:
            if player.posx > 1000:
                return -1
            return self.speed
        elif player.posx >= 300:
            self.w1 -= player.speed
            self.w2 -= player.speed
            return 0
        else:
            return self.speed

    def end(self):
        pass

class boss_stage(): #보스스테이지 클래스
    def __init__(self):
        self.image = pygame.image.load("resources/images/boss/bossmap.png")
        self.w1, self.h1, self.w2, self.h2 = -150, -0, 1000, 657
        self.rect = pygame.Rect(((self.w1,self.h1),(self.w2,self.h2)))
        self.image = pygame.transform.scale(self.image, (1344, 736))
        self.speed = 10
        self.bossmon = enemy.boss()
    
    def draw(self,screen): #보스 화면에 출력
        self.rect = pygame.Rect(((self.w1, self.h1), (self.w2, self.h2)))
        screen.blit(self.image, self.rect)

    def move(self, player): #보스속도
        return player.speed

    def generation_boss(self, all_sprites, enemys): #보스를 sprites에 추가
        all_sprites.add(self.bossmon)
        enemys.add(self.bossmon)

    def end(self): #보스 죽을때
        if self.bossmon.hp == 0: 
            return 1