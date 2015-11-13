"""
platformer.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

turquoise= Color(0x2EFEC8, 1.0)

thinline = LineStyle(1, black)
noline= LineStyle(0, black)

Block= RectangleAsset(500, 500, noline, turquoise)
Sprite(block)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Block(Sprite):
    asset = ImageAsset



myapp= App()
myapp.run()