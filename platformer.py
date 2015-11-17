"""
platformer.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

darkblue= Color(0x0000CD, 1.0)
black= Color(0x000000, 1.0)

thinline = LineStyle(1, black)
noline= LineStyle(0, black)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

class Block(Sprite):
    block= RectangleAsset(125, 65, noline, darkblue)
    def __init__(self, xval, yval):
        super().__init__(Block.block, (xval, yval))
        self.x = xval
        self.y = yval

ocean= Color(0x87CEFA, 0.75)

black = Color(0, 1)
noline = LineStyle(0, black)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, ocean)
bg = Sprite(bg_asset, (0,0))
      
Block(55, 250)
Block(300, 250)

class Platformer(Sprite):
    """
    Animated space ship
    """
    #asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        #Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(Platformer.asset, position)
        self.vx = 1
        self.vy = 1
        self.vr = 0.01
        self.thrust = 0
        self.thrustframe = 1
        Platformer.listenKeyEvent("keydown", "space", self.thrustOn)
        Platformer.listenKeyEvent("keyup", "space", self.thrustOff)
        self.fxcenter = self.fycenter = 0.5

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)

    def thrustOn(self, event):
        self.thrust = 1

    def thrustOff(self, event):
        self.thrust = 0

class Platformer(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        
myapp= Platformer(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()