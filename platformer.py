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

SCREEN_WIDTH = 1750
SCREEN_HEIGHT = 980

black = Color(0x000000, 1.0)
green = Color(0x00ff00, 1.0)
white = Color(0xFFFFFF, 1.0)

thinline = LineStyle(1, black)
noline = lineStyle(0, green)
wallplace = RectangleAsset(35, 35, thinline, black)
bungo = RectangleAsset(17, 35, noline, green)

#select mode
for i in range(1):    
    mode = "w"
    def wallPlaceMode(event):
        mode = "w"
    def bungoMode(event):
        mode = "b"
    def thraxonMode(event):
        mode = "t"
    def jumpyMode(event):
        mode = "j"

#place wall sprites & snap to grid
for j in range(1):
    #make lists
    for i in range(1):
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
    def closesty(listx, numclicky):
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
    
    #make wall sprites   
    def mouseClick(event):
        numclickx = event.x-25
        numclicky = event.y-25
        xcoord = closestx(listx, numclickx)
        ycoord = closesty(listy, numclicky)
        Sprite (wallplace, (xcoord, ycoord))
        print (str(event.x) + " = mouseclickX")
        print (str(event.y) + " = mouseclickY")
        print (closestx(listx, event.x))
        print (closesty(listy, event.y))

#place bungo
for i in range(1):
    if 

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenMouseEvent('click', mouseClick)
myapp.listenKeyEvent('keydown', 'r', wallPlaceMode)
myapp.listenKeyEvent('keydown', 'b', bungoMode)
myapp.listenKeyEvent('keydown', 't', thraxonMode)
myapp.listenKeyEvent('keydown', 'j', jumpyMode)
myapp.listenKeyEvent('keydown', 'm', maloogMode)


myapp.run()