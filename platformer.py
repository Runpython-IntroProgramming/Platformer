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

class Player(GravityActor):
   def __init__(self, x, y, app):
       w = 20
       h = 20
       super().__init__(x-w//2, y-h//2, w, h, Color(0xFF00FF, 1.0), app)



   def step(self):
       springs = self.collidingWithSprites(Spring)
       if len(springs):
           self.vy = -15
           self.resting = False
       super().step()
      
   def move(self, key):
       if key == "left arrow":
           if self.vx > 0:
               self.vx = 0
           else:
               self.vx = -5
       elif key == "right arrow":
           if self.vx < 0:
               self.vx = 0
           else:
               self.vx = 5
       elif key == "up arrow" and self.resting:
           self.vy = -12
           self.resting = False
          
   def stopMove(self, key):
       if key == "left arrow" or key == "right arrow":
           if self.resting:
               self.vx = 0
               
class Spring(GravityActor):
   def __init__(self, x, y, app):
       w = 10
       h = 4
       super().__init__(x-w//2, y-h//2, w, h, Color(0x0000ff, 1.0), app)
      
   def step(self):
       if self.resting:
           self.app.FallingSprings.remove(self)
       super().step()
      
class Goal(Sprite):
   def __init__(self, x, y, w, h, color):
       snapfunc = lambda X : X - X % w
       super().__init__(
           RectangleAsset(w-1,h-1,LineStyle(0,Color(0x00ff00, 1.0)), color),
           (snapfunc(x), snapfunc(y)))
  
class Platformer(App):
   def __init__(self):
       super().__init__()
       self.p = None
       self.pos = (0,0)
       self.listenKeyEvent("keydown", "b", self.newWall)
       self.listenKeyEvent("keydown", "s", self.newPlayer)
       self.listenKeyEvent("keydown", "j", self.newSpring)
       self.listenKeyEvent("keydown", "p", self.newFloor)
       self.listenKeyEvent("keydown", "g", self.newGoal)
       self.listenKeyEvent("keydown", "left arrow", self.moveKey)
       self.listenKeyEvent("keydown", "right arrow", self.moveKey)
       self.listenKeyEvent("keydown", "up arrow", self.moveKey)
       self.listenKeyEvent("keyup", "left arrow", self.stopMoveKey)
       self.listenKeyEvent("keyup", "right arrow", self.stopMoveKey)
       self.listenKeyEvent("keyup", "up arrow", self.stopMoveKey)
       self.listenMouseEvent("mousemove", self.moveMouse)
       self.FallingSprings = []
       self.KillList = []



   def moveMouse(self, event):
       self.pos = (event.x, event.y)
  
   def newWall(self, event):
       Wall(self.pos[0], self.pos[1])
      
   def newPlayer(self, event):
       for p in Platformer.getSpritesbyClass(Player):
           p.destroy()
           self.p = None
       self.p = Player(self.pos[0], self.pos[1], self)
  
   def newSpring(self, event):
       self.FallingSprings.append(Spring(self.pos[0], self.pos[1], self))
  
   def newFloor(self, event):
       Platform(self.pos[0], self.pos[1])
      
   def newGoal(self, event):
       Goal(self.pos[0], self.pos[1])
      
   def moveKey(self, event):
       if self.p:
           self.p.move(event.key)
      
   def stopMoveKey(self, event):
       if self.p:
           self.p.stopMove(event.key)
      
   def step(self):
       if self.p:
           self.p.step()
       for s in self.FallingSprings:
           s.step()
       for k in self.KillList:
           k.destroy()
       self.KillList = []
          
   def killMe(self, obj):
       if obj in self.FallingSprings:
           self.FallingSprings.remove(obj)
       elif obj == self.p:
           self.p = None
       if not obj in self.KillList:
           self.KillList.append(obj)
      
print("Use your cursor to aim where you want to place the following")
print("Hit s to spawn a sprite")
print("Hit b to create a block")
print("Hit j to create a jump pad")
print("Hit p to create a platform")
print("Hit g to create a goal")
print("Use the left, right, and up arrow to move around")
print("Leave the cursor over where you want to spawn after you've designed your level so if you fail you can jsut hit s to start over from the original spawn point you used")
      
app = Platformer()
app.run()





