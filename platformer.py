"""
platformer.py
Author: Nick lee
Credit: ggame documentation, Mr. Dennison, original platormer example
Assignment: Level 3 project
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""


from ggame import (App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset,  
    EllipseAsset, PolygonAsset, ImageAsset, Frame)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
sw = 0
sh = 0

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
bcolor = white
grid = RectangleAsset(40,40,gridline, bcolor)
class Character(Sprite):
    Box = RectangleAsset(15, 35, noline, green)
    def __init__(self, position):
        super().__init__(Character.Box, position)
        global sh, sw
        Platformer.charon = 1
        self.bcollide = 0
        self.tcollide = 0
        self.vx = 0
        self.vy = 0
        self.keydown = 0
        self.inair = 0
        
        Platformer.listenKeyEvent("keydown", "right arrow", self.checkmove)
        Platformer.listenKeyEvent("keydown", "left arrow", self.checkmove)
        Platformer.listenKeyEvent("keydown", "up arrow", self.checkmove)
        Platformer.listenKeyEvent("keyup", "right arrow", self.stop)
        Platformer.listenKeyEvent("keyup", "left arrow", self.stop)
        Platformer.listenKeyEvent("keyup", "up arrow", self.stop)

    def step(self, h):
        self.x += self.vx
        self.y += self.vy
        
        self.bcollide = self.collidingWithSprites(Block)
        self.tcollide = self.collidingWithSprites(top)
        self.scollide = self.collidingWithSprites(spring)
        if self.y > h :
            Platformer.charon = 0
            self.destroy()

        if len(self.bcollide):
            self.x -= self.vx
            self.vx = 0 
            
        if len(self.scollide):
            self.vy = -16
            #self.inair += 1

        if len(self.tcollide):
            if len(self.scollide) == 0:
                self.y -= self.vy
                self.vy = 0
            
            self.inair = 0
        else:
            self.vy += 0.9

    def checkmove(self, event):
        if len(self.bcollide) == 0:
            if event.key == "right arrow":
                self.vx = 3
            if event.key == "left arrow":
                self.vx = -3
        if event.key == "up arrow":
            if self.inair == 0:
                self.vy = -11
                self.inair += 1
        
    def stop(self, event):
        self.keydown = 0
        self.vx = 0

class spring(Sprite):
    assign = 0
    s = RectangleAsset(15,5,noline,red)
    def __init__(self, position):
        super().__init__(spring.s, position)
        self.falling = 1
        Platformer.springnum += 1
        self.num = Platformer.springnum
        #print(Platformer.springnum)
        #self.assign
        self.listi = []
        self.vy = 0
        #print(self.num)
        
    def step(self, h):
        self.y += self.vy
        self.stopcollide = self.collidingWithSprites(top)
        if len(self.stopcollide):
            self.y -= self.vy
            self.vy = self.vy/2
            self.falling = 0
            if self.vy < 0.1:
                for i in range(len(Platformer.alive)):
                    self.t = Platformer.alive[i-1]
                    if self.num == self.t[1]:
                        del Platformer.alive[i-1]
        else:
            if self.vy < 5:
                self.vy += 0.98

        if self.y > h:
            for i in range(len(Platformer.alive)):
                self.t = Platformer.alive[i-1]
                if self.num == self.t[1]:
                    del Platformer.alive[i-1]
        
    def delself(self, event):
        print('a')
        for i in range(len(Platformer.alive)):
            self.listi = Platformer.alive[i]
            self.listi = self.list[1]
            if self.num == self.listi:
                del Platformer.alive[i]
                print(self.listi, self.num)

class top(Sprite):
    r =  RectangleAsset(39,10,noline,black)
    def __init__(self, position):
        super().__init__(top.r, position)
        die = self.collidingWithSprites(top)
        if len(die):
            self.destroy()

class Block(Sprite):
    cube = (RectangleAsset(39, 20, noline, black))
    
    def __init__(self, position):
        super().__init__(Block.cube,position)
        global grey, black, bcolor
        die = self.collidingWithSprites(Block)
        if len(die):
            self.destroy()

class Platformer(App):
    alive = []
    springnum = 0
    go = 0
    charon = 0
    noline = LineStyle(0, grey)
    def __init__(self):
        super().__init__()
        global black, white, grey, bcolor, sw, sh
        Character.alive2 = 0
        springfall = 1
        mxp = 0
        myp = 0
        mx = 0
        my = 0
        bg_asset = RectangleAsset(self.width, self.height, noline, white)
        bg = Sprite(bg_asset, (0,0))
        Platformer.listenKeyEvent("keydown", "w", self.placeblock)
        Platformer.listenKeyEvent("keydown", "p", self.placeuser)
        Platformer.listenKeyEvent("keydown", "s", self.placespring)
        Platformer.listenMouseEvent("mousemove", self.getmousepos)

    def getmousepos(self,event):
        self.mx = event.x
        self.my = event.y
        self.mxp = round((event.x-20)/40)
        self.myp = round((event.y-20)/40)
        self.mousepos = (self.mxp, self.myp)
    
    def placeblock(self, event):
        Block((((self.mxp*40)),((self.myp*40)+9)))
        top((self.mxp*40, self.myp*40))
        top((self.mxp*40, self.myp*40 + 29))

    def placeuser(self, event):
        if Platformer.charon == 0:
            Character(((self.mxp*40),(self.myp*40)))
            self.charon = 0
    
    def placespring(self, event):
        
        self.alive.append([spring((self.mx, self.my)), self.springnum])
        self.springnum += 1
        #spring.assign = self.springnum

    def step(self):
        sw = self.width
        sh = self.height
        for Box in self.getSpritesbyClass(Character):
            Box.step(sh)
        
        for i in self.alive:
            i[0].step(sh)
                
myapp = Platformer()
myapp.run()












