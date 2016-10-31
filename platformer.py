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

black = Color(0x000000, 1)
green = Color(0x00ff00, 1)
white = Color(0xFFFFFF, 1)

thinline = LineStyle(1, black)
wallplace = RectangleAsset(5, 5, thinline, black)

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240


listx= list(range(64))
for i in listx:
    i = i+1
    i = i*5
    print (i)
listy= list(range(48))
for j in listy:
    j = j+1
    j = 5*j


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
    #lowestpos = myestimationordered[0]
    lowestneg = myestneg[(len(myestneg)-1)]
    ln=lowestneg
    #lp=lowestpos
    #if abs(ln)<abs(lp):
    final=ln
    #elif abs(lp)<abs(ln):
        #final=lp
    final = final + numclickx
    return(final)
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
    #lowestpos = myestimationordered[0]
    lowestneg = myestneg[(len(myestneg)-1)]
    ln=lowestneg
    #lp=lowestpos
    #if abs(ln)<abs(lp):
    final=ln
    #elif abs(lp)<abs(ln):
        #final=lp
    final = final + numclicky
    return(final)
    
def mouseClick(event):
    numclickx = event.x
    numclicky = event.y
    xcoord = closestx(listx, numclickx)
    ycoord = closesty(listy, numclicky)
    Sprite (wallplace, (xcoord, ycoord))
    print (event.x)
    print (event.y)
    print (closestx(listx, event.x))

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.listenMouseEvent('click', mouseClick)

myapp.run


