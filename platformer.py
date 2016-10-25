"""
platformer.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
# THIS IS BOXY
class Boxy(Sprite):
    #THIS IS BOXY'S WORLD
class Platformer(App):
    
    def __init__(self, width, height):
        super().__init__(width, height)
        black=Color(1, 0)
        Black=Color(0, 1)
        blue=Color(0x0000ff, 1.0)
        noline=LineStyle(5, Black)
        Noline=LineStyle(0, Black)
        bg_asset=RectangleAsset(width, height, noline, black)
        bg=Sprite(bg_asset, (0, 0))
       
    
    
    
    
myapp = Platformer(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()