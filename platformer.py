"""
platformer.py
Author: Andy Kotz
Credit: milo, kezar
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""

from ggame import App, RectangleAsset, Sprite
from ggame import LineStyle, Color

SCREEN_WIDTH = 1015
SCREEN_HEIGHT = 700

#define colors and sprites
for i in range(1):
    black = Color(0x000000, 1.0)
    green = Color(0x00ff00, 1.0)
    white = Color(0xFFFFFF, 1.0)
    blue = Color(0x5D5DFF, 1.0)
    red = Color(0xff0000, 1.0)
    noline = LineStyle(0, black)
    
    wallplace = RectangleAsset(35, 35, noline, black)
    bungosprite = RectangleAsset(17, 33, noline, green)
    jumpy = RectangleAsset(18, 3, noline, blue)
    bottomof = RectangleAsset(1015, 1, noline, black)
    sideof = RectangleAsset(1, 700, noline, black)
    Sprite (bottomof, (0, 0))
    Sprite (bottomof, (0, 699))
    Sprite (sideof, (0, 0))
    Sprite (sideof, (1014, 0))
    
    class Wall(Sprite):
        def __init__(self, position):
            super().__init__(wallplace, position)
    class Jumpy(Sprite):
        def __init__(self, position):
            super().__init__(jumpy, position)
            self.vertvel = 20
    class Bungo(Sprite):
        def __init__(self, position):
            super().__init__(bungosprite, position)

#select mode
for i in range(1):    
    mode = "w"
    def wallPlaceKey(event):
        global mode
        mode = "w"
    def bungoKey(event):
        global mode
        mode = "b"
    def jumpyKey(event):
        global mode
        mode = "j"

#define arrow key movements
for p in range(1):
    jump = 0
    vertvel = 0
    latmove = 0
    def leftgo(event):
        global latmove
        latmove = -1
    def leftstop(event):
        global latmove
        latmove = 0
    def jumpgo(event):
        global jump
        global vertvel
        if jump == 0 or jump == 1:
            vertvel = 8
        jump += 1
    def rightgo(event):
        global latmove
        latmove = 1
    def rightstop(event):
        global latmove
        latmove = 0

#snap to grid
for p in range(1):
    listxs= list(range(1, 129))
    listx = []
    for i in listxs:
        x = i*35
        listx.append(x)
    listys= list(range(1, 97))
    listy = []
    for j in listys:
        y = 35*j
        listy.append(y)

    #make closest functions
    def closestx(listx, numclickx):
        myestimation=[]
        myestimationordered=[]
        myvar=0
        while myvar < len(listx):
            myestimation.append(listx[myvar]-numclickx)
            myvar+=1
        myvar=0
        myestimationordered = myestimation
        myestneg=[]
        for i in myestimationordered:
            if i<=0:
                myestneg.append(i)
        for j in range(10):
            for i in myestimationordered:
                if i<=0:
                    myestimationordered.remove(i)
        if len(myestimationordered) > 0 and len(myestneg) > 0:
            lp = myestimationordered[0]
            ln = myestneg[len(myestneg)-1]
            if abs(ln)<abs(lp):
                final=ln
            elif abs(lp)<abs(ln):
                final=lp    
        elif len(myestimationordered) > 0:
            lowestpos = myestimationordered[0]
            final=lowestpos
        elif len(myestneg) >0:
            lowestneg = myestneg[(len(myestneg)-1)]
            final=lowestneg
        final = final + numclickx
        return (final)
    def closesty(listy, numclicky):
        myestimation=[]
        myestimationordered=[]
        myvar=0
        while myvar < len(listy):
            myestimation.append(listy[myvar]-numclicky)
            myvar+=1
        myvar=0
        myestimationordered = myestimation
        myestneg=[]
        for i in myestimationordered:
            if i<=0:
                myestneg.append(i)
        for j in range(10):
            for i in myestimationordered:
                if i<=0:
                    myestimationordered.remove(i)
        if len(myestimationordered) > 0 and len(myestneg) > 0:
            lp = myestimationordered[0]
            ln = myestneg[len(myestneg)-1]
            if abs(ln)<abs(lp):
                final=ln
            elif abs(lp)<abs(ln):
                final=lp    
        elif len(myestimationordered) > 0:
            lowestpos = myestimationordered[0]
            final=lowestpos
        elif len(myestneg) >0:
            lowestneg = myestneg[(len(myestneg)-1)]
            final=lowestneg
        final = final + numclicky
        return (final)
    
#make all sprites
bungothere = 'false'
bungo = None
bouncy = None
endzone = None
def mouseClick(event):
    global endzone
    global bungo
    global bungothere
    global bouncy
    numclickx = event.x-25
    numclicky = event.y-25
    if mode == "b" and bungo == None:
        bungo = Bungo((numclickx, numclicky))
    if mode == "w":
        xcoord = closestx(listx, numclickx)
        ycoord = closesty(listy, numclicky)
        wall = Wall((xcoord, ycoord))
    if mode == "j":
        bouncy = Jumpy ((numclickx+8, numclicky+15))


#movement
posendtickx = 0
posendticky = 0
def step():
    jum = 0
    global vertvel
    global latmove
    global bungo
    global bouncy
    global posendtickx
    global posendticky
    global jump
    global jum
    if bouncy != None:
        bouncy.y += bouncy.vertvel
        bouncycollision = bouncy.collidingWithSprites(Wall)
        if bouncycollision != [] or bouncy.y >= 695:
            bouncy.vertvel = 0
            bouncy.y = closesty(listy, bouncy.y)-3
    if bungo != None:
        posendticky = bungo.y
        posendtickx = bungo.x
    if bungo != None:
        bungo.y -= vertvel
        vertvel -= 0.2
        if vertvel <= -8:
            vertvel = -8
        bungo.x += 3*latmove
        if bouncy != None:
            bouncyjump = bungo.collidingWithSprites(Jumpy)
            if bouncyjump != []:
                vertvel = 10
                jump = 1
    if bungo != None:
        collision = bungo.collidingWithSprites(Wall)
        if collision != []:
            jump = 0
            while jum <= len(collision)-1:
                if bungo.y >= collision[jum].y-35 and bungo.y <= collision[jum].y+35:
                    if bungo.x >= collision[jum].x-35 and bungo.x <= collision[jum].x+35:
                        bungo.y = posendticky
                        vertvel = 0
                if bungo.x >= collision[jum].x-35 and bungo.x <= collision[jum].x+35:
                    if bungo.y >= collision[jum].y-35 and bungo.y <= collision[jum].y+35:
                        bungo.x = posendtickx
                jum += 1
        if bungo.y >= 667:
            bungo.y = posendticky
            jump = 0
        if bungo.y <= 0:
            vertvel = 0
            bungo.y = posendticky
        if bungo.x >= 998 or bungo.x <= 0:
            bungo.x = posendtickx


#app stuff
for j in range(1):
    myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
    myapp.listenMouseEvent('click', mouseClick)
    myapp.listenKeyEvent('keydown', 'w', wallPlaceKey)
    myapp.listenKeyEvent('keydown', 'b', bungoKey)
    myapp.listenKeyEvent('keydown', 'j', jumpyKey)
    myapp.listenKeyEvent('keydown', 'up arrow', jumpgo)
    myapp.listenKeyEvent('keydown', 'left arrow', leftgo)
    myapp.listenKeyEvent('keydown', 'right arrow', rightgo)
    myapp.listenKeyEvent('keyup', 'right arrow', rightstop)
    myapp.listenKeyEvent('keyup', 'left arrow', leftstop)

    myapp.run(step)
