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


black = Color(0, 1)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, black)
bg = Sprite(bg_asset, (0,0))


class SSprite(Sprite):
    dog = CircleAsset(10, thinline, pink)
    def __init__(self, x, y):
        super().__init__(SSprite.dog, (x, y))
        self.x = x
        self.y = y
        

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
        #SSprite(self.mousex, self.mousey)
        if self.dogsprite:
            self.dogsprite.destroy()
        self.dogsprite = SSprite(self.mousex, self.mousey)
            #delete first sprite and only keep the last sprite
    
    def buildBlock(self, event):
        x = self.mousex - self.mousex%40
        y = self.mousey - self.mousey%40
        Block(x-10, y-10)
        
    def moveDogR(self, event):
        self.dogsprite.x += 5
        collisions = self.collidingWithSprites()
        if collisions:
            self.dogsprite.x -= 5
            
    def moveDogL(self, event):
        self.dogsprite.x -= 5
        collisions = self.collidingWithSprites()
        if collisions:
            self.dogsprite.x += 5
            
    def moveDogU(self, event):
        self.dogsprite.y -= 5
        collisions = self.collidingWithSprites()
        if collisions:
            self.dogsprite.y += 5
            
    def moveDogD(self, event):
        self.dogsprite.y += 5
        collisions = self.collidingWithSprites()
        if collisions:
            self.dogsprite.y -= 5
        
        
myapp = Platformer(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()

#def collidingWithSprites(self, sclass=None)
#Return a list of sprite objects identified by the sclass parameter 
#that are currently colliding with (that is, with which the collidingWith 
#method returns True) this sprite. If sclass is set to None (default), 
#then all other sprites are checked for collision, otherwise, only sprites 
#whose class matches sclass are checked.