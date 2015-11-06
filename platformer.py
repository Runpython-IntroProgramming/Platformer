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

class Springt(Sprite):
    water = Color(0x660000, 1.0)
    thinline = LineStyle (1, water)
    asset = RectangleAsset (20, 5, thinline, water)

    def __init__ (self, position):
        super().__init__(Springt.asset, position)
        self.vy = 1
        Sandbox.listenKeyEvent("keydown", "s", self.Generate)
        
    def step(self):
        oldy = self.y
        self.vy += .05
        self.y += self.vy
        coll = len(self.collidingWithSprites())
        if coll > 1:
            self.vy = 0
            self.y = oldy
        oldy = self.y
        oldx = self.x
        self.y += self.vy
        coll = len(self.collidingWithSprites())
        if coll > 1:
            self.vy = 0
            self.y = oldy
        
    def Move (self, event):
        self.x = event.x
        self.y = event.y
        Sandbox.unlistenMouseEvent("mousemove", self.Move)
        
    def Generate (self, event):
        self.vy = 0
        Sandbox.listenMouseEvent("mousemove", self.Move)

class Dummy(Sprite):
    black = Color(0xCC0033, 1.0)
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
        self.vx = 1
        self.vy = 1
        self.thrustframe = 1
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.g = 1
        self.thrust = 0
        self.thrustframe = 1
        Sandbox.listenKeyEvent("keydown", "up arrow", self.up)
        Sandbox.listenKeyEvent("keydown", "down arrow", self.down)
        Sandbox.listenKeyEvent("keydown", "left arrow", self.left)
        Sandbox.listenKeyEvent("keydown", "right arrow", self.right)
        Sandbox.listenKeyEvent("keyup", "up arrow", self.upoff)
        Sandbox.listenKeyEvent("keyup", "down arrow", self.downoff)
        Sandbox.listenKeyEvent("keyup", "left arrow", self.leftoff)
        Sandbox.listenKeyEvent("keyup", "right arrow", self.rightoff)
        Sandbox.listenKeyEvent("keydown", "p", self.Generate)
        self.fxcenter = self.fycenter = 0.5

    def step(self):
        oldy = self.y
        self.vy += .1
        self.y += self.vy
        coll = len(self.collidingWithSprites())
        if coll > 1:
            self.vy = 0
            self.y = oldy
        oldy = self.y
        oldx = self.x
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        coll = len(self.collidingWithSprites())
        if coll > 1:
            self.vy = 0
            self.y = oldy
            self.x = oldx

    def up (self, event):
        self.y = self.y + 1
        x = self.collidingWithSprites()
        print (x)
        twix = len(self.collidingWithSprites())
        if twix > 1:
            self.vy = -3
            print (self.vy)
    
    def down (self, event):
        self.vy += .1
        
    def left (self, event):
        self.vx += -.1
        
    def right (self, event):
        self.vx += .1
        
    def upoff (self, event):
        self.vy += 0
    
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
        self.vy = 0
        Sandbox.listenMouseEvent("mousemove", self.Move)
        #http://brythonserver.github.io/ggame/#ggame.App.listenMouseEvent

class Sandbox(App):
    
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0xFFFFEE, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(width, height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        Springt((200, 200))
        Dummy ((100, 300))
        Player((100, 100))
    
    def step(self):
        for x in self.getSpritesbyClass(Player):
            x.step()
        for x in self.getSpritesbyClass(Springt):
            x.step()


myapp = Sandbox(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
