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
grid = RectangleAsset(30,30,gridline,white)

#keys = ['up arrow', 'down arrow', 'right arrow', 'left arrow']
class Character(Sprite):
    box = RectangleAsset(15, 25, greenline, green)
    def __init__(self, position):
        super().__init__(SpaceShip.ship, position)
        keydown = 0
        self.vx = 0
        self.vy = 0
        platformer.listenKeyEvent("keyup", "up arrow", self.up)
        platformer.listenKeyEvent("keydown", "up arrow", self.stop)
        platformer.listenKeyEvent("keyup", "down arrow", self.right)
        platformer.listenKeyEvent("keydown", "down arrow", self.stop)
        platformer.listenKeyEvent("keyup", "right arrow", self.down)
        platformer.listenKeyEvent("keydown", "right arrow", self.stop)
        platformer.listenKeyEvent("keyup", "left arrow", self.left)
        platformer.listenKeyEvent("keydown", "left arrow", self.stop)
     
    def keycheck(self, event):
        if self.keydown == 0:
            if self.vy != 0:
                if self.vy > 0:
                    self.vy -= 0.2
                else:
                    self.vy += 0.2
            if self.vx != 0:
                if self.vx > 0:
                    self.vx -= 0.2
                else:
                    self.vx += 0.2

    def up(self, event):
        if self.vy < 2:
            self.vy += 0.2
        self.keydown = 1
        print('a')
    def down(self, event):
        if self.vy > -2:
            self.vy -= 0.2
        self.keydown = 1
        print('a')        
    def right(self, event):
        if self.vx < 2:
            self.vx += 0.2
        self.keydown = 1
        print('a')        
    def left(self, event):
        if self.vx > -2:
            self.vx -= 0.2
        self.keydown = 1
        
    def stop(self, event):
        self.keydown = 0
        
class platformer(Sprite):
    global black, white, grey
    def __init__(self):
        super().__init__()
        noline = LineStyle(0, grey)
        bg_asset = RectangleAsset(self.width, self.height, noline, black)
        bg = Sprite(bg_asset, (0,0))






myApp = platformer
myApp.run()












