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
black= Color(0x000000, 1.0)

thinline = LineStyle(1, black)
noline= LineStyle(0, black)

block= RectangleAsset(125, 65, noline, turquoise)
Sprite(block, (55, 250))

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Box3D(object):
    def __init__(self, width, length, height):
        self.w = width
        self.l = length
        self.h = height

    def volume(self):
        return self.w * self.l * self.h
        
box = Box3D(1,3,6)    # create a box object using the 
                      # Box3D class or "blueprint"
box2 = Box3D(3,6,2)   # create another, different object 
                      # using the same class
print(box.volume())
print(box2.volume())  # volume() is a method of the Box3D class
print(box.h)          # you can access the members
box.h = 99.0          # and you can change them
print(box.volume())   # and it will change the box properties


myapp= App()
myapp.run()