"""
platformer.py
Author: Dina
Credit: Jazzy, Anushka, Mr.Dennison, ggame documentaion
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

red= Color(0xFE2E64, 1.0)
green = Color(0x5dff00, 1.0)
bluelight = Color(0x81F7F3,1.0)
blue= Color(0x0000ff, 1.0)
white= Color(0xffffff, 1.0)
thinline = LineStyle(3, red)
blueline = LineStyle(3, blue)

#Walls
class Wall(Sprite):
    wall = RectangleAsset(50, 50, thinline, bluelight)
    def __init__(self, xPos, yPos):
        super().__init__(Wall.wall, (xPos, yPos))
        self.x = xPos
        self.y = yPos
#Sprite
class Ball(Sprite):
    ball = RectangleAsset(30, 30, blueline, blue)
    def __init__(self, xPos, yPos):
        super().__init__(Ball.ball, (xPos, yPos))
        self.x = xPos
        self.y = yPos
        self.xvel = 0
        self.yvel = 0
        self.fxcenter = 0.5
        self.fycenter = 0.5
#spring
class spring(Sprite):
    Spring = RectangleAsset(30, 5, thinline, blue)
    def __init__(self, xPos, yPos):
        super().__init__(spring.Spring, (xPos, yPos))
        self.x = xPos
        self.y = yPos
#endings sprite
class winner(Sprite):
    win = RectangleAsset(30, 30, blueline, green)
    def __init__(self, xPos, yPos):
        super().__init__(winner.win, (xPos, yPos))
        self.x = xPos
        self.y = yPos

gravity = 0
Sgravity = 0
#App
class Platformer(App):
    def __init__(self):
        super().__init__()
        self.mousex = 0
        self.mousey = 0
        self.JAZZY = 0
        self.spring = 0
        self.winner = 0
        self.Wall = 0
        self.listenKeyEvent('keydown', 'q', self.buildWall)
        self.listenKeyEvent('keydown', 'e', self.buildChara)
        self.listenMouseEvent('mousemove', self.mousemove)
        self.listenKeyEvent('keydown', 'a', self.moveL)
        self.listenKeyEvent('keydown', 'w', self.moveU)
        self.listenKeyEvent('keydown', 'd', self.moveR)
        self.listenKeyEvent('keydown', 's', self.buildSpring)
        self.listenKeyEvent('keydown', 'r', self.buildahh)
    #make wall
    def buildWall(self, event):
        x = self.mousex- self.mousex%50
        y = self.mousey- self.mousey%50
        self.Wall = Wall(x-25, y-25)
    #tracks where the  mouse is
    def mousemove(self, event):
        self.mousex = event.x
        self.mousey = event.y
    #make !!!
    def buildahh(self, event):
        if self.winner:
            self.winner.destroy()
        self.winner = winner(self.mousex, self.mousey)
    #make Sprite
    def buildChara(self, event):
        global gravity
        if self.JAZZY:
            self.JAZZY.destroy()
            gravity = 0
        self.JAZZY = Ball(self.mousex, self.mousey)
        self.z = self.mousex
    #make Spring
    def buildSpring(self, event):
        global Sgravity
        self.spring = spring(self.mousex, self.mousey)
    #move the Sprite Left
    def moveL(self, event):
        if self.JAZZY:
            self.JAZZY.x -= 2
            p = self.JAZZY.collidingWithSprites(Wall)
            if p:
                self.JAZZY.x += 2
    #Up
    def moveU(self, event):
        if self.JAZZY:
            global gravity
            if gravity == 0:
                gravity = -7
                p = self.JAZZY.collidingWithSprites(Wall)
                if p:
                    self.JAZZY.y += 50
    #Right
    def moveR(self, event):
        if self.JAZZY:
            self.JAZZY.x += 2
            p = self.JAZZY.collidingWithSprites(Wall)
            if p:
                self.JAZZY.x -= 2
    #gravity
    def step(self):
        global gravity
        global Sgravity
        if self.spring:
            Sgravity +=0.2
            self.spring.y += Sgravity
            i = self.spring.collidingWithSprites(Wall)
            if i:
                self.spring.y -= Sgravity
                Sgravity = 0
        if self.JAZZY:
            gravity +=0.2
            self.JAZZY.y += gravity
            p = self.JAZZY.collidingWithSprites(Wall)
            o = self.JAZZY.collidingWithSprites(spring)
            if p:
                self.JAZZY.y -= gravity
                gravity = 0
            if o:
                self.JAZZY.y -= gravity
                gravity = -10
        if self.JAZZY and winner:
            u = self.JAZZY.collidingWithSprites(winner)
            if u:
                print ("winner!!!!!!!!!!!!!!!!!!!!")
                f = input("If you are done with this game write 'done'")
                if f == 'done':
                    self.JAZZY.destroy()
                    self.spring.destroy()
                    self.Wall.destroy()
                    self.winner.destroy()
myapp = Platformer()
myapp.run()