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
        self.collidetop=Collide(position,15,5,green)
        self.collidebottom=Collide(position,10,5,blue)
        self.collideleft=Collide(position,5,22,red)
        self.collideright=Collide(position,5,22,pink)
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
        self.collidetop.x = self.x
        self.collidetop.y = self.y-15
        self.collidebottom.x =self.x
        self.collidebottom.y =self.y+10
        self.collideright.x =self.x+7
        self.collideright.y =self.y
        self.collideleft.x =self.x-7
        self.collideleft.y =self.y
        upcollide=self.collidetop.collidingWithSprites(Wallblock)
        downcollide=self.collidebottom.collidingWithSprites(Wallblock)
        downcollidep=self.collidebottom.collidingWithSprites(Platform)
        downcollide.extend(downcollidep)
        if len(downcollide)>0:
            if self.vy>0:
                if self.vy>=3:
                    self.vy=0
                    self.y=self.y-3
                self.vy=0
                self.resting=1
        elif len(downcollide)==0:
            self.vy=self.vy+.2
            self.resting=0
            if len(upcollide):
                self.y=self.y+3
                self.vy=self.vy*-.5
        leftcollide=self.collideleft.collidingWithSprites(Wallblock)
        if len(leftcollide):
            self.x=self.x+3
            self.vx=self.vx*-0.5
        rightcollide=self.collideright.collidingWithSprites(Wallblock)
        if len(rightcollide):
            self.x=self.x-3
            self.vx=self.vx*-0.5
        if self.left==1:
            self.vx=-3
        else:
            if self.right==1:
                self.vx=3
            else:
                self.vx=0
        
        if self.thrust == 1:
            self.vy = -7
            self.thrust=0
        else:
            if self.y>=x:
                self.vy=0
        
    def thrustOn(self, event):
        if self.y>=x or self.resting==1:
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
    def __init__(self, position,w,h,color):
        super().__init__(RectangleAsset(w,h,noline, color), position)
        self.fxcenter = 0.5
        self.fycenter = 0.5
        self.visible=False

class Wallblock(Sprite):
    def __init__(self, x, y, w, h, color):
        grid=lambda W: (W-W%51)
        super().__init__(RectangleAsset(w-1,h-1,noline, color),
            (grid(x), grid(y)))
        collideswith = self.collidingWithSprites(type(self))
        if len(collideswith):
            collideswith[0].destroy()
        Wallblock.fxcenter = Wallblock.fycenter = 0
class Platform(Wallblock):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 10, blue)
class Block(Wallblock):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50, red)
class Longblock(Wallblock):
    def __init__(self, x, y):
        super().__init__(x, y, 100, 50, pink)
class SpaceGame(App):
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
        self.listenKeyEvent("keydown", "w", self.Block)
        self.listenKeyEvent("keydown", "p", self.Platform)
        self.listenMouseEvent("mousemove", self.Mouse)
        self.listenKeyEvent("keydown", "l", self.Longblock)
    def Mouse(self, event):
        self.pos = (event.x, event.y)
    
    def Block(self,event):
        Block(self.pos[0], self.pos[1])
    def Platform(self,event):
        Platform(self.pos[0], self.pos[1])
    def Longblock(self,event):
        Longblock(self.pos[0], self.pos[1])  
        
    def step(self):
        for ship in self.getSpritesbyClass(Player):
            ship.step()
        
        
myapp = SpaceGame()
myapp.run()