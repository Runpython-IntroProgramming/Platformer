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
#display grid
wall = RectangleAsset(20,20,gridline,black)
dude = RectangleAsset(10,20,greenline,green)
mousepositionx=0
mousepositiony=0
a=0
b=0

   

for x in width:
    for y in height:
        Sprite(grid, (20*x,20*y))
    

def pKey(even):
    global a
    global b
    Sprite(dude, (a, b))
    
def drag(event):
    global mousepositionx
    global mousepositiony
    global a
    global b
    a=event.x
    b=event.y
    mousepositionx=(event.x - event.x%20)
    mousepositiony=(event.y- event.y%20)

def wKey(event):
    global mousepositionx
    global mousepositiony
    Sprite(wall, (mousepositionx, mousepositiony))



myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
# Set up event handlers for the app
myapp.listenKeyEvent('keydown', 'w', wKey)
myapp.listenMouseEvent('mousemove', drag)
myapp.listenKeyEvent('keydown', 'p', pKey)


myapp.run()