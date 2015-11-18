"""
platformer.py
Author: Dina
Credit: so far none
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

black= Color(0x000000, 1.0)
red = Color(0xff0000,1.0)
thinline = LineStyle(3, red)

class Wall(Sprite):
    wall = RectangleAsset(50, 50, thinline, black)
    def __init__(self, xPos, yPos):
        super().__init__(Wall.wall, (xPos, yPos))
        self.x = xPos
        self.y = yPos

def buildWall(event):
    #xPos.x = event.x
    #yPos.y = event.y
    Wall(event.x+25, event.y+25)


class Platformer(App):
    def __init__(self):
        super().__init__()
        

myapp = Platformer()
myapp.listenMouseEvent('click', buildWall)
#myapp.listenMouseEvent('
myapp.run()