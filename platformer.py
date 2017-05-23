"""
platformer.py
Author: 
Credit: 
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame

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
grid=RectangleAsset(30,30,gridline,white)


black = Color(0, 1)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, black)
bg = Sprite(bg_asset, (0,0))

class Brick(Sprite):
    brick = RectangleAsset(30, 30, thinline, pink)
    def __init__(self, x, y):
        super().__init__(Brick.brick, (x, y))
        self.x = x
        self.y = y
        
class Guy(Sprite):
    guy = RectangleAsset(20, 20, thinline, green)
    def __init__(self, x, y):
        super().__init__(Guy.guy, (x, y))
        self.x = x
        self.y = y
        
    def step(self):
        self.grav += 0.2
        self.y += self.grav
        collide = self.collidingWithSprites(brick)
        if collide:
            self.y -= self.grav
            self.grav = 0
            
grav=0



myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()