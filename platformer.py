"""
platformer.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

blue = Color(0x2EFEC8, 1.0)
black = Color(0x000000, 1.0)

thinline = LineStyle(1, blue)
noline = LineStyle(0, blue)

class Block(Sprite):
    block = RectangleAsset(100, 25, thinline, blue)
    def __init__(self, xval, yval):
        super().__init__(Block.block, (xval, yval))
        self.x = xval
        self.y = yval

Block(100,400)

class Platformer(App):
    def __init__(self):
        super().__init__()

myapp = Platformer()
myapp.run()