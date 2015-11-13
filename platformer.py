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
        self.x = 100
        self.y = 100
Wall(400,300)

myapp = App()
myapp.run()