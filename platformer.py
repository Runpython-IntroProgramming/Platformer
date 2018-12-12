"""
platformer.py
Author: Kyle Rozzi
Credit:Mr. Dennison, Mr. Dennison's sample program, and Tristan Meyer
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
from math import floor

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

pink = Color(0xFF00FF, 1.0)
red = Color(0xFF5733, 1.0)
red = Color(0xff0000, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
grey = Color(0xC0C0C0, 1.0)

gridline = LineStyle(1, grey)

class Block(Sprite):
    def __init__(self, position):
        box = RectangleAsset(40,40, LineStyle(4, grey),red)
        super().__init__(box, position)
class Falling(Sprite):
    def __init__(self,x,y,w,h,COLOR,app):
        self.vx=0
        self.vy=0
        self.app=app
        self.stuck=False
        self.resting=False
        BOX=RectangleAsset(w,h,LineStyle(0, white),COLOR)
        super().__init__(BOX,(x, y)) 
    def step(self):
        self.x+=self.vx
        collision=self.collidingWithSprites(Block)
        for i in collision:
            if self.vx>0 or self.vx<0:
                if self.vx > 0:
                    self.x = i.x - self.width - 1
                else:
                    self.x = i.x + i.width + 1
                self.vx = 0
        self.y += self.vy
        collision=self.collidingWithSprites(Block)
        self.vy+=1
        if self.y>self.app.height:
            self.app.killMe(self)
        for i1 in collision:
            if self.vy>0 or self.vy<0:
                if self.vy>0:
                    self.y= i1.y - self.height-1
                    if not self.resting:
                        self.vx=0
                    self.resting=True
                    self.vy=0
                else:
                    self.y=i1.y+i1.height
                    self.vy=0
class Spring(Falling):
    def __init__(self,x,y,app):
        super().__init__(x,y,20,10,pink, app)
    def step(self):
        if self.resting:
            self.app.q.remove(self)
        super().step()
class User(Falling):
    def __init__(self,x,y,app):
        super().__init__(x,y,20,40,blue, app)
    def step(self):
        springtouch = self.collidingWithSprites(Spring)
        if springtouch:
            self.vy = -20
            self.resting=False
        super().step()
    def Arrows(self, key):
        if key == "left arrow":
                self.vx = -8
        elif key == "right arrow":
                self.vx = 8
        elif key == "up arrow" and self.resting:
            self.vy = -14
            self.resting = False
    def stop(self, key):
        if key == "left arrow" or key == "right arrow":
            if self.resting:
                self.vx = 0
class Game(App):
    def __init__(self):
        super().__init__()
        grid = RectangleAsset(40,40,gridline,white)
        x = 0 
        y = 0 
        for d in range(20):
            for e in range(30):
                Sprite(grid, (x,y))
                x = x + 40
            x = 0
            Sprite(grid,(x,y))
            y = y + 40
        super().__init__()
        self.listenKeyEvent("keydown", "b", self.cBlock)
        self.listenKeyEvent("keydown", "p", self.cUser)
        self.listenKeyEvent("keydown", "s", self.cSpring)
        self.listenKeyEvent("keydown", "left arrow", self.Keys)
        self.listenKeyEvent("keydown", "right arrow", self.Keys)
        self.listenKeyEvent("keydown", "up arrow", self.Keys)
        self.listenKeyEvent("keyup", "left arrow", self.stopKeys)
        self.listenKeyEvent("keyup", "right arrow", self.stopKeys)
        self.listenKeyEvent("keyup", "up arrow", self.stopKeys)
        self.listenMouseEvent("mousemove", self.Mouse)
        self.q = []
        self.w = []
        self.g = None
        self.pos = (0,0)
    def Mouse(self, event):
        self.pos = (event.x, event.y)
    def cBlock(self,event):
        x = floor(self.pos[0]/40)*40
        y = floor(self.pos[1]/40)*40
        Block((x,y))
    def cUser(self, event):
        for t in Game.getSpritesbyClass(User):
            t.destroy()
            self.g = None
        self.g = User(self.pos[0], self.pos[1], self)
    def cSpring(self, event):
        self.q.append(Spring(self.pos[0], self.pos[1], self))
    def Keys(self, event):
        if self.g:
            self.g.Arrows(event.key)
    def stopKeys(self,event):
        if self.g:
            self.g.stop(event.key)
    def step(self):
        if self.g:
            self.g.step()
        for i in self.q:
            i.step()
        for o in self.w:
            o.destroy()
        self.w=[]
    def killMe(self,t):
        if t in self.q:
            self.q.remove(t)
        elif t == self.g:
            self.g = None
        if not t in self.w:
            self.w.append(t)
print('Move your mouse around the screen and:')
print('create a block with b')
print('create a spring with s')
print('create a player with p')
print('Control your player with the arrow keys')
app=Game()
app.run()
                
         
                
    