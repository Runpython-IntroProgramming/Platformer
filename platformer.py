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

SCREEN_WIDTH = 1715
SCREEN_HEIGHT = 980

#define colors and sprites
for i in range(1):
    black = Color(0x000000, 1.0)
    green = Color(0x00ff00, 1.0)
    white = Color(0xFFFFFF, 1.0)
    blue = Color(0x5D5DFF, 1.0)
    red = Color(0xff0000, 1.0)
    noline = LineStyle(0, black)
    
    wallplace = RectangleAsset(35, 35, noline, black)
    bungosprite = RectangleAsset(17, 35, noline, green)
    jumpy = RectangleAsset(18, 3, noline, blue)
    
    class Wall(Sprite):
        def __init__(self, position):
            super().__init__(wallplace, position)
    class Jumpy(Sprite):
        def __init__(self, position):
            super().__init__(jumpy, position)
            self.vertvel = 3
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
    """
    def shooterKey(event):
        global mode
        mode = "s"
    def killerKey(event):
        global mode
        mode = "k"
    def platformKey(event):
        global mode
        mode = "p"
    """

#define arrow key movements
stopmo = False
for p in range(1):
    vertvel = 0
    latmove = 0
    jump = "false"
    def leftgo(event):
        global latmove
        latmove = -1
    def leftstop(event):
        global latmove
        latmove = 0
    def jumpgo(event):
        global vertvel
        vertvel = 7
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
        print (final)
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
        print(final)
    
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
    global vertvel
    global latmove
    global bungo
    global bouncy
    global posendtickx
    global posendticky
    if bungo != None:
        collision = bungo.collidingWithSprites(Wall)
        if collision != []:
            bungo.x = posendtickx
            bungo.y = posendticky
            print (posendtickx + "," + posendticky)
    if bouncy != None:
        bouncy.y += bouncy.vertvel
        bouncycollision = bouncy.collidingWithSprites(Wall)
        if bouncycollision != []:
            bouncy.vertvel = 0
            ycoordbouncy = closesty(listy, bouncy.y)
            bouncy.y = ycoordbouncy-3
    if bungo != None:
        bungo.y -= vertvel
        vertvel -= 0.2
        if vertvel <= -9:
            vertvel = -9
        bungo.x += 3*latmove
        if bouncy != None:
            bouncyjump = bungo.collidingWithSprites(Jumpy)
            if bouncyjump != []:
                vertvel = 10
    if bungo != None:
        posendtickx = bungo.x
        posendticky = bungo.y

    



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
    """
    myapp.listenKeyEvent('keydown', 's', shooterKey)
    myapp.listenKeyEvent('keydown', 'k', killerKey)
    myapp.listenKeyEvent('keydown', 'p', platformKey)
    """
    
    myapp.run(step)
    
   
   
    