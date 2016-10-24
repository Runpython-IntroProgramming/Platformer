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
SCREEN_HEIGHT=801
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
grey = Color(0x000000, 0.5)

#grid
gridline = LineStyle(1, grey)
grid=RectangleAsset(30,30,gridline,white)
width=list(range(0,41))
height=list(range(0,41))
a=2
#display grid
wall = RectangleAsset(20,20,gridline,black)
wall.create = True

   

    
    
   

for x in width:
    for y in height:
        Sprite(grid, (20*x,20*y))
    
def step():
    if wall.create:
        Sprite(wall, (event.x,event.y))
    else:
        a=2



def wKey(event):
    wall.create


myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
# Set up event handlers for the app
myapp.listenKeyEvent('keydown', 'w', wKey)


myapp.run(step)