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
FPS=30

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
pink=(255,0,255)
lblue=(0,255,255)

thinline = LineStyle(2, black)
blkline = LineStyle(1, black)
noline = LineStyle(0, white)
coolline = LineStyle(1, grey)
blueline = LineStyle(2, blue)
redline = LineStyle(1, red)
greenline = LineStyle(1, green)
gridline = LineStyle(1, grey)
grid=RectangleAsset(30,30,gridline,white)

class Platformer:
    def __init__(self):
        pygame.init()
        self.screen=pygame.set_mode(WIDTH,HEIGHT))
        self.clock=pygame.time.Clock()
        self.running=True
    def new(self):
        self.all_sprites=pygame.sprite.Group()
        self.P1=Player()
        self.all_sprites.add(self.P1)
        self.run()
    def run(self):
        self.playing=True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    def update(self):
        self.all_sprites.update()
    def events(self):
        for i in pygame.event.get():
            if event.type==pygame.QUIT:
                if self.playing:
                    self.playing=False
                self.running=False
    def draw(self):
        screen.fill(white)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
    def ssc(self):
        pass
    def esc(self):
        pass
p=Platformer()



