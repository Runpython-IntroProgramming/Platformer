"""
platformer.py
Author: 
Credit: 
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
import pygame

WIDTH=1600
HEIGHT=800
FPS=60

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
pink=(255,0,255)
lblue=(0,255,255)


class User(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((20,40))
        self.image.fill(lblue)
        self.rect=self.image.get_rect()
        self.vex=0
        self.vey=0
        self.rect.center=(WIDTH/2,HEIGHT/2)
    def update(self):
        self.vex=0
        arrows=pygame.key.get_pressed()
        if arrows[pygame.K_LEFT]:
            self.vex=-15
        if arrows[pygame.K_RIGHT]:
            self.vex=15
        self.rect.x +=self.vex
        self.rect.y +=self.vey


class Platformer:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock=pygame.time.Clock()
        self.running=True
    def new(self):
        self.asp=pygame.sprite.Group()
        self.player= User()
        self.asp.add(self.player)
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
    def events(self):
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
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


