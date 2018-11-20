"""
platformer.py
Author: Johari 
Credit: Meggie, Noah 
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
myapp = App()

from math import floor

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

blue = Color(0x2EFEC8, 1.0)
black = Color(0x000000, 1.0)
pink = Color(0xFF00FF, 1.0)
red = Color(0xFF5733, 1.0)
white = Color(0xFFFFFF, 1.0)
red = Color(0xffbaf0, 1.0)
green = Color(0x9cf5f0, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
grey = Color(0xC0C0C0, 1.0) 
purple = Color(0xc8beff, 1.0)

thinline = LineStyle(2, black)
blkline = LineStyle(1, black)
noline = LineStyle(0, white)
coolline = LineStyle(1, grey)
blueline = LineStyle(2, blue)
redline = LineStyle(1, red)
greenline = LineStyle(1, green)
gridline = LineStyle(1, grey)
grid=RectangleAsset(30,30,gridline,white)

class Wall(Sprite):
    
    asset = RectangleAsset(35, 35, thinline, red)

    def __init__(self, position):
        super().__init__(Wall.asset, position)

class Player(Sprite):
    
    asset = RectangleAsset(12, 28, thinline, purple)

    def __init__(self, position):
        self.vx = 0 
        self.vy = 0
        super().__init__(Player.asset, position)
        
class Spring(Sprite):
    
    asset = RectangleAsset(15, 5, thinline, blue)

    def __init__(self, position):
        self.vy = 0
        super().__init__(Spring.asset, position)
        
class Top(Sprite):
    asset = RectangleAsset(5, 3, thinline, purple)

    def __init__(self, position):
        self.vx = 0 
        self.vy = 0
        super().__init__(Top.asset, position)
        
class Bottom(Sprite):
    asset = RectangleAsset(5, 3, thinline, purple)

    def __init__(self, position):
        self.vx = 0 
        self.vy = 0
        super().__init__(Bottom.asset, position)
        
class Left(Sprite):
    asset = RectangleAsset(3, 5, thinline, purple)

    def __init__(self, position):
        self.vx = 0 
        self.vy = 0
        super().__init__(Left.asset, position)
class Right(Sprite): 
    asset = RectangleAsset(3, 5, thinline, purple)

    def __init__(self, position):
        self.vx = 0 
        self.vy = 0
        super().__init__(Right.asset, position)
class Platformer(App):
    
    def __init__(self):
        super().__init__()
        bg_asset = RectangleAsset(1000, 800, noline, green)
        bg = Sprite(bg_asset, (0,0))
        self.asset = [0,0] 
        Platformer.listenMouseEvent('mousemove', self.mouse) 
        Platformer.listenKeyEvent('keydown', 'w', self.wall)
        Platformer.listenKeyEvent('keydown', 's', self.spring)
        Platformer.listenKeyEvent('keydown', 'p', self.player)
        
        Platformer.listenKeyEvent('keydown', 'left arrow', self.lvelocity)
        Platformer.listenKeyEvent('keyup', 'left arrow', self.lvelocity2)
        Platformer.listenKeyEvent('keydown', 'right arrow', self.rvelocity)
        Platformer.listenKeyEvent('keyup', 'right arrow', self.rvelocity2)
        
        Platformer.listenKeyEvent('keydown', 'left arrow', self.lvelocityb)
        Platformer.listenKeyEvent('keyup', 'left arrow', self.lvelocity2b)
        Platformer.listenKeyEvent('keydown', 'right arrow', self.rvelocityb)
        Platformer.listenKeyEvent('keyup', 'right arrow', self.rvelocity2b)
        
        Platformer.listenKeyEvent('keydown', 'left arrow', self.lvelocityr)
        Platformer.listenKeyEvent('keyup', 'left arrow', self.lvelocity2r)
        Platformer.listenKeyEvent('keydown', 'right arrow', self.rvelocityr)
        Platformer.listenKeyEvent('keyup', 'right arrow', self.rvelocity2r)
        
        Platformer.listenKeyEvent('keydown', 'left arrow', self.lvelocityl)
        Platformer.listenKeyEvent('keyup', 'left arrow', self.lvelocity2l)
        Platformer.listenKeyEvent('keydown', 'right arrow', self.rvelocityl)
        Platformer.listenKeyEvent('keyup', 'right arrow', self.rvelocity2l)
        
        Platformer.listenKeyEvent('keydown', 'left arrow', self.lvelocityt)
        Platformer.listenKeyEvent('keyup', 'left arrow', self.lvelocity2t)
        Platformer.listenKeyEvent('keydown', 'right arrow', self.rvelocityt)
        Platformer.listenKeyEvent('keyup', 'right arrow', self.rvelocity2t)
        
        Platformer.listenKeyEvent('keydown', 'up arrow', self.jump)
        Platformer.listenKeyEvent('keyup', 'up arrow', self.jump2)
    
    def step(self):  
        
        for pplayer in self.getSpritesbyClass(Player):
            for left in self.getSpritesbyClass(Left):
                for right in self.getSpritesbyClass(Right):
                    for top in self.getSpritesbyClass(Top):
                        for bottom in self.getSpritesbyClass(Bottom):
                            if pplayer.y>1000:
                                pplayer.destroy()
                            
                            pplayer.x += pplayer.vx
                            pplayer.y += pplayer.vy
                            
                            m = 0
                            n = 0 
                            o = 0
                            p = 0
                            q = 0 
                            for wwall in self.getSpritesbyClass(Wall):
                                if left.collidingWith(wwall): 
                                    m+=1
                                if right.collidingWith(wwall): 
                                    q+=1
                                if top.collidingWith(wwall): 
                                    o+=1
                                if bottom.collidingWith(wwall): 
                                    p+=1
                        
                            if p > 0: 
                               pplayer.vy=0
                            else:
                                pplayer.vy = pplayer.vy +.6
                            n=0
                            for sspring in self.getSpritesbyClass(Spring):
                                if pplayer.collidingWith(sspring): 
                                    n+=1
                            if n > 0: 
                               pplayer.vy=  -10
                            else:
                                pplayer.vy = pplayer.vy
                        
                        for right in self.getSpritesbyClass(Right):
                            if right.y>1000:
                                right.destroy()
                            right.x += right.vx
                            right.y += right.vy
                            
                        for left in self.getSpritesbyClass(Left):
                            if left.y>1000:
                                left.destroy()
                            left.x += left.vx
                            left.y += left.vy
                            
                        for top in self.getSpritesbyClass(Top):
                            if top.y>1000:
                                top.destroy()
                            top.x += top.vx
                            top.y += top.vy
                            
                        for bottom in self.getSpritesbyClass(Bottom):
                            if bottom.y>1000:
                                bottom.destroy()
                            bottom.x += bottom.vx
                            bottom.y += bottom.vy
                        
                        
                        for s in self.getSpritesbyClass(Spring):
                            if s.y>1000:
                                s.destroy()
                            s.y += s.vy
                            mm = 0
                            
                            for w in self.getSpritesbyClass(Wall):
                                if s.collidingWith(w): 
                                    mm+=1
                                
                            if mm > 0: 
                               s.vy=0
                            else:
                                s.vy = s.vy +.6
                            '''
                            l = 0
                            for wwall in self.getSpritesbyClass(Wall):
                                if pplayer.collidingWith(wwall): 
                                    l+=1
                            if l > 0: 
                               pplayer.vx=0
                            else:
                                pplayer.vx = pplayer.vx
                            '''
    
        

    def lvelocity(self, event): 
        for pplayer in self.getSpritesbyClass(Player):
            pplayer.vx = -1
    def lvelocity2(self, event): 
        for pplayer in self.getSpritesbyClass(Player):
            pplayer.vx = 0
    def rvelocity(self, event): 
        for pplayer in self.getSpritesbyClass(Player):
            pplayer.vx = 1
    def rvelocity2(self, event): 
        for pplayer in self.getSpritesbyClass(Player):
            pplayer.vx = 0
    
    def lvelocityb(self, event): 
        for bottom in self.getSpritesbyClass(Bottom):
            bottom.vx = -1
    def lvelocity2b(self, event): 
        for bottom in self.getSpritesbyClass(Bottom):
            bottom.vx = 0
    def rvelocityb(self, event): 
        for bottom in self.getSpritesbyClass(Bottom):
            bottom.vx = 1
    def rvelocity2b(self, event): 
        for bottom in self.getSpritesbyClass(Bottom):
            bottom.vx = 0
    
    
    def lvelocityt(self, event): 
        for top in self.getSpritesbyClass(Top):
            top.vx = -1
    def lvelocity2t(self, event): 
        for top in self.getSpritesbyClass(Top):
            top.vx = 0
    def rvelocityt(self, event): 
        for top in self.getSpritesbyClass(Top):
            top.vx = 1
    def rvelocity2t(self, event): 
        for top in self.getSpritesbyClass(Top):
            top.vx = 0
            
    def lvelocityl(self, event): 
        for left in self.getSpritesbyClass(Left):
            left.vx = -1
    def lvelocity2l(self, event): 
        for left in self.getSpritesbyClass(Left):
            left.vx = 0
    def rvelocityl(self, event): 
        for left in self.getSpritesbyClass(Left):
            left.vx = 1
    def rvelocity2l(self, event): 
        for left in self.getSpritesbyClass(Left):
            left.vx = 0
    
    
    def lvelocityr(self, event): 
        for right in self.getSpritesbyClass(Right):
            right.vx = -1
    def lvelocity2r(self, event): 
        for right in self.getSpritesbyClass(Right):
            right.vx = 0
    def rvelocityr(self, event): 
        for right in self.getSpritesbyClass(Right):
            right.vx = 1
    def rvelocity2r(self, event): 
        for right in self.getSpritesbyClass(Right):
            right.vx = 0
            
    def jump(self, event): 
        for pplayer in self.getSpritesbyClass(Player):
            pplayer.vy = -10
    def jump2(self, event): 
        for pplayer in self.getSpritesbyClass(Player):
            pplayer.vy = 0
            
    def mouse(self, event):
        self.asset[0]= event.x
        self.asset[1] = event.y
        
    def wall(self, event):
        Wall(((35*(floor((self.asset[0])/35))), (35*(floor((self.asset[1])/35)))))
    
    def player(self, event):
        for a in Platformer.getSpritesbyClass(Player):
            a.destroy()
        Player((self.asset[0], self.asset[1]))
        Left((self.asset[0], self.asset[1]+9))
        Right((self.asset[0]+8, self.asset[1]+9))
        Top((self.asset[0]+4, self.asset[1]))
        Bottom((self.asset[0]+4, self.asset[1]+25))
        
    def spring(self, event):
        Spring((self.asset[0], self.asset[1]))
    
myapp = Platformer()
myapp.run()
