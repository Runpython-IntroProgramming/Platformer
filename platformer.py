"""
platformer.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

SCREEN_WIDTH = 10000
SCREEN_HEIGHT = 10000

blue = Color(0x2EFEC8, 1.0)
black = Color(0x000000, 1.0)
pink = Color(0xFF00FF, 1.0)

thinline = LineStyle(2, pink)
noline = LineStyle(0, blue)

class Block(Sprite):
    block = RectangleAsset(40, 40, thinline, blue)
    def __init__(self, xval, yval):
        super().__init__(Block.block, (xval, yval))
        self.x = xval
        self.y = yval

black = Color(0, 1)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, black)
bg = Sprite(bg_asset, (0,0))

def buildBlock(event):
    event.x = event.x - event.x%40
    event.y = event.y - event.y%40
    Block(event.x-10, event.y-10)

class Platformer(App):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()

myapp = Platformer(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenMouseEvent('click', buildBlock)
myapp.run()