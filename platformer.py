"""
platformer.py
Author: Robbie
Credit: Matt
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640

# THIS IS BOXY
class Boxy(Sprite):
    Black=Color(0,1)
    oline= LineStyle(0, Black)
    blue=Color(0x0000ff, 1.0)
    asset= RectangleAsset(25, 50, oline, blue)
    
    def __init__(self, position):
        super().__init__(Boxy.asset, position)
        self.vx = 0
        self.vy = 5
        self.vr = 0
        self.a = self.collidingWithSprites(Wall)
        self.b = self.collidingWithSprites(Spring)
        self.fxcenter = self.fycenter = 0.25
        self.YourDad = True
        self.YourUncle = False
        self.You = False
        self.YourAunt = False
        Platformer.listenKeyEvent("keydown", "right arrow", self.MoveRIGHT)
        Platformer.listenKeyEvent("keyup", "right arrow", self.MoveOff)
        Platformer.listenKeyEvent("keydown", "left arrow", self.MoveLEFT)
        Platformer.listenKeyEvent("keyup", "left arrow", self.MoveOff)
        Platformer.listenKeyEvent("keydown", "up arrow", self.JumpOn)
        Platformer.listenKeyEvent("keyup", "up arrow", self.JumpOff)
        Platformer.listenKeyEvent("keydown", "right arrow", self.falling)
        Platformer.listenKeyEvent("keydown", "left arrow", self.falling)
       

    def step(self):
        self.vy = self.vy + 1.25
        self.y += self.vy
        self.a = self.collidingWithSprites(Wall)
        self.b = self.collidingWithSprites(Spring)
        if len(self.b) != 0:
            self.You = True
        if len(self.a) != 0:
            self.y -= self.vy
            self.vy = 0
            self.YourDad = False
        else:
            self.YourDad = True
        if self.You == True:
            self.vy = -30
            self.You = False
        if self.YourDad == True:
            self.YourUncle = True
        else:
            self.YourUncle = False
        self.x += self.vx
        self.a = self.collidingWithSprites(Wall)
        if len(self.a) != 0:
            self.x -= self.vx
            self.vx = 0
            self.YourDad = False
        else:
            self.YourDad = True

    def falling(self, event):
        if self.YourDad == True:
            self.vy = self.vy + 1 
    
    def MoveRIGHT(self, event):
        if len(self.a) == 0:
            self.YourDad = True
        if self.YourDad == False:
            self.vx = 5
        else:
            self.vx = 5
            self.vy = 5
    
    def MoveLEFT(self, event):
        if len(self.a) == 0:
            self.YourDad = True
        if self.YourDad == False:
            self.vx = -5
        else:
            self.vx = -5
            self.vy = 5
        
    def MoveOff(self, event):
        self.vx = 0
        self.vy = 5

    def JumpOn(self, event):
        if len(self.a) == 0:
            self.YourDad = True
        if self.YourUncle == False:
            if self.YourDad == True:
                self.vy = -15
        else:
            self.vy = 5

    def JumpOff(self, event):
        self. vy = self.vy + 1
        
        # MAKE A WALL
class Wall(Sprite):
    Black = Color(0,1)
    noline = LineStyle(0, Black)
    asset = RectangleAsset(25, 25, noline, Black)
    
    def __init__(self, position):
        super().__init__(Wall.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.fxcenter = self.fycenter = 0

# MAKE DAT SPRUNG


class Spring(Sprite):
    Purple = Color(0xFF33FF, 1)
    noline = LineStyle(0, Purple)
    asset = RectangleAsset(25, 5, noline, Purple)
    
    def __init__ (self, position):
        super().__init__(Spring.asset, position)
        self.vx = 0
        self.vy = 5
        self.YourDad  = True
        self.a = self.collidingWithSprites(Wall)
        self.fxcenter = self.fycenter = .25
        Platformer.listenKeyEvent("keyup" , "s", self.fall)
        
    def step(self):
        self.vy = self.vy + 1.25
        self.y += self.vy
        self.a = self.collidingWithSprites(Wall)
        if len(self.a) != 0:
            self.y -= self.vy
            self.vy = 0
            self.YourDad = False
        else:
            self.YourDad = True
        if self.YourDad == True:
            self.YourUncle = True
        else:
            self.YourUncle = False
        self.x += self.vx
        self.a = self.collidingWithSprites(Wall)
        if len(self.a) != 0:
            self.x -= self.vx
            self.vx = 0
            self.YourDad = False
        else:
            self.YourDad = True
            
    def fall (self, event):
        if self.YourDad == True:
            self.vy = self.vy + 1

        #THIS IS BOXY'S WORLD
class Platformer(App):
    
    def __init__(self, width, height):
        super().__init__(width, height)
        black=Color(1, 0)
        Black=Color(0, 1)
        blue=Color(0x0000ff, 1.0)
        noline=LineStyle(5, Black)
        Noline=LineStyle(0, Black)
        bg_asset=RectangleAsset(width, height, noline, black)
        Platformer.listenKeyEvent("keydown", "w", self.Wall)
        Platformer.listenMouseEvent("mousemove" , self.mousemove)
        Platformer.listenKeyEvent("keydown", "p", self.Box)
        Platformer.listenKeyEvent("keydown", "s", self.Spring)
        bg=Sprite(bg_asset, (0, 0))
        self.x= 0
        self.y = 0
        self.YourMom = False
    
    def step(self):
        for ship in self.getSpritesbyClass(Boxy):
            ship.step()
            if ship.y > 640:
                ship.destroy()
                self.YourMom = False
        for hip in self.getSpritesbyClass(Spring):
            hip.step()
            if hip. y > 640:
                hip.destroy()
        
    def mousemove(self, event):
        self.x = event.x
        self.y = event.y
        
    def Wall(self, event):
        a = round(self.x/ 25)
        b = round(self.y / 25)
        e = a * 25
        f = b * 25
        Wall((e, f))
    
    def Spring(self, event):
        t = round(self.x/ 25)
        h = round(self.y / 25)
        j = t * 25
        k = h * 25
        Spring((j, k))
    
    def Box(self, event):
        if self.YourMom == False:
            Boxy((self.x, self.y))
            self.YourMom = True
    
myapp = Platformer(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()

