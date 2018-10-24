
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
grid = RectangleAsset(50,50,gridline,white)

#==Grid=========================================================================
x = 0 
y = 0 
for b in range(15):
    for a in range(25):
        Sprite(grid, (x,y))
        x = x + 50
    x = 0
    Sprite(grid, (x,y))
    y = y + 50
    
#==Player=======================================================================  
myapp = App()

playerasset = RectangleAsset(15, 35, noline, green)
player = Sprite(playerasset)
player.direction = 1
player.go = True

def forward():
    if player.go == True:
        player.x += player.direction

myapp.listenKeyEvent('keydown','d', forward)


def backward(b):
    if player.go == True:
        player.x -= player.direction

myapp.listenKeyEvent('keydown','a', backward)

myapp.run()