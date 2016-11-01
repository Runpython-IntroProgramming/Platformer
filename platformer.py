"""
platformer.py
Author: Finn
Credit: <list sources used, if any>
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
#imports
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

SCREEN_WIDTH=801
SCREEN_HEIGHT=601
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
grey = Color(0x000000, 0.5)

#grid
greenline = LineStyle(1, green)
gridline = LineStyle(1, grey)
grid=RectangleAsset(30,30,gridline,white)
width=list(range(0,41))
height=list(range(0,41))
a=2
'''
Dude = RectangleAsset(10,20,greenline,green)
'''

mousepositionx=0
mousepositiony=0
a=0
b=0
dudesprite = None
wallsprite = None

   
for x in width:
    for y in height:
        Sprite(grid, (20*x,20*y))



class Dude(Sprite):
    dude = RectangleAsset(10,20,greenline,green)
    def __init__(self, a, b):
        super().__init__(Dude.dude, (a, b))
        self.x = a
        self.y = b
    
    def step(self):
        self.gravity += 0.3
        self.y += self.gravity
        dudecollisions = self.collidingWithSprites(Wall)
        if dudecollisions:
            self.y -= self.gravity
            self.gravity = 0
        
class Wall(Sprite):
    wall = RectangleAsset(20,20,gridline,black)
    def __init__(self, a, b):
        super().__init__(Wall.wall, (a, b))
        self.x = a
        self.y = b



gravity=0






class Game(App):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        
        super().__init__()
        a = 0
        b = 0
        self.dudesprite = None
        self.listenKeyEvent('keydown', 'w', classwall)
        self.listenMouseEvent('mousemove', drag)
        self.listenKeyEvent('keydown', 'p', classdude)
        self.listenKeyEvent('keydown', 'right arrow', Right)
        self.listenKeyEvent('keydown', 'left arrow', Left)
        self.listenKeyEvent('keydown', 'up arrow', Jump)
    
    def drag(self, event):
        global mousepositionx
        global mousepositiony
        global a
        global b
        a=event.x
        b=event.y
        mousepositionx=(event.x - event.x%20)
        mousepositiony=(event.y- event.y%20)

    def classwall(self, event):
        gravity=0
        global a, b, wallsprite
        wallsprite = Wall(a-a%20, b-b%20)

    def classdude(self,event):
        gravity = 0
        global a, b, dudesprite
        dudesprite = Dude(a, b)
 
    def step(self):
        global gravity
        if self.dudesprite:
            gravity += 0.3
            self.dudesprite.y += gravity
            collisions = self.dudesprite.collidingWithSprites(Wall)
            if collisions:
                self.dogsprite.y -= gravity
                gravity = 0
                
    def Right(self,event):
        c=0
        while c != 5:
            if dudesprite:
                dudesprite.x += 1
                bump = dudesprite.collidingWithSprites(Wall)
                if bump:
                    dudesprite.x -= 1
            c = c + 1
    

                
    def Left(self,event):
        if dudesprite:
            dudesprite.x -= 5
            bump = dudesprite.collidingWithSprites(Wall)
            if bump:
                dudesprite.x += 5
       
    def Jump(event):
        global gravity
        if dudesprite:
            gravity = -5
myapp = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()