"""
platformer.py
Author: Dina
Credit: so far none
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

    
red= Color(0xFE2E64, 1.0)
bluelight = Color(0x81F7F3,1.0)
#blue= Color(0x0000ff, 1.0)
thinline = LineStyle(3, red)

class Wall(Sprite):
    wall = RectangleAsset(50, 50, thinline, bluelight)
    def __init__(self, xPos, yPos):
        super().__init__(Wall.wall, (xPos, yPos))
        self.x = xPos
        self.y = yPos
'''
class Ball(Sprite):
    ball = CircleAsset(15, thinline, blue)

def moveChara(event):
 Sprite(Ball, (event.x, event.y))
'''
def buildWall(event):
    x = event.x%30
    if x != 0:
        if x >= 15:
            e = 30- x
            x = event.x + e
        elif x < 15:
            e = 15-x
            x = event.x - e
    Wall(x-25, event.y-25)

class Platformer(App):
    def __init__(self):
        super().__init__()

myapp = Platformer()
myapp.listenMouseEvent('click', buildWall)
#myapp.listenKeyEvent('keydown', 'space', moveChara)
myapp.run()