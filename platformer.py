"""
platformer.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000


class Player(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(Player.asset, position)
        g = 1
        self.vx = 1
        self.vy = 1
        self.thrust = 0
        self.thrustframe = 1
        Sandbox.listenKeyEvent("keydown", "p", self.mouseClick)
        self.fxcenter = self.fycenter = 0.5

    #def step(self):
        #self.x += self.vx
        #self.y += self.vy
        #self.rotation += self.vr
        #if self.thrust == 1:
            #self.setImage(self.thrustframe)
            #self.thrustframe += 1
            #if self.thrustframe == 4:
            #    self.thrustframe = 1
        #else:
            #self.setImage(0)
            
    def collidingWithSprites(self, sclass=None):
        if sclass == None:
            slist = App.spritelist
        else:
            slist = App.getSpritesbyClass(sclass)
            t = 1
            return t
            #list(filter(self.collidingWith, slist))
            
    def mouseClick(self, event):
        x = event.x
        y = event.y

    def Generate(self, event):
        x = event.x
        y = event.y
        Player((x,y))
        t = 0
        while t == 0:
            self.vy += .1
            t = collidingWithSprites(self, sclass=None)
            
        
        

    def thrustOff(self, event):
        self.thrust = 0



class Sandbox(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(width, height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        Player((0, 0))

    def step(self):
        for x in self.getSpritesbyClass(Player):
            x.step()


myapp = Sandbox(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()