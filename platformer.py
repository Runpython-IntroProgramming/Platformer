"""
platformer.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

turquoise= Color(0x2EFEC8, 1.0)
black= Color(0x000000, 1.0)

thinline = LineStyle(1, black)
noline= LineStyle(0, black)


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Block(Sprite):
    block= RectangleAsset(125, 65, noline, turquoise)
    def __init__(self, xval, yval):
        super().__init__(Block.block, (xval, yval))
        self.x = xval
        self.y = yval
        
Block(55, 250)
Block

class Platformer(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self):
        super().__init__()
        
myapp= Platformer()
myapp.run()