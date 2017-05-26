"""
platformer.py
Author: 
Credit: 
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame

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

thinline = LineStyle(2, black)
blkline = LineStyle(1, black)
noline = LineStyle(0, white)
coolline = LineStyle(1, grey)
blueline = LineStyle(2, blue)
redline = LineStyle(1, red)
greenline = LineStyle(1, green)
gridline = LineStyle(1, grey)
grid=RectangleAsset(30,30,gridline,white)


black = Color(0, 1)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, black)
bg = Sprite(bg_asset, (0,0))
        
class Guy(Sprite):
    guy = RectangleAsset(20, 20, thinline, green)
    def __init__(self, x, y):
        super().__init__(Guy.guy, (x, y))
        self.x = x
        self.y = y
        
class Brick(Sprite):
    brick = RectangleAsset(30, 30, thinline, pink)
    def __init__(self, x, y):
        super().__init__(Brick.brick, (x, y))
        self.x = x
        self.y = y
        
    def step(self):
        self.grav += 0.2
        self.y += self.grav
        collide = self.collidingWithSprites(brick)
        if collide:
            self.y -= self.grav
            self.grav = 0
            
grav=0

class Pform(App):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        self.mousex = 0
        self.mousey = 0
        self.guy = 0
        self.guysprite = None
        self.brick = None
        self.listenKeyEvent('keydown', 'p', self.createGuy)
        self.listenKeyEvent('keydown', 'w', self.createBrick)
        self.listenMouseEvent('mousemove', self.motion)
        self.listenKeyEvent('keydown', 'right arrow', self.R)
        self.listenKeyEvent('keydown', 'left arrow', self.L)
        self.listenKeyEvent('keydown', 'up arrow', self.U)
        self.listenKeyEvent('keydown', 'down arrow', self.D)




    def motion(self, event):
        self.mousex = event.x
        self.mousey = event.y
    
    def createGuy (self, event):
        global grav
        if self.guysprite:
            self.guysprite.destroy()
            grav = 0
        self.guysprite = Guy(self.mousex - 15, self.mousey - 15)
    
    def createBrick(self, event):
        x = self.mousex - self.mousex%20
        y = self.mousey - self.mousey%20
        Brick(x-10, y-10)
        
        
    def R(self, event):
        self.guysprite.x += 5
        collisions = self.guysprite.collidingWithSprites(Brick)
        if collisions:
            self.guysprite.x -= 5
            
    def L(self, event):
        self.guysprite.x -= 5
        collisions = self.guysprite.collidingWithSprites(Brick)
        if collisions:
            self.guysprite.x += 5
            
    def U(self, event):
        global grav
        if grav == 0:
            grav = -7
            collisions = self.guysprite.collidingWithSprites(Brick)
            if collisions:
                self.guysprite.y += 50

    def D(self, event):
        self.guysprite.y += 5
        collisions = self.guysprite.collidingWithSprites(Brick)
        if collisions:
            self.guysprite.y -= 5
            
    def step(self):
        global grav
        print('a')
        if self.guysprite:
            grav += 0.3
            print('a')
            self.guysprite.y += grav
            print('a')
            collisions = self.guysprite.collidingWithSprites(Brick)
            print('a')
            if collisions:
                self.guysprite.y -= grav
                grav = 0
            


myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()