"""
platformer.py
Author: Sarah Dunbar
Credit: http://brythonserver.github.io/ggame/
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

class Dummy(Sprite):
    black = Color(0x000000, 1.0)
    thinline = LineStyle (1, black)
    asset = RectangleAsset(50, 50, thinline, black)
    def __init__(self, position):
        super().__init__(Dummy.asset, position)
        self.vx = 1
        self.vy = 1
        self.thrustframe = 1
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.thrust = 0
        self.thrustframe = 1
        Sandbox.listenKeyEvent("keydown", "w", self.Generate1)
    
    def Move (self, event):
        x = event.x
        y = event.y
        xreal = x%50
        yreal = y%50
        if xreal < 25:
            xx = x - xreal
        else:
            xx = x + (50 - xreal)
        if yreal < 25:
            yy = y - yreal
        else:
            yy = y + (50 - yreal)
        Dummy ((xx, yy))
        Sandbox.unlistenMouseEvent("mousemove", self.Move)
        
    def Generate1 (self, event):
        Sandbox.listenMouseEvent("mousemove", self.Move)

class Player(Sprite):
    grassy = Color(0xeeff00, 1.0)
    thinline = LineStyle (1, grassy)
    asset = RectangleAsset(15, 45, thinline, grassy)
    
    def __init__(self, position):
        super().__init__(Player.asset, position)
        self.p = 1
        self.vx = 1
        self.vy = 1
        self.thrustframe = 1
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.p = 0
        self.thrust = 0
        self.thrustframe = 1
        Sandbox.listenKeyEvent("keydown", "w", self.up)
        Sandbox.listenKeyEvent("keydown", "s", self.down)
        Sandbox.listenKeyEvent("keydown", "a", self.left)
        Sandbox.listenKeyEvent("keydown", "d", self.right)
        Sandbox.listenKeyEvent("keyup", "w", self.upoff)
        Sandbox.listenKeyEvent("keyup", "s", self.downoff)
        Sandbox.listenKeyEvent("keyup", "a", self.leftoff)
        Sandbox.listenKeyEvent("keyup", "d", self.rightoff)
        Sandbox.listenKeyEvent("keydown", "p", self.Generate)
        self.fxcenter = self.fycenter = 0.5

    def step(self):
        oldy = self.y
        self.p += .1
        self.y += self.p
        coll = len(self.collidingWithSprites())
        if coll > 1:
            self.p = 0
            self.y = oldy
        oldy = self.y
        oldx = self.x
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        coll = len(self.collidingWithSprites())
        if coll > 1:
            self.p = 0
            self.y = oldy
            self.x = oldx

    def up (self, event):
        self.vy += 3
        self.vy += 2
        self.p = 0
    
    def down (self, event):
        self.vy += .1
        
    def left (self, event):
        self.vx += -.1
        
    def right (self, event):
        self.vx += .1
        
    def upoff (self, event):
        self.vy = 0
    
    def downoff (self, event):
        self.vy = 0
        
    def leftoff (self, event):
        self.vx = 0
        
    def rightoff (self, event):
        self.vx = 0
        
    def Move (self, event):
        self.x = event.x
        self.y = event.y
        Sandbox.unlistenMouseEvent("mousemove", self.Move)
        
    def Generate (self, event):
        Sandbox.listenMouseEvent("mousemove", self.Move)
        self.vy += 2
        #http://brythonserver.github.io/ggame/#ggame.App.listenMouseEvent

class Sandbox(App):
    
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0xFFFFEE, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(width, height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        Dummy ((100, 300))
        Player((100, 100))
    
    def step(self):
        for x in self.getSpritesbyClass(Player):
            x.step()


myapp = Sandbox(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()