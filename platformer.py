"""
platformer.py
Author: Morgan Gardner
Credit: https://github.com/HHS-IntroProgramming/Platformer
        https://github.com/BrythonServer/Platformer
        http://programarcadegames.com/index.php?chapter=example_code_platformer


Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800


blue = Color(0x2EFEC8, 1.0)
yellow = Color(0xffff00, 1.0)
black = Color(0x000000, 1.0)
pink = Color(0xFF00FF, 1.0)
red = Color(0xFF5733, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800



class GenericWall(Sprite):
   def __init__(self, x, y, w, h, color):
       snapfunc = lambda X : X - X % w
       super().__init__(
           RectangleAsset(w-1,h-1,LineStyle(0,Color(0x0000ff, 1.0)), color),
           (snapfunc(x), snapfunc(y)))
       collideswith = self.collidingWithSprites(type(self))
       if len(collideswith):
           collideswith[0].destroy()

class Wall(GenericWall):
   def __init__(self, x, y):
       super().__init__(x, y, 35, 35, Color(0x0000ff, 1.0))
      
class Goal(GenericWall):
   def __init__(self, x, y):
       super().__init__(x, y, 40, 80, Color(0xffff00, 1.0))
       
class Platform(GenericWall):
   def __init__(self, x, y):
       super().__init__(x, y, 70, 25, Color(0x2EFEC8, 1.0))
  
class GravityActor(Sprite):
   def __init__(self, x, y, width, height, color, app):
       self.vx = self.vy = 0
       self.stuck = False
       self.app = app                        
       self.resting = False                 
       super().__init__(
           RectangleAsset(
               width, height,
               LineStyle(0, Color(0, 1.0)),
               color),
           (x, y))


   def step(self):
       self.x += self.vx
       collides = self.collidingWithSprites(Wall)
       collides.extend(self.collidingWithSprites(Platform))
       for collider in collides:
           if self.vx > 0 or self.vx < 0:
               if self.vx > 0:
                   self.x = collider.x - self.width - 1
               else:
                   self.x = collider.x + collider.width + 1
               self.vx = 0
       self.y += self.vy
       collides = self.collidingWithSprites(Wall)
       collides.extend(self.collidingWithSprites(Platform))
       for collider in collides:
           if self.vy > 0 or self.vy < 0:
               if self.vy > 0:
                   self.y = collider.y - self.height - 1
                   if not self.resting:
                       self.vx = 0
                   self.resting = True
                   self.vy = 0
               elif isinstance(collider, Wall):
                   pass
       self.vy += 1
       if self.y > self.app.height:
           self.app.killMe(self)



