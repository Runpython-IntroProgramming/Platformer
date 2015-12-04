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
coolline = LineStyle(2, blue)

class Block(Sprite):
    block = RectangleAsset(40, 40, thinline, blue)
    def __init__(self, xval, yval):
        super().__init__(Block.block, (xval, yval))
        self.x = xval
        self.y = yval


black = Color(0, 1)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, black)
bg = Sprite(bg_asset, (0,0))


class SSprite(Sprite):
    dog = RectangleAsset(30, 30, coolline, pink)
    def __init__(self, x, y):
        super().__init__(SSprite.dog, (x, y))
        self.x = x
        self.y = y
        
gravity = 0

class Platformer(App):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        self.mousex = 0
        self.mousey = 0
        self.dog = 0
        self.dogsprite = None
        self.listenKeyEvent('keydown', 'p', self.buildDog)
        self.listenKeyEvent('keydown', 'w', self.buildBlock)
        self.listenMouseEvent('mousemove', self.motion)
        self.listenKeyEvent('keydown', 'right arrow', self.moveDogR)
        self.listenKeyEvent('keydown', 'left arrow', self.moveDogL)
        self.listenKeyEvent('keydown', 'up arrow', self.moveDogU)
        self.listenKeyEvent('keydown', 'down arrow', self.moveDogD)
    
    def motion(self, event):
        self.mousex = event.x
        self.mousey = event.y
    
    def buildDog (self, event):
        if self.dogsprite:
            self.dogsprite.destroy()
        self.dogsprite = SSprite(self.mousex - 15, self.mousey - 15)
        gravity = 0
    
    def buildBlock(self, event):
        x = self.mousex - self.mousex%40
        y = self.mousey - self.mousey%40
        Block(x-10, y-10)
        
    def moveDogR(self, event):
        self.dogsprite.x += 5
        collisions = self.dogsprite.collidingWithSprites(Block)
        if collisions:
            self.dogsprite.x -= 5
            
    def moveDogL(self, event):
        self.dogsprite.x -= 5
        collisions = self.dogsprite.collidingWithSprites(Block)
        if collisions:
            self.dogsprite.x += 5
            
    def moveDogU(self, event):
        self.dogsprite.y -= 50
        collisions = self.dogsprite.collidingWithSprites(Block)
        if collisions:
            self.dogsprite.y += 50

    def moveDogD(self, event):
        self.dogsprite.y += 5
        collisions = self.dogsprite.collidingWithSprites(Block)
        if collisions:
            self.dogsprite.y -= 5
            
    def step(self):
        #pass
        if self.dogsprite:
            self.dogsprite.y += gravity
            gravity += 0.2
            
        
        
        
        
myapp = Platformer(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()