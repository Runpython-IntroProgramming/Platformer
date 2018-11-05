"""
platformer.py
Author: Olivia Simon
Credit: 
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame

myapp = App()

SCREEN_WIDTH = 1000
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
grid=RectangleAsset(30,30,gridline,white)


#class Wall(Sprite):
    #def __init__(self, x, y, w, h, color):
       # place = lambda X = X - % w
       # super().__init__(
        #    RectangleAsset(50, 50, blackLine, black)
        #    (snapfunc(x), snapffunc(y))
    
#class Player(Sprite):
  #  def 
    
#class Spring(Sprite):
   # def 
    
#class Gravity(Sprite):
   # def 
class Blocks(Sprite):
    def __init__(self, x, y, w, h, color):
        grid = lambda X : X - X % w
        super().__init__(
            RectangleAsset(w-1, h-1, LineStyle(0,Color(0, 1.0)), color),(grid(x), grid(y)))
        #collisions
        collisionsontra=self.collidingWithSprites(type(self))
        if len(collisioncontra):
            collisioncontra[0].destroy()
            

class wall(Blocks):
    def __init__(self,x,y):
        super().__init__(x,y,60,60,Color(0,1.0))      #(self, x, y, w, h, color)
        
class Newton(Sprite):
     def __init__(self, x, y, width, height, color, app):
        self.stuck = False
        self.app = app                          # app, need to know
        self.resting = False                    # whether resting on wall
        super().__init__(
            RectangleAsset(
                width, height, 
                LineStyle(0, Color(0, 1.0)),
                color), (x, y)) 
                
        collisionsontra=self.collidingWithSprites()
        if len(collisioncontra):
            self.destroy()

class playah(Newton):
    def __init__(self, x, y, app):
        x = 
        y = 

def wallKey(event):
    Sprite(wall,)

    
myapp.listenKeyEvent('keydown','w',wallKey)

#def playaKey(event):
    
#def springKey(event):

# A super wall class for wall-ish behaviors
#class GenericWall(Sprite):
    #def __init__(self, x, y, w, h, color):
        #snapfunc = lambda X : X - X % w
       # super().__init__(
            #RectangleAsset(w-1,h-1,LineStyle(0,Color(0, 1.0)), color),
            #(snapfunc(x), snapfunc(y)))
myapp.run()
