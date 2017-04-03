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

black = Color(0, 1)
backcol = Color(0xd9ffcc, 1.0)
noline = LineStyle(0, black)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, backcol)
bg = Sprite(bg_asset, (0,0))
thinline = LineStyle(1, black)
sq = RectangleAsset (50, 50, noline, black)
wub=0

def wup(event):
    global wub
    wub = 1


if wub == 1:
    block = Sprite (sq, mouse.x-((mouse.x)%50), mouse.y-((mouse.y)%50))
    






























#myapp.listenKeyEvent('keydown', 'p', pup)
myapp.listenKeyEvent('keydown', 'w', wup)
myapp.listenMouseEvent('move', mousemo)
myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()