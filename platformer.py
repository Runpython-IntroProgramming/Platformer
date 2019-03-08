"""
platformer.py
Author: 
Credit: 
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
x=510
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
L=range(5)
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

thinline = LineStyle(2, black)
blkline = LineStyle(1, black)
noline = LineStyle(0, white)
coolline = LineStyle(1, grey)
blueline = LineStyle(2, blue)
redline = LineStyle(1, red)
greenline = LineStyle(1, green)
gridline = LineStyle(1, grey)
grid=RectangleAsset(30,30,gridline,white)


from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
"""class Collide(Sprite):
     asset = RectangleAsset(10,20,blkline,red) 
    def __init__(self, position):
        super().__init__(Collide.asset, position)
        self.vx = 0
        self.vy = 0
        self.thrust = 0
        self.left=0
        self.right=0
        self.collidingwithsprites=0
    
        self.fxcenter = self.fycenter = 0.5"""
class Player(Sprite):
    """
    Animated space ship
    """
    asset = RectangleAsset(10,20,blkline,green) 
    
    
    def __init__(self, position,):
        super().__init__(Player.asset, position)
        self.vx = 0
        self.vy = 0
        self.thrust = 0
        self.left=0
        self.right=0
        self.collidingwithsprites=0
        self.resting=0
        self.collidetop=Collide(position,15,5,.5,2.6, green)
        self.collidebottom=Collide(position,15,5,.5,-2,blue)
        self.collideleft=Collide(position,5,20,2,.5,red)
        self.collideright=Collide(position,5,20,-1,.5,pink)
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.lefton)
        SpaceGame.listenKeyEvent("keyup", "left arrow", self.leftoff)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.righton)
        SpaceGame.listenKeyEvent("keyup", "right arrow", self.rightoff)
        self.fxcenter = self.fycenter = 0.5
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.collidetop.x += self.vx
        self.collidetop.y += self.vy
        self.collidebottom.x +=self.vx
        self.collidebottom.y +=self.vy
        self.collideright.x +=self.vx
        self.collideright.y +=self.vy
        self.collideleft.x +=self.vx
        self.collideleft.y +=self.vy
        upcollide=self.collidetop.collidingWithSprites(Wallblock)
        if len(upcollide):
            self.vy=0
        downcollide=self.collidebottom.collidingWithSprites(Wallblock)
        if len(downcollide):
            self.vy=0
            self.resting=1
        else:
            self.resting=0
        leftcollide=self.collideleft.collidingWithSprites(Wallblock)
        rigthcollide=self.collideright.collidingWithSprites(Wallblock)
        if self.left==1:
            self.vx=-3
        else:
            if self.right==1:
                self.vx=3
            else:
                self.vx=0
        
        if self.thrust == 1:
            self.vy = -5
            self.thrust=0
        else:
            if self.y>=x:
                self.vy=0
            else:
                if resting==0:
                    self.vy=self.vy+.1
    def thrustOn(self, event):
        if self.y>=x and not self.collidingWithSprites:
            self.thrust = 1
    def thrustOff(self, event):
        self.thrust = 0
    def lefton(self, event):
        self.left=1
    def leftoff(self, event):
        self.left=0
    def righton(self, event):
        self.right=1
    def rightoff(self, event):
        self.right=0

class Collide(Sprite):
    def __init__(self, position,w,h,centerx, centery, color):
        super().__init__(RectangleAsset(w,h,noline, color), position)
        self.fxcenter = centerx
        self.fycenter = centery

class Wallblock(Sprite):
    """
    Animated space ship
    """
    wallasset = RectangleAsset(100, 50, noline, black)

    def __init__(self, x, y):
        grid=lambda W: (W-W%51)
        super().__init__(RectangleAsset(50,50,noline,red),(grid(x), grid(y)))
        # destroy any overlapping walls
        collideswith = self.collidingWithSprites(type(self))
        if len(collideswith):
            collideswith[0].destroy()
        
        Wallblock.fxcenter = Wallblock.fycenter = 0.5

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr



        


class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self):
        super().__init__()
        # Background
        x=510
        beeg=50
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(self.width, self.height, noline, green)
        ground_asset = RectangleAsset(self.width, beeg, noline, white)
        #bg = Sprite(bg_asset, (0,0))
        ground = Sprite(ground_asset, (0, x+beeg/2))
        Player((100,100))
        self.listenKeyEvent("keydown", "w", self.Wallblock)
        self.listenMouseEvent("mousemove", self.Mouse)
    def Mouse(self, event):
        self.pos = (event.x, event.y)
    
    def Wallblock(self,event):
        Wallblock(self.pos[0], self.pos[1])
        
        
        
    def step(self):
        for ship in self.getSpritesbyClass(Player):
            ship.step()
        
        
myapp = SpaceGame()
myapp.run()