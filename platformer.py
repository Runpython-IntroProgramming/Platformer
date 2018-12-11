"""
platformer.py
Author: 
Credit: 
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
import pygame
import random

WIDTH=800
HEIGHT=600
FPS=60

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
pink=(255,0,255)
lblue=(0,255,255)

vector=pygame.math.Vector2
fric = -0.12
pacc =0.8

class User(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((20,40))
        self.image.fill(lblue)
        self.rect=self.image.get_rect()
        self.rect.center=(WIDTH / 2, HEIGHT / 2)
        self.pos=vector(WIDTH / 2, HEIGHT / 2)
        self.vel=vector(0,0)
        self.acc=vector(0,0)
    def update(self):
        self.acc=vector(0,0.8)
        arrows=pygame.key.get_pressed()
        if arrows[pygame.K_LEFT]:
            self.acc.x= -pacc
        if arrows[pygame.K_RIGHT]:
            self.acc.x= pacc
        self.acc.x += self.vel.x * fric
        self.vel +=self.acc
        self.pos += self.vel + 0.8 * self.acc
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Platformer:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock=pygame.time.Clock()
        self.running=True
    def new(self):
        self.asp=pygame.sprite.Group()
        self.player= User()
        self.Wall=pygame.sprite.Group()
        self.asp.add(self.player)
        b=Wall(0,HEIGHT-40, WIDTH,80)
        self.asp.add(b)
        self.Wall.add(b)
        self.run()
    def run(self):
        self.playing=True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    def update(self):
        self.asp.update()
        collide=pygame.sprite.spritecollide(self.player, self.Wall, False)
        if collide:
            self.player.pos.y=collide[0].rect.top
            self.player.vel.y=0
    def events(self):
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                if self.playing:
                    self.playing=False
            self.running=False
    def draw(self):
        self.screen.fill(white)
        self.asp.draw(self.screen)
        pygame.display.flip()
    def ssc(self):
        pass
    def esc(self):
        pass
p=Platformer()
p.ssc()
while p.running:
    p.new()
    p.esc()
pygame.quit()