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
        Platformer.listenKeyEvent('keydown', 'up arrow', self.uvelocityb)
        Platformer.listenKeyEvent('keyup', 'up arrow', self.uvelocity2b)
        
        Platformer.listenKeyEvent('keydown', 'left arrow', self.lvelocityr)
        Platformer.listenKeyEvent('keyup', 'left arrow', self.lvelocity2r)
        Platformer.listenKeyEvent('keydown', 'right arrow', self.rvelocityr)
        Platformer.listenKeyEvent('keyup', 'right arrow', self.rvelocity2r)
        Platformer.listenKeyEvent('keydown', 'up arrow', self.uvelocityr)
        Platformer.listenKeyEvent('keyup', 'up arrow', self.uvelocity2r)
        
        Platformer.listenKeyEvent('keydown', 'left arrow', self.lvelocityl)
        Platformer.listenKeyEvent('keyup', 'left arrow', self.lvelocity2l)
        Platformer.listenKeyEvent('keydown', 'right arrow', self.rvelocityl)
        Platformer.listenKeyEvent('keyup', 'right arrow', self.rvelocity2l)
        Platformer.listenKeyEvent('keydown', 'up arrow', self.uvelocityl)
        Platformer.listenKeyEvent('keyup', 'up arrow', self.uvelocity2l)
        
        Platformer.listenKeyEvent('keydown', 'left arrow', self.lvelocityt)
        Platformer.listenKeyEvent('keyup', 'left arrow', self.lvelocity2t)
        Platformer.listenKeyEvent('keydown', 'right arrow', self.rvelocityt)
        Platformer.listenKeyEvent('keyup', 'right arrow', self.rvelocity2t)
        Platformer.listenKeyEvent('keydown', 'up arrow', self.uvelocityt)
        Platformer.listenKeyEvent('keyup', 'up arrow', self.uvelocity2t)
        
        Platformer.listenKeyEvent('keydown', 'up arrow', self.uvelocity)
        Platformer.listenKeyEvent('keyup', 'up arrow', self.uvelocity2)
    
    def step(self):  
        
        for pplayer in self.getSpritesbyClass(Player):
            for left in self.getSpritesbyClass(Left):
                for right in self.getSpritesbyClass(Right):
                    for top in self.getSpritesbyClass(Top):
                        for bottom in self.getSpritesbyClass(Bottom):
                            if pplayer.y>1000:
                                pplayer.destroy()
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
                               pplayer.vy=-pplayer.vy
                               left.vy=-left.vy
                               right.vy=-right.vy
                               top.vy=-top.vy
                               bottom.vy=-bottom.vy
                               
                            else:
                                left.vy = left.vy +.6
                                pplayer.vy = pplayer.vy +.6
                                bottom.vy = bottom.vy +.6
                                top.vy = top.vy +.6
                                right.vy = right.vy +.6
                            
                            if q > 0: 
                               pplayer.vx=-pplayer.vx
                               left.vx=-left.vx
                               right.vx=-right.vx
                               top.vx=-top.vx
                               bottom.vx=-bottom.vx
    
                            
                            if m > 0: 
                               pplayer.vx=-pplayer.vx
                               left.vx=-left.vx
                               right.vx=-right.vx
                               top.vx=-top.vx
                               bottom.vx=-bottom.vx
                        
                            n=0
                            for sspring in self.getSpritesbyClass(Spring):
                                if bottom.collidingWith(sspring): 
                                    n+=1
                            if n > 0: 
                               bottom.vy=  -10
                               left.vy=  -10
                               top.vy=  -10
                               right.vy=  -10
                               pplayer.vy=  -10
                            else:
                                pplayer.vy = pplayer.vy
                                top.vy = top.vy
                                bottom.vy = bottom.vy
                                right.vy = right.vy
                                left.vy = left.vy
                        
                            if right.y>1000:
                                right.destroy()
                            
                            if left.y>1000:
                                left.destroy()
                           
                            if top.y>1000:
                                top.destroy()
                        
                            if bottom.y>1000:
                                bottom.destroy()
                            
                            pplayer.x += pplayer.vx
                            pplayer.y += pplayer.vy
                                
                            left.x += left.vx
                            left.y += left.vy
                                
                            right.x += right.vx
                            right.y += right.vy
                                
                            bottom.x += bottom.vx
                            bottom.y += bottom.vy
                                
                            top.x += top.vx
                            top.y += top.vy    
                        
                        
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
    def uvelocity(self, event): 
        for pplayer in self.getSpritesbyClass(Player):
            pplayer.vy = -20
    def uvelocity2(self, event): 
        for pplayer in self.getSpritesbyClass(Player):
            pplayer.vy = 0
    
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
    def uvelocityb(self, event): 
        for bottom in self.getSpritesbyClass(Bottom):
            bottom.vy = -20
    def uvelocity2b(self, event): 
        for bottom in self.getSpritesbyClass(Bottom):
            bottom.vy = 0
    
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
    def uvelocityt(self, event): 
        for top in self.getSpritesbyClass(Top):
            top.vy = -20
    def uvelocity2t(self, event): 
        for top in self.getSpritesbyClass(Top):
            top.vy = 0
     
          
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
    def uvelocityl(self, event): 
        for left in self.getSpritesbyClass(Left):
            left.vy = -20
    def uvelocity2l(self, event): 
        for left in self.getSpritesbyClass(Left):
            left.vy = 0
            
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
    def uvelocityr(self, event): 
        for right in self.getSpritesbyClass(Right):
            right.vy = -20
    def uvelocity2r(self, event): 
        for right in self.getSpritesbyClass(Right):
            right.vy = 0        
    
    
    def mouse(self, event):
        self.asset[0]= event.x
        self.asset[1] = event.y
        
    def wall(self, event):
        Wall(((35*(floor((self.asset[0])/35))), (35*(floor((self.asset[1])/35)))))
    
    def player(self, event):
        for a in Platformer.getSpritesbyClass(Player):
            a.destroy()
        for b in Platformer.getSpritesbyClass(Bottom):
            b.destroy()
        for t in Platformer.getSpritesbyClass(Top):
            t.destroy()
        for l in Platformer.getSpritesbyClass(Left):
            l.destroy()
        for r in Platformer.getSpritesbyClass(Right):
            r.destroy()
        Player((self.asset[0], self.asset[1]))
        Left((self.asset[0], self.asset[1]+9))
        Right((self.asset[0]+8, self.asset[1]+9))
        Top((self.asset[0]+4, self.asset[1]))
        Bottom((self.asset[0]+4, self.asset[1]+25))
        
    def spring(self, event):
        Spring((self.asset[0], self.asset[1]))
    
myapp = Platformer()
myapp.run()
