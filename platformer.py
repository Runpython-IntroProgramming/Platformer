"""
platformer.py
Author: Patrick Daley
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

rectangle = RectangleAsset(50, 50, blkline, white)

#---------------------------------------------------------------------------
#Grid
for x in range(0, 21):
    for y in range(0, 11):
        Sprite(rectangle, (50*x, 50*y))
#---------------------------------------------------------------------------
#Player

player = RectangleAsset(15,30, blkline, red)
Sprite(player,(20,20))
player.direction = 1
player.go = True
def reverse(p):
    p.direction *= -1
def step():
    if player.go:
        player.x += ball.direction
        if player.x + player.width > myapp.width or player.x < 0:
            ball.x -= player.direction
            reverse(player)

# Handle the mouse click
def mouseClick(event):
    #RectangleAsset(50, 50, blkline, black)
    Sprite(player)
"""
#Tracking Mouse Movement
class MouseEvent(_Event):
    def __init__ var mousemove # identifies where the mouse is

var keypress # identifies when a key is pressed
var key # which key is pressed
"""

myapp = App()
myapp.run()


