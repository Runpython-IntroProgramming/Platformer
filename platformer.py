"""
platformer.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame

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

    def buildBlock(event):
        event.x = event.x - event.x%40
        event.y = event.y - event.y%40
        Block(event.x-10, event.y-10)
        

black = Color(0, 1)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, black)
bg = Sprite(bg_asset, (0,0))


class SSprite(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(227,0,292-227,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(SSprite.asset, position)
        
SSprite((100, 100))
        


class Platformer(App):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        self.mousex = 0
        self.mousey = 0
        self.listenMouseEvent('mousemove', 

myapp = Platformer(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenMouseEvent('click', buildBlock)
myapp.run()