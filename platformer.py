"""
platformer.py
Author: Jasper Meyer
Credit: Will, you, the internet, Brendan
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
sq = RectangleAsset (50, 20, thinline, black)

while 'w' is pressed:
    
    if mouse is at (0>=x>=50) and (0>=y>=50):
        Sprite (sq, (25, 25))
    if mouse is at (0>=x>=50) and (50>=y>=100):
        Sprite (sq, (25, 75))

































myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()