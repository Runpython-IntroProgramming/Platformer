"""
platformer.py
Author: 
Credit: 
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
from math import floor

SCREEN_WIDTH = 1200
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
grid = RectangleAsset(40,40,gridline,white)

class Block(Sprite):
    def __init__(self, x, y, w, h, color):
        box = RectangleAsset(40,40,LineStyle(4,grey), red)
        super().__init__(box,x,y)


class Falling(Sprite):
    def __init__(self,x,y,w,h,COLOR,app):
        self.vx=0
        self.vy=0
        self.app=app
        self.stuck=False
        self.resting=False
        BOX=RectangleAsset(w,h,thinline,COLOR)
        super().__init__(BOX,(x, y)) 
    def step(self):
        self.x=+self.vx
        collision=self.collidingWithSprites(Block)
        if self.x>self.app.w:
            self.app.killMe(self)
        for i in collision:
            if self.vx>0 or self.vx<0:
                if self.vx<0:
                    self.x=i.x+i.w+.1
                    if not self.resting:
                        self.vx = 0
                    self.resting = True
                else:
                    self.x=i.x-self.w-.1
                self.vx=0
        self.y=+self.vy
        collision1=self.collidingWithSprites(Block)
        self.vy+=0.8
        if self.y>self.app.h:
            self.app.killMe(self)
        for i in collision1:
            if self.vy>0 or self.vy<0:
                if self.vy>0:
                    self.y= i.y + self.h-.1
                    if not self.resting:
                        self.vx=0
                    self.resting=True
                else:
                    self.y=i.y+i.h
                    self.vy=0

class Spring(Falling):
    def __init__(self,x,y,app):
        super().__init__(x,y,10,10,pink, app)
        
class User(Falling):
    def __init__(self,x,y,app):
        super().__init__(x,y,10,20,blue, app)
    def step(self):
        springtouch = self.collidingWithSprites(Spring)
        if springtouch:
            self.vy = -22
            self.resting=False
        super().step()
    def Arrows(self,press)
        if press=='right':
            self.vx=7
        elif press=='left':
            self.vx=-7
        elif press=='up' and self.resting:
            self.vy=-14
            self.resting=False
    def stop(self, press):
        if button == 'left' or button == 'right':
            if self.resting:
                self.vx = 0
        else:
            pass
        
class Game(App):
    def __init__(self):
        super().__init__()
        grid = RectangleAsset(40,40,gridline,white)
        x = 0 
        y = 0 
        for d in range(15):
            for e in range(25):
                Sprite(grid, (x,y))
                x = x + 40
            x = 0
            Sprite(grid,(x,y))
            y = y + 40
        self.listenKeyEvent("keydown", 'q', self.cBlock)
        self.listenKeyEvent("keydown", 'p', self.cUser)
        self.listenKeyEvent("keydown", 's', self.cSpring)
        self.listenKeyEvent("keydown", 'left', self.Keys)
        self.listenKeyEvent("keydown",'right', self.Keys)
        self.listenKeyEvent("keydown", 'up', self.Keys)
        self.listenKeyEvent("keyup", 'left', self.stopKeys)
        self.listenKeyEvent("keyup", 'right', self.stopKeys)
        self.listenKeyEvent("keyup", 'up', self.stopKeys)
        self.listenMouseEvent('mouse', self.Mouse)
        z=0
        x=0
        self.i = 0
        
        def moveMouse(self, event):
            self.z = event.x
            self.x = event.y
        def cBlock(self,event):
            x=self.z - self.z%40
            y=self.x - self.x%40
        def springplacement(self,event):
        Spring((self.z,self.x))
        def cUser(self,event):
            for i in Game.getSpritesbyClass(User):
                i.destroy
                self.i=0
            self.i=User((self.z,self.x))
        def cSpring(self,event):
            Spring((self.z,self.x))
        def Keys(self, event):
        if self.i:
            self.i.Arrows(event.press)
        def StopKeys(self, event):
        if self.i:
            self.i.stop(event.press)
         
                
    



