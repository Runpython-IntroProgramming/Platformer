"""
platformer.py
Author: 
Credit: 
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
import pygame as pg

blue = Color(0x2EFEC8, 1.0)
black = Color(0x000000, 1.0)
pink = Color(0xFF00FF, 1.0)
red = Color(0xFF5733, 1.0)
white = Color(0xFFFFFF, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
grey = Color(0xC0C0C0, 1.0)

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
        pygame.mixer.init()
        self.screen=pygame.set_mode(WIDTH,HEIGHT))
        self.running=True
    def new(self):
        self.all_sprites=pg.sprite.Group()
        self.player=P1()
        self.all_sprites.add(self.player)
        self.run()
    def run(self):
        self.events()
        self.update()
        self.draw()
    def update(self):
        self.all_sprites.update()
    def events(self):
        if event.type==pg.QUIT:
            running=False
    def draw(self):
        screen.fill(white)
        all_sprites.draw(screen)
        pg.display.flip()
        
g=Platformer()


