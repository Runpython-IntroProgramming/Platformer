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
play = RectangleAsset (75,75, noline, purp)

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
    global mousexround
    global mouseyround
    pub = 1
    if pub == 1:
        mousexround=mousex-((mousex)%75)
        mouseyround=mousey-((mousey)%75)
        block = Sprite (sq, (mousexround, mouseyround))



    






























myapp.listenKeyEvent('keyup', 'p', pup)
myapp.listenKeyEvent('keyup', 'w', wup)
myapp.listenMouseEvent('mousemove', mousemo)

myapp.run()