"""
platformer.py
Author: 
Credit: 
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
from math import floor

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

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
grid = RectangleAsset(40,40,gridline,white)

class Block(Sprite):
    def __init__(self, position):
        box = RectangleAsset(40,40, cooline, red)
        x-=x%w
        y-=y%w
        super().__init__(box, (x,y))


class Falling(Sprite):
    def __init__(self,x,y,w,h,COLOR,app):
        self.vx=0
        self.vy=0
        self.stuck=False
        self.resting=False
        BOX=RectangleAsset(w,h,thinline,COLOR)
        super().__init__(BOX,(x, y)) 
    def step(self):
        self.x=+self.vx
        collision=self.collidingWithSprites(Block)
        for i in collision:
            if self.vx>0 or self.vx<0:
                if self.vx<0:
                    self.x=i.x+i.w+1
                else:
                    self.x=i.x-self.w-1
                self.vx=0
        self.y=+self.vy
        collision1=self.collidingWithSprites(Block)
        for i in collision:
            if self.vx>0 or self.vx<0:
                if self.vx<0:
                    self.x=i.x+i.w+1
                else:
                    self.x=i.x-self.w-1
                self.vx=0



