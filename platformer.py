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
        self.vx = 0
        self.vy = 0
        for i in keys:
        platformer.listenKeyEvent("keyup", "up arrow", self.up)
        platformer.listenKeyEvent("keydown", "up arrow", self.down)
        platformer.listenKeyEvent("keyup", "down arrow", self.right)
        platformer.listenKeyEvent("keydown", "down arrow", self.left)
        platformer.listenKeyEvent("keyup", "right arrow", self.down)
        platformer.listenKeyEvent("keydown", "right arrow", self.up)
        platformer.listenKeyEvent("keyup", "left arrow", self.left)
        platformer.listenKeyEvent("keydown", "left arrow", self.right)
        
        
        
'''
myApp = App
myApp.run()
'''











