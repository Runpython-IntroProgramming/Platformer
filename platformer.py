"""
platformer.py
Author: Anoushka Alavilli
Credit: <list sources used, if any>
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

darkblue= Color(0x0000CD, 1.0)
black= Color(0x000000, 1.0)
turquoise= Color(0x58FAD0, 1.0)

thinline = LineStyle(3, turquoise)
noline= LineStyle(0, black)


SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800

class Block(Sprite):
    block= RectangleAsset(80, 65, thinline, darkblue)
    def __init__(self, xval, yval):
        super().__init__(Block.block, (xval, yval))
        self.x = xval
        self.y = yval

ocean= Color(0x87CEFA, 0.75)

black = Color(0, 1)
noline = LineStyle(0, black)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, ocean)
bg = Sprite(bg_asset, (0,0))

def classblock(event):
    Block(event.x-45, event.y-40)
      
#Block(55, 250)
#Block(300, 250)


class Platformer(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        
myapp= Platformer(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenMouseEvent('click', classblock)
myapp.run()