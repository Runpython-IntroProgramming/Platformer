"""
platformer.py
Author: Finn Hackett
Credit: 
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

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

class Wall(Sprite):
    wall = RectangleAsset(40, 40, thinline, grey)
    def __init__(self, x, y):
        super().__init__(Wall.wall, (x, y))
        self.x = x
        self.y = y

class Dude(Sprite):
    dude = RectangleAsset(30, 30, redline, green)
    def __init__(self, x, y):
        super().__init__(Dude.dude, (x, y))
        self.x = x
        self.y = y
        
    
    def step(self):
        self.gravity += 0.3
        self.y += self.gravity
        scollisions = self.collidingWithSprites(wall)
        if scollisions:
            self.y -= self.gravity
            self.gravity = 0

gravity = 0

class Platformer(App):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        self.mousex = 0
        self.mousey = 0
        self.dude = 0
        self.dudesprite = None
        self.listenKeyEvent('keydown', 'p', self.buildDude)
        self.listenKeyEvent('keydown', 'w', self.buildWall)
        self.listenMouseEvent('mousemove', self.motion)
        self.listenKeyEvent('keydown', 'right arrow', self.R)
        self.listenKeyEvent('keydown', 'left arrow', self.L)
        self.listenKeyEvent('keydown', 'up arrow', self.U)
        self.listenKeyEvent('keydown', 'down arrow', self.D)
    
    def motion(self, event):
        self.mousex = event.x
        self.mousey = event.y
    
    def buildDude (self, event):
        global gravity
        if self.dudesprite:
            self.dudesprite.destroy()
            gravity = 0
        self.dudesprite = Dude(self.mousex - 15, self.mousey - 15)
    
    def buildWall(self, event):
        x = self.mousex - self.mousex%40
        y = self.mousey - self.mousey%40
        Wall(x-10, y-10)
        
    def destroyWall(self, event):
        x = self.mousex - self.mousex%40
        y = self.mousey - self.mousey%40
        Wall(x-10, y-10)
        
        
    def R(self, event):
        self.dudesprite.x += 5
        collisions = self.dudesprite.collidingWithSprites(Wall)
        if collisions:
            self.dudesprite.x -= 5
            
    def L(self, event):
        self.dudesprite.x -= 5
        collisions = self.dudesprite.collidingWithSprites(Wall)
        if collisions:
            self.dudesprite.x += 5
            
    def U(self, event):
        global gravity
        if gravity == 0:
            gravity = -7
            collisions = self.dudesprite.collidingWithSprites(Wall)
            if collisions:
                self.dudesprite.y += 50

    def D(self, event):
        self.dudesprite.y += 5
        collisions = self.dudesprite.collidingWithSprites(Wall)
        if collisions:
            self.dudesprite.y -= 5
            
    def step(self):
        global gravity
        if self.dudesprite:
            gravity += 0.3
            self.dudesprite.y += gravity
            collisions = self.dudesprite.collidingWithSprites(Wall)
            if collisions:
                self.dudesprite.y -= gravity
                gravity = 0
            
myapp = Platformer(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()