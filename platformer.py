"""
platformer.py
Author: Nick lee
Credit: ggame documentation, Mr. Dennison, original platormer example (nothing copied and pasted)
Assignment: Level 3 project
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""


from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
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

#keys = ['up arrow', 'down arrow', 'right arrow', 'left arrow']
        
class Character(Sprite):
    Box = RectangleAsset(15, 25, noline, blue)
    def __init__(self, position):
        super().__init__(Character.Box, position)
        global sh, sw
        self.vx = 0
        self.vy = 0
        self.keydown = 0
        self.inair = 0
        
        '''
        Platformer.listenKeyEvent("keyup", "up arrow", self.stop)
        Platformer.listenKeyEvent("keydown", "up arrow", self.up)
        Platformer.listenKeyEvent("keyup", "right arrow", self.stop)
        Platformer.listenKeyEvent("keydown", "right arrow", self.right)
        Platformer.listenKeyEvent("keyup", "left arrow", self.stop)
        Platformer.listenKeyEvent("keydown", "left arrow", self.left)
        Platformer.listenMouseEvent("mousedown", self.yeet)
        '''
        Platformer.listenKeyEvent("keydown", "right arrow", self.checkmove)
        Platformer.listenKeyEvent("keydown", "left arrow", self.checkmove)
        Platformer.listenKeyEvent("keydown", "up arrow", self.checkmove)
        Platformer.listenKeyEvent("keyup", "right arrow", self.stop)
        Platformer.listenKeyEvent("keyup", "left arrow", self.stop)
        Platformer.listenKeyEvent("keyup", "up arrow", self.stop)

    def step(self, h):
        self.x += self.vx
        self.y += self.vy
        bcollide = self.collidingWithSprites(Block)
        tcollide = self.collidingWithSprites(top)    
        
        if self.y > h :
            self.destroy()

        if len(bcollide):
            self.vx = 0 
            self.vy = 0
            self.x += self.vx*2
            self.y += self.vy*2

        if len(tcollide):
            self.y -= self.vy
            self.vy = 0
            self.inair = 0
        else:
            self.vy += 0.9

    def checkmove(self, event):
        if event.key == "right arrow":
            self.vx = 3
        if event.key == "left arrow":
            self.vx = -3
        if event.key == "up arrow":
            if self.inair < 2:
                self.vy = -10
                self.inair += 1
        
    def stop(self, event):
        self.keydown = 0
        self.vx = 0
    
    def yeet(self, event):
        epos = round(round(event.x)/40),round(round(event.y)/40)
"""
class Plainwall(Sprite):
    def __init__(self, x, y, color):
        super().__init__(
            RectangleAsset(39, 39, noline, color))
        # destroy any overlapping walls
        collideswith = self.collidingWithSprites(type(self))
        if len(collideswith):
            collideswith[0].destroy()  

class bsquare(Plainwall):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50, black)
"""
class spring(Sprite):
    s = RectangleAsset(15,2,noline,red)
    def __init__(self, position):
        super().__init__(spring.s, position)
        self.vy = 0
        '''
    def step(self, event):
        self.y += self.vy
        stopcollide = self.collidingWithSprites(Block)
        if len(stopcollide):
            self.vy = 0
            self.y += self.vy
        else:
            self.vy += 0.8
        '''
class top(Sprite):
    r =  RectangleAsset(39,10,noline,white)
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
    noline = LineStyle(0, grey)
    def __init__(self):
        super().__init__()
        global black, white, grey, bcolor, sw, sh
        go = 0
        mxp = 0
        myp = 0
        mx = 0
        my = 0
        bg_asset = RectangleAsset(self.width, self.height, noline, grey)
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
        Character(((self.mxp*40),(self.myp*40)))
    
    def placespring(self, event):
        spring((self.mx, self.my))
    def step(self):
        sw = self.width
        sh = self.height
        for Box in self.getSpritesbyClass(Character):
            Box.step(sh)
        for s in self.getSpritesbyClass(spring):
            s.step()

class SpaceGame(App):
    
    """
    Tutorial4 space game example.
    """
    def __init__(self):
        super().__init__()
        
        # Background
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(self.width, self.height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        SpaceShip((100,100))
        SpaceShip((150,150))
        SpaceShip((200,50))
        for i in range(0, (self.width/40)):
            Block(())
        
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()

myapp = Platformer()
myapp.run()












