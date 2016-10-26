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

def drag(event):
    global mousepositionx
    global mousepositiony
    global a
    global b
    a=event.x
    b=event.y
    mousepositionx=(event.x - event.x%20)
    mousepositiony=(event.y- event.y%20)

class Dude(Sprite):
    dude = RectangleAsset(10,20,greenline,green)
    def __init__(self, a, b):
        super().__init__(Dude.dude, (a, b))
        self.x = a
        self.y = b
        
class Wall(Sprite):
    wall = RectangleAsset(20,20,gridline,black)
    def __init__(self, a, b):
        super().__init__(Wall.wall, (a, b))
        self.x = a
        self.y = b

def classwall(event):
    gravity=0
    global a, b, wallsprite
    wallsprite = Wall(a-a%20, b-b%20)

def classdude(event):
    gravity = 0
    global a, b, dudesprite
    dudesprite = Dude(a, b)




def Right(event):
    if dudesprite:
        dudesprite.x += 5
        bump = dudesprite.collidingWithSprites(Wall)
        q=0
        if bump:
            while q != 5:
                dudesprite.x -= 5-q
                q = q+1

                
def Left(event):
    if dudesprite:
        dudesprite.x -= 5
       
def Jump(event):
    global gravity
    if dudesprite:
        gravity = -5




myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenKeyEvent('keydown', 'w', classwall)
myapp.listenMouseEvent('mousemove', drag)
myapp.listenKeyEvent('keydown', 'p', classdude)

myapp.listenKeyEvent('keydown', 'right arrow', Right)
myapp.listenKeyEvent('keydown', 'left arrow', Left)
myapp.listenKeyEvent('keydown', 'up arrow', Jump)

myapp.run()