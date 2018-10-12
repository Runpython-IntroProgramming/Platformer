"""
platformer.py
Author: Meg
Credit: http://brythonserver.github.io/ggame/#ggame.Sprite.collidingWithSprites
Noah
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
teal = Color(0x9fffff, .9)
coral = Color(0xff9e88, 1.0)

thinline = LineStyle(2, black)
blkline = LineStyle(1, black)
noline = LineStyle(0, white)
coolline = LineStyle(1, grey)
blueline = LineStyle(2, blue)
redline = LineStyle(1, red)
greenline = LineStyle(1, green)
gridline = LineStyle(1, grey)
grid=RectangleAsset(30,30,gridline,white)

class Wall(Sprite):
    """
    Create Wall
    """
    asset = RectangleAsset(30,30,gridline,white)

    def __init__(self, position):
        super().__init__(Wall.asset, position)


class Player(Sprite):
    """
    Create Player
    """
    asset = RectangleAsset(15,30,gridline,teal)

    def __init__(self, position):
        super().__init__(Player.asset, position)

        
class Spring(Sprite):
    """
    Create Spring
    """
    asset = RectangleAsset(15,5,gridline,coral)

    def __init__(self, position):
        super().__init__(Spring.asset, position)
        
class Platform(App):
    """
    Tutorial4 space game example.
    """
    
    def __init__(self):
        super().__init__()
        # Backgroundw
        bg_asset = RectangleAsset(self.width, self.height, noline, grey)
        bg = Sprite(bg_asset, (0,0))
        Platform.listenKeyEvent("keydown", "w", self.wallMaker)
        Platform.listenKeyEvent("keydown", "p", self.playerMaker)
        Platform.listenKeyEvent("keydown", "s", self.springMaker)
        self.asset = [0,0]
        Platform.listenMouseEvent('mousemove', self.mouseMove)
        
    # Handle the mouse click
    def mouseMove(self, event):
        self.asset[0] = event.x
        self.asset[1] = event.y

    def wallMaker(self, event):
        Wall((30*floor((self.asset[0])/30),30*floor((self.asset[1])/30)))
        
    def playerMaker(self, event):
        Player((self.asset[0],self.asset[1]))
    def springMaker(self, event):
        Spring((self.asset[0],self.asset[1]))

myapp = Platform()
myapp.run()


