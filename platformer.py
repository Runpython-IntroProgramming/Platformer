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

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


listx= list(range(128))
for i in listx:
    i = 5*i
for i in listx:
    print(i)
listy= list(range(96))
for j in listy:
    j = 5*j


def closest(mylist, mynum):
    myestimation=[]
    myestimationordered=[]
    myvar=0
    while myvar < len(mylist):
        myestimation.append(mylist[myvar]-mynum)
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
    lowestpos = myestimationordered[0]
    lowestneg = myestneg[(len(myestneg)-1)]
    ln=lowestneg
    lp=lowestpos
    if abs(ln)<abs(lp):
        final=ln
    elif abs(lp)<abs(ln):
        final=lp
    final = final + mynum
    return(final)
    
    
"""
def reverse(b):
    b.dir *= -1
    pop.play()

# Set up function for handling screen refresh
def step():
    if ball.go:
        ball.x += ball.dir
        if ball.x + ball.width > SCREEN_WIDTH or ball.x < 0:
            ball.x -= ball.dir
            reverse(ball)

# Handle the space key
def spaceKey(event):
    ball.go = not ball.go

# Handle the "reverse" key
def reverseKey(event):
    reverse(ball)

# Handle the mouse click
def mouseClick(event):
    
    ball.x = closest(listx, event.x)
    ball.y = closest(listy, event.y)
    pew1.play()

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
# Set up event handlers for the app
myapp.listenKeyEvent('keydown', 'space', spaceKey)
myapp.listenKeyEvent('keydown', 'r', reverseKey)
myapp.listenMouseEvent('click', mouseClick)

myapp.run(step)


