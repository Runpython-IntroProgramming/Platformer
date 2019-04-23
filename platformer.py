"""
platformer.py
Author: 
Credit: 
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame

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

# Exemplar implementation of the Platformer Project
# (c) 2018 E. Dennison
# See: https://github.com/BrythonServer/Platformer

from ggame import App, Sprite, RectangleAsset, LineStyle, Color
   
# A super wall class for wall-ish behaviors
class GenericWall(Sprite):
    def __init__(self, x, y, w, h, color):
        snapfunc = lambda X : X - X % w
        super().__init__(
            RectangleAsset(w-1,h-1,LineStyle(0,Color(0, 1.0)), color),
            (snapfunc(x), snapfunc(y)))
        # destroy any overlapping walls
        collideswith = self.collidingWithSprites(type(self))
        if len(collideswith):
            collideswith[0].destroy()

# impenetrable wall (black)
class Wall(GenericWall):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50, Color(0, 1.0))

# pass thru going up wall
class Platform(GenericWall):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 15, Color(0xff0000, 1.0))
    
# super class for anything that falls and lands or bumps into walls
class GravityActor(Sprite):
    def __init__(self, asset, x, y, app):
        self.vx = self.vy = 0
        self.stuck = False
        self.app = app                          # app, need to know
        self.resting = False                    # whether resting on wall
        super().__init__(asset,(x, y)) 
        # destroy self if overlapping with anything
        #collideswith = self.collidingWithSprites()
        #if len(collideswith):
        #    self.destroy()
        
    def step(self):
        # process movement in horizontal direction first
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
        # process movement in vertical direction second
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
                # upward collisions for true Wall only
                elif isinstance(collider, Wall):
                    pass
                    #self.y = collider.y + collider.height
                    #self.vy = 0
        # adjust vertical velocity for acceleration due to gravity
        self.vy += 1
        # check for out of bounds
        if self.y > self.app.height:
            self.app.killMe(self)

# "bullets" to fire from Turrets.
class Bolt(Sprite):
    def __init__(self, direction, x, y, app):
        asset = ImageAsset("dn copy 2.png")
        self.direction = direction
        self.app = app
        super().__init__(asset, (x,y))

    def step(self):
        self.x += self.direction
        # check for out of bounds
        if self.x > self.app.width or self.x < 0:
            self.app.killMe(self)
        # check for any collisions
        hits = self.collidingWithSprites()
        selfdestruct = False
        for target in hits:
            # destroy players and other bolts
            if isinstance(target, Player) or isinstance(target, Bolt):
                self.app.killMe(target)
            # self destruct on anything but a Turret
            if not isinstance(target, Turret):
                selfdestruct = True
        if selfdestruct:
            self.app.killMe(self)


# An object that generates bolts (laser shots)
class Turret(GravityActor):
    def __init__(self, x, y, app):
        asset = ImageAsset("doughnut-transparent-stacked-9.png")
        self.time = 0
        self.direction = 1
        super().__init__(asset, x, y, app)
        
    def step(self):
        super().step()
        self.time += 1
        if self.time % 100 == 0:
            Bolt(self.direction, 
                 self.x+self.width//2,
                 self.y+10,
                 self.app)
            self.direction *= -1

        

# The player class. only one instance of this is allowed.
class Player(GravityActor):
    def __init__(self, x, y, app):
        w = 15
        h = 30
        asset = ImageAsset("ox7pesyc2oi01 copy.png")
        super().__init__(asset, x, y, app)

    def step(self):
        # look for spring collisions
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

  
# A spring makes the player "bounce" higher than she can jump
class Spring(GravityActor):
    def __init__(self, x, y, app):
        w = 10
        h = 4
        asset = ImageAsset("20150207151848!Trampoline-2 copy 4.png",Frame(17,62,161,66))
        super().__init__(asset, x, y, app)
        self.scale = 0.3
        
    def step(self):
        if self.resting:
            self.app.FallingSprings.remove(self)
        super().step()

# The application class. Subclass of App
class Platformer(App):
    def __init__(self):
        super().__init__()
        self.p = None
        self.pos = (0,0)
        self.listenKeyEvent("keydown", "w", self.newWall)
        self.listenKeyEvent("keydown", "p", self.newPlayer)
        self.listenKeyEvent("keydown", "s", self.newSpring)
        self.listenKeyEvent("keydown", "f", self.newFloor)
        self.listenKeyEvent("keydown", "l", self.newLaser)
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
        
    def newLaser(self, event):
        Turret(self.pos[0], self.pos[1], self)
        
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
        for t in Platformer.getSpritesbyClass(Turret):
            t.step()
        for b in Platformer.getSpritesbyClass(Bolt):
            b.step()
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
        
# Display some hints about how to play!
print("Move your mouse cursor around the graphics screen and:")
print("w: create a wall block")
print("s: create a spring")
print("f: create a floor")
print("l: create a laser turret")
print("p: create a player")
print("left, right, up arrow: control player movement")
        
# Execute the application by instantiate and run        
app = Platformer()
app.run()