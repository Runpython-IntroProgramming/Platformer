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
blue= Color(0x0000ff, 1.0)
thinline = LineStyle(3, red)
#Walls
class Wall(Sprite):
    wall = RectangleAsset(50, 50, thinline, bluelight)
    def __init__(self, xPos, yPos):
        super().__init__(Wall.wall, (xPos, yPos))
        self.x = xPos
        self.y = yPos

#Sprite
class Ball(Sprite):
    ball = CircleAsset(20, thinline, blue)
    def __init__(self, xPos, yPos):
        super().__init__(Ball.ball, (xPos, yPos))
        self.x = xPos
        self.y = yPos


    

#App
class Platformer(App):
    def __init__(self):
        super().__init__()
        self.mousex = 0
        self.mousey = 0
        self.listenMouseEvent('click', self.buildWall)
        self.listenKeyEvent('keydown', 'r', self.buildChara)
        self.listenMouseEvent('mousemove', self.mousemove)

    #make wall
    def buildWall(self, event):
        x = self.mousex- self.mousex%50
        y = self.mousey- self.mousey%50
        Wall(x-25, y-25)
    
    def mousemove(self, event):
        self.mousex = event.x
        self.mousey = event.y
        
    #make Sprite
    def buildChara(self, event):
        Ball(self.mousex, self.mousey)

'''
def moveChara(event):
 Sprite(Ball, (event.x, event.y))
'''
myapp = Platformer()
myapp.run()