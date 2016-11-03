"""
platformer.py
Author: Andy Kotz
Credit: milo
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""

from ggame import App, RectangleAsset, Sprite
from ggame import LineStyle, Color

black = Color(0x000000, 1.0)
green = Color(0x00ff00, 1.0)
white = Color(0xFFFFFF, 1.0)

thinline = LineStyle(1, black)
wallplace = RectangleAsset(25, 25, thinline, black)

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240


listxs= list(range(1, 65))
listx = []
for i in listxs:
    x = i*25
    listx.append(x)
listys= list(range(1, 49))
listy = []
for j in listys:
    y = 25*j
    listy.append(y)

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
    
    
def mouseClick(event):
    numclickx = event.x
    numclicky = event.y
    xcoord = closestx(listx, numclickx)
    ycoord = closesty(listy, numclicky)
    Sprite (wallplace, (xcoord, ycoord))
    print (str(event.x) + " = mouseclickX")
    print (str(event.y) + " = mouseclickY")
    print (closestx(listx, event.x))
    print (closesty(listy, event.y))

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenMouseEvent('click', mouseClick)

myapp.run()