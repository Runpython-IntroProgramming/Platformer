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

class Springo(Sprite):
    """
    THIS IS BOXY'S SPRING
    """
    plurple = Color(0xff33ff, 1)
    noline = LineStyle(0, plurple)
    asset = RectangleAsset(25,5, noline, plurple)
    
    
    def __init__(self, position):
        super().__init__(Springo.asset, position)
        self.vx = 0
        self.vy = 5
        self.fxcenter = self.fycenter = 0.25
        bricks = self.collidingWithSprites(Wall)
        Platformer.listenKeyEvent("keyup","s", self.Falling)
        self.Matty = True
   
    def step(self):
        self.vy = self.vy + 1.25
        self.y += self.vy
        bricks = self.collidingWithSprites(Wall)
        if len(bricks) != 0:
            self.y -= self.vy
            self.vy = 0
            self.Matty = False
        else: 
            self.Matty = True
        self.x += self.vx
        bricks = self.collidingWithSprites(Wall)
        if len(bricks) != 0:
            self.x -= self.vx
            self.vx = 0
            self.Matty = False
        else:
            self.Matty = True
        
    def Falling(self,event):
        if self.Matty == True:
            self.vy = self.vy + 1    

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
        self.vy = 5
        self.bricks = self.collidingWithSprites(Wall)
        self.fxcenter = self.fycenter = 0.25
        self.Matty = True
        self.DonFluffles = False
        Platformer.listenKeyEvent("keydown", "right arrow", self.moveright)
        Platformer.listenKeyEvent("keyup", "right arrow", self.moveoff)
        Platformer.listenKeyEvent("keydown", "left arrow", self.moveleft)
        Platformer.listenKeyEvent("keyup", "left arrow", self.moveoff)
        Platformer.listenKeyEvent("keydown", "up arrow", self.moveup)
        Platformer.listenKeyEvent("keyup", "up arrow", self.moveoff)
        Platformer.listenKeyEvent("keydown", "right arrow", self.Falling)
        Platformer.listenKeyEvent("keydown", "left arrow", self.Falling)
        
        
    def step(self):
        self.vy = self.vy + 1.25
        self.y += self.vy
        bricks = self.collidingWithSprites(Wall)
        if len(bricks) != 0:
            self.y -= self.vy
            self.vy = 0
            self.Matty = False
        else:
            self.Matty = True
        if self.Matty == True:
            self.DonFluffles = True
        else:
            self.DonFluffles = False
        
        self.x += self.vx
        bricks = self.collidingWithSprites(Wall)
        if len(bricks) != 0:
            self.x -= self.vx
            self.vx = 0
            self.Matty = False
        else:
            self.Matty = True
            
    def Falling(self,event):
        if self.Matty == True:
            self.vy = self.vy + 1
    
    def moveoff(self,event):
            self.vx = 0
            self.vy = self.vy + 1
        
    def moveright(self, event):
        if len(self.bricks) == 0:
            self.Matty = True
        if self.Matty == True:
            self.vx = 5
        else:
            self.vx = 5
            self.vy = 5
            
    def moveleft(self,event):
        if len(self.bricks) == 0:
            self.Matty = True
        if self.Matty == True:
            self.vx = -5
        else:
            self.vx = -5
            self.vy = 5
            
    def moveup(self,event):
        if len(self.bricks) == 0:
            self.Matty = True
        if self.DonFluffles == False:
            if self.Matty == True:
                self.vy = -15
        else:
            self.vy = 5
            
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
        Platformer.listenKeyEvent("keydown", "s", self.Springo)
        Platformer.listenMouseEvent('mousemove', self.mousemove)
        self.Robbie = False
        bg = Sprite(bg_asset, (0,0))
        self.x = 0
        self.y = 0
        
    def step(self):
        for ship in self.getSpritesbyClass(Boxy):
            ship.step()
    def stoop(self):
        for hip in self.getSpritesbyClass(Springo):
            hip.step()
    def mousemove(self, event):
        self.x = event.x
        self.y = event.y 
        
    def Wall(self, event):
        self.x = round(self.x/25)
        self.y = round(self.y/25)
        self.x = self.x*25
        self.y = self.y*25
        Wall((self.x, self.y))
    
    def Springo(self, event):
        self.x = round(self.x/25)
        self.y = round(self.y/25)
        self.x = self.x*25
        self.y = self.y*25
        Springo((self.x, self.y))
        
    def Boxy(self, event):
        if self.Robbie == False:
            Boxy((self.x, self.y))
            self.Robbie = True
    
        

myapp = Platformer(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
