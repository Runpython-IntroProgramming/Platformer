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

lightBlue = Color(0x2EFEC8, 1.0)
black = Color(0x000000, 1.0)
pink = Color(0xFF00FF, 1.0)
red = Color(0xFF5733, 1.0)
white = Color(0xFFFFFF, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
darkBlue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
grey = Color(0xC0C0C0, 1.0)

thinline = LineStyle(2, black)
blkline = LineStyle(1, black)
noline = LineStyle(0, white)
coolline = LineStyle(1, grey)
blueline = LineStyle(2, darkBlue)
redline = LineStyle(1, red)
greenline = LineStyle(1, green)
gridline = LineStyle(1, grey)
grid=RectangleAsset(30,30,gridline,white)


class Blocks(Sprite):
    def __init__(self, x, y, w, h, color):
        grid = lambda X : X - X % w
        super().__init__(
            RectangleAsset(w-1, h-1, LineStyle(0,Color(0, 1.0)), color),(grid(x), grid(y)))
        #collisions
        collisioncontra =self.collidingWithSprites(type(self))
        if len(collisioncontra):
            collisioncontra[0].destroy()

class Wall(Blocks):
    def __init__(self,x,y):
        super().__init__(x,y,60,60,grey)      #(self, x, y, w, h, color)

class MarioWall(Blocks):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 15, purple)
        
        
class Newton(Sprite):
    def __init__(self, x, y, width, height, color, app):
        self.vx = self.vy = 0
        self.stuck = False
        self.app = app                          
        self.resting = False                    
        super().__init__(
            RectangleAsset(
                width, height, 
                LineStyle(0, white),
                color),
            (x, y)) 
        
    def step(self):
        # process movement in horizontal direction first
        self.x += self.vx
        collides = self.collidingWithSprites(Wall)
        collides.extend(self.collidingWithSprites(MarioWall))
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
        collides.extend(self.collidingWithSprites(MarioWall))
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

class Playah(Newton):
    def __init__(self, x, y, app):
        w = 10 
        h = 20
        super().__init__(x-w//2, y-h//2, w, h, lightBlue, app)
        
    def step(self):
        Jumpers = self.collidingWithSprites(Jumper)    #interference with Jumpers
        if len(Jumpers):
            self.vy = -10    #y -- y positioning
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
            self.vy = -8
            self.resting = False
            
    def stopMove(self, key):
        if key == "left arrow" or key == "right arrow":
            if self.resting:
                self.vx = 0
                
class Pellets(Sprite):
    def __init__(self, direction, x, y, app):
        w = 15
        h = 5
        self.direction = direction
        self.app = app
        super().__init__(RectangleAsset(w, h, 
            LineStyle(0, Color(0, 1.0)),
            Color(0x00ffff, 1.0)),
            (x-w//2, y-h//2))

    def step(self):
        self.x += self.direction
        # check for out of bounds
        if self.x > self.app.width or self.x < 0:
            self.app.killMe(self)
        # check for any collisions
        hits = self.collidingWithSprites()
        selfdestruct = False
        for target in hits:
            # destroy players and other Pellets
            if isinstance(target, Playah) or isinstance(target, Pellets):
                self.app.killMe(target)
            # self destruct on anything but a Machina
            if not isinstance(target, Machina):
                selfdestruct = True
        if selfdestruct:
            self.app.killMe(self)
            
class Machina(Newton):
    def __init__(self, x, y, app):
        w = 20
        h = 35
        r = 10
        self.time = 0
        self.direction = 1
        super().__init__(x-w//2, y-h//2, w, h, Color(0xff8800, 1.0), app)
        
    def step(self):
        super().step()
        self.time += 1
        if self.time % 100 == 0:
            Pellets(self.direction, 
                 self.x+self.width//2,
                 self.y+10,
                 self.app)
            self.direction *= -1

class Jumper(Newton):
    def __init__(self, x, y, app):
        w = 10
        h = t
        super().__init__(x-w//2, y-h//2, w, h,green, app)
    def step(self):
        if self.resting:
            self.app.FallingJumpers.remove(self)
        super().step()

#Index/Glossarix
class Game(App):
    def __init__(self):
        super().__init__()
        self.p = None
        self.pos = (0,0)
        self.listenKeyEvent("keydown", "w", self.newWall)
        self.listenKeyEvent("keydown", "p", self.newPlayah)
        self.listenKeyEvent("keydown", "j", self.newJumper)
        self.listenKeyEvent("keydown", "m", self.newStepThrough)
        self.listenKeyEvent("keydown", "left arrow", self.moveKey)
        self.listenKeyEvent("keydown", "right arrow", self.moveKey)
        self.listenKeyEvent("keydown", "up arrow", self.moveKey)
        self.listenKeyEvent("keyup", "left arrow", self.stopMoveKey)
        self.listenKeyEvent("keyup", "right arrow", self.stopMoveKey)
        self.listenKeyEvent("keyup", "up arrow", self.stopMoveKey)
        self.listenMouseEvent("mousemove", self.moveMouse)
        self.FallingJumpers = []
        self.KillList = []
    def moveMouse(self, event):
        self.pos = (event.x, event.y)

    def newWall(self, event):
        Wall(self.pos[0], self.pos[1])

    def newPlayah(self, event):
        for p in Game.getSpritesbyClass(Playah):
            p.destroy()
            self.p = None
        self.p = Playah(self.pos[0], self.pos[1], self)
        
    def newJumper(self, event):
        self.FallingJumpers.append(Jumper(self.pos[0], self.pos[1], self))
        
    def newStepThrough(self, event):
        Game(self.pos[0], self.pos[1])   #tuple???

    def moveKey(self, event):
        if self.p:
            self.p.move(event.key)
        
    def stopMoveKey(self, event):
        if self.p:
            self.p.stopMove(event.key)

    #########           
    def step(self):
        if self.p:
            self.p.step()
        for s in self.FallingJumpers:
            s.step()
        for t in Game.getSpritesbyClass(Machina):
            t.step()
        for b in Game.getSpritesbyClass(Pellets):
            b.step()
        for k in self.KillList:
            k.destroy()
        self.KillList = []
    ##########
    
    def killMe(self, obj):
        if obj in self.FallingJumpers:
            self.FallingJumpers.remove(obj)
        elif obj == self.p:
            self.p = None
        if not obj in self.KillList:
            self.KillList.append(obj)

app = Game()
app.run()





