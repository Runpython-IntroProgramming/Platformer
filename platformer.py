"""
platformer.py
Author: Matthew F
Credit: Robbie
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
        Platformer.listenKeyEvent("keydown", "s", self.SPRING)
        Platformer.listenKeyEvent("keyup", "s", self.SPRINGoff)
            
        Platformer.listenKeyEvent("keydown", "w", self.WALL)
        Platformer.listenKeyEvent("keyup", "w", self.WALLoff)
"""

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640

class Wall(Sprite):
    """
    THIS IS BOXY'S WALL
    """
    black = Color(0, 1)
    noline = LineStyle(0, black)
    asset = RectangleAsset(25, 25, noline, black)
    
    def __init__(self, position):
        super().__init__(Wall.asset, position)
        self.vx = 0
        self.vy = 0
        self.fxcenter = self.fycenter = 0.25

class Boxy(Sprite):
    """
    THIS IS BOXY
    """
    Black = Color(0, 1)
    oline = LineStyle(0, Black)
    blue = Color(0x0000ff, 1.0)
    asset = RectangleAsset(25, 50, oline, blue)
    
    def __init__(self, position):
        super().__init__(Boxy.asset, position)
        self.vx = 0
        self.vy = 0
        self.bricks = self.collidingWithSprites(Wall)
        self.fxcenter = self.fycenter = 0.25
        Platformer.listenKeyEvent("keydown", "right arrow", self.moveright)
        Platformer.listenKeyEvent("keyup", "right arrow", self.moveoff)
        Platformer.listenKeyEvent("keydown", "left arrow", self.moveleft)
        Platformer.listenKeyEvent("keyup", "left arrow", self.moveoff)
        Platformer.listenKeyEvent("keydown", "up arrow", self.moveup)
        Platformer.listenKeyEvent("keyup", "up arrow", self.moveoff)
        Platformer.listenKeyEvent("keydown", "down arrow", self.movedown)
        Platformer.listenKeyEvent("keyup", "down arrow", self.moveoff)        
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        bricks =self.collidingWithSprites(Wall)
        if len(bricks) != 0:
            self.vx = self.vy = 0
    
    def moveoff(self,event):
        self.vx = self.vy = 0
    def moveright(self, event):
        self.vx = 2.5 
    def moveleft(self,event):
        self.vx = -2.5
    def moveup(self,event):
        self.vy = -2.5
    def movedown(self,event):
        self.bricks == 0
        self.vy = 2.5
class Platformer(App):
    """
    THIS IS BOXY'S WORLD
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(1, 0)
        Black = Color(0, 1)
        Blue = Color(0x0000ff, 1.0)
        noline = LineStyle(5, Black)
        Noline = LineStyle(0, Black)
        bg_asset = RectangleAsset(width, height, noline, black)
        Platformer.listenKeyEvent("keydown", "w", self.Wall)
        Platformer.listenKeyEvent("keydown", "p", self.Boxy)
        Platformer.listenMouseEvent('mousemove', self.mousemove)
        self.Robbie = False
        bg = Sprite(bg_asset, (0,0))
        self.x = 0
        self.y = 0
        
    def step(self):
        for ship in self.getSpritesbyClass(Boxy):
            ship.step()
    def mousemove(self, event):
        self.x = event.x
        self.y = event.y 
        
    def Wall(self, event):
        Wall((self.x, self.y))
    def Boxy(self, event):
        if self.Robbie == False:
            Boxy((self.x, self.y))
            self.Robbie = True
    
        

myapp = Platformer(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
