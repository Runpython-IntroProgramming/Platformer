"""
platformer.py
Author: 
Credit: 
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
import pygame as pg

class Platformer:
    def __init(self):
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
        pass
    def events(self):
        if event.type==pg.QUIT:
            running=False
    def draw(self):
        pass
        
g=Platformer()


