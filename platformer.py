"""
platformer.py
Author: Jasper Meyer
Credit: You, the internet, Brendan
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""


from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
black = Color(0, 1)
backcol = Color(0xd9ffcc, 1.0)
purp = Color(0x9900cc, 1.0)
noline = LineStyle(0, black)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, backcol)
bg = Sprite(bg_asset, (0,0))
thinline = LineStyle(1, black)
sq = RectangleAsset (75,75, noline, black)
wub=0
pup=0
mousex=0
mousey=0
mousexround=0
mouseyround=0
play = RectangleAsset (25,50, noline, purp)
vy=0
player=0
acc = 0
ti = 0
rupx=0
vx=0

def wup(event):
    global wub
    global mousexround
    global mouseyround
    wub = 1
    if wub == 1:
        mousexround=mousex-((mousex)%75)
        mouseyround=mousey-((mousey)%75)
        block = Sprite (sq, (mousexround, mouseyround))

def mousemo(event):
    global mousex
    global mousey
    mousex=event.x
    mousey=event.y
    

def pup(event):
    global pub
    global mousex
    global mouseyround
    global player
    pub = 1
    if pub == 1:
        mouseyround=mousey-((mousey)%75)+25
        if player == 0:
            player = Sprite (play, (mousex, mouseyround))


def rup(event):
    global rupx
    rupx=1
    

def step():
    if player != 0:
        global vy
        global acc
        global ti
        global rupx
        global vx
        acc = 0.02
        vy = 0.2*ti
        ti=ti+.1
        player.y=player.y+vy
        player.x=player.x+vx
        if rupx == 1:
            vx = vx+0.1
        
            
        




    






















myapp.listenKeyEvent('keyup', 'right arrow', rup)
myapp.listenKeyEvent('keyup', 'p', pup)
myapp.listenKeyEvent('keyup', 'w', wup)
myapp.listenMouseEvent('mousemove', mousemo)

myapp.run(step)