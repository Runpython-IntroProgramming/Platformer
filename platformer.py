
"""
platformer.py
Author: 
Credit: 
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

blue = Color(0x2EFEC8, 1.0)
black = Color(0x000000, 1.0)
pink = Color(0xFF00FF, 1.0)
red = Color(0xFF5733, 1.0)
white = Color(0xFFFFFF, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
grey = Color(0xC0C0C0, 1.0)
thinline = LineStyle(2, black)
blkline = LineStyle(1, black)
noline = LineStyle(0, white)
coolline = LineStyle(1, grey)
blueline = LineStyle(2, blue)
redline = LineStyle(1, red)
greenline = LineStyle(1, green)
gridline = LineStyle(1, grey)

from math import floor

class Player(Sprite):
    def __init__(self, position):
        player = RectangleAsset(15,35, noline,red)
        self.vx = 0
        self.vy = 0
        super().__init__(player, position)
        
class Player2(Sprite):
    def __init__(self, position):
        player = RectangleAsset(15,35, noline,blue)
        self.vx = 0
        self.vy = 0
        super().__init__(player, position)

        
class Spring(Sprite):
    def __init__(self,position):
        spring = RectangleAsset(15,8, noline,blue)
        self.vy = 5
        super().__init__(spring, position)

class Bullet(Sprite):
    def __init__(self,position):
        bullet = RectangleAsset(10,5, noline,red)
        self.vx = 0
        self.vy = 0
        super().__init__(bullet, position)
        
class Bullet2(Sprite):
    def __init__(self,position):
        bullet = RectangleAsset(10,5, noline,blue)
        self.vx = 0
        self.vy = 0
        super().__init__(bullet, position)

class Box(Sprite):
    def __init__(self, position):
        box = RectangleAsset(50,50, noline, black)
        super().__init__(box, position)
        
class Line(Sprite):
    def __init__(self, position):
        line = RectangleAsset(1,40, noline, black)
        super().__init__(line, position)
        
class Line2(Sprite):
    def __init__(self, position):
        line = RectangleAsset(1,40, noline, black)
        super().__init__(line, position)
        
class Line3(Sprite):
    def __init__(self, position):
        line = RectangleAsset(48,1, noline, black)
        super().__init__(line, position)

class Line4(Sprite):
    def __init__(self, position):
        line = RectangleAsset(48,1, noline, black)
        super().__init__(line, position)

class Game(App):
    def __init__(self):
        super().__init__()
        grid = RectangleAsset(50,50,gridline,white)
        x = 0 
        y = 0 
        for b in range(15):
            for a in range(25):
                Sprite(grid, (x,y))
                x = x + 50
            x = 0
            Sprite(grid,(x,y))
            y = y + 50
    
        
        print("Press 'x' to sqawn a player 1")
        print("Press 'f' to sqawn a block")
        print("Press 's' to sqawn a spring")
        print("Press 'a' to move left")
        print("Press 'd' to move right")
        print("Press 'w' to jump")
        print("")
        print("Press 'm' to sqawn a player 2")
        print("Press 'h' to sqawn a block")
        print("Press 'k' to sqawn a spring")
        print("Press 'j' to move left")
        print("Press 'l' to move right")
        print("Press 'i' to jump")
        print("")
        print("")
        
        Game.listenKeyEvent('keydown', 'f',  self.Square)
        Game.listenKeyEvent('keydown', 'h',  self.Square)
        Game.listenKeyEvent('keydown', 'x',  self.playerplacement)
        Game.listenKeyEvent('keydown', 'm',  self.player2placement)
        Game.listenKeyEvent('keydown', 's', self.springplacement)
        Game.listenKeyEvent('keydown', 'k', self.springplacement)
        #-----------------------------------------------------------------------
        Game.listenKeyEvent('keydown', 'd', self.right)
        Game.listenKeyEvent('keyup', 'd', self.stop)
        Game.listenKeyEvent('keydown', 'a', self.left)
        Game.listenKeyEvent('keyup', 'a', self.stop)
        Game.listenKeyEvent('keydown', 'w', self.jump)
        Game.listenKeyEvent('keyup', 'w', self.jumpstop)
        #-----------------------------------------------------------------------
        Game.listenKeyEvent('keydown', 'l', self.right2)
        Game.listenKeyEvent('keyup', 'l', self.stop2)
        Game.listenKeyEvent('keydown', 'j', self.left2)
        Game.listenKeyEvent('keyup', 'j', self.stop2)
        Game.listenKeyEvent('keydown', 'i', self.jump2)
        Game.listenKeyEvent('keyup', 'i', self.jumpstop2)
        #-----------------------------------------------------------------------
        Game.listenKeyEvent('keyup', 'e', self.bulletshot)
        Game.listenKeyEvent('keyup', 'q', self.bulletshotleft)
        Game.listenKeyEvent('keydown', 'd', self.bulletright)
        Game.listenKeyEvent('keyup', 'd', self.bulletstop)
        Game.listenKeyEvent('keydown', 'a', self.bulletleft)
        Game.listenKeyEvent('keyup', 'a', self.bulletstop)
        Game.listenKeyEvent('keydown', 'w', self.bulletjump)
        Game.listenKeyEvent('keyup', 'w', self.bulletjumpstop)
        #-----------------------------------------------------------------------
        Game.listenKeyEvent('keyup', 'o', self.bulletshot2)
        Game.listenKeyEvent('keyup', 'u', self.bulletshotleft2)
        Game.listenKeyEvent('keydown', 'l', self.bulletright2)
        Game.listenKeyEvent('keyup', 'l', self.bulletstop2)
        Game.listenKeyEvent('keydown', 'j', self.bulletleft2)
        Game.listenKeyEvent('keyup', 'j', self.bulletstop2)
        Game.listenKeyEvent('keydown', 'i', self.bulletjump2)
        Game.listenKeyEvent('keyup', 'i', self.bulletjumpstop2)
        #-----------------------------------------------------------------------
        Game.listenMouseEvent("mousemove", self.moveMouse)
        
        m = 0
        n = 0
        p = 0 
        q = 0
        
    def moveMouse(self, event):
        self.m = event.x
        self.n = event.y
        
    def Square(self,event):
        x = floor(self.m/50)*50
        y = floor(self.n/50)*50
        Box((x,y))
        
        x = floor(self.m/50)*50
        y = (floor(self.n/50)*50)+10
        Line((x,y))
        
        x = (floor(self.m/50)*50)+49
        y = (floor(self.n/50)*50)+10
        Line2((x,y))
        
        x = (floor(self.m/50)*50)+1
        y = (floor(self.n/50)*50)+49
        Line3((x,y))

    def playerplacement(self,event):
        for a in Game.getSpritesbyClass(Player):
            a.destroy()
        for a in Game.getSpritesbyClass(Bullet):
            a.destroy()
        Player((self.m,self.n))
        Bullet((self.m,self.n))
        
    def player2placement(self,event):
        for a in Game.getSpritesbyClass(Player2):
            a.destroy()
        for a in Game.getSpritesbyClass(Bullet2):
            a.destroy()
        Player2((self.m,self.n))
        Bullet2((self.m,self.n))

    def springplacement(self,event):
        Spring((self.m,self.n))
    
    #-----------------------------------------------------------------------
    
    def right(self, event):
        for a in self.getSpritesbyClass(Player):
            a.vx = 1.8
    
    def left(self,event):
        for a in self.getSpritesbyClass(Player):
            a.vx = -1.8
            
    def stop(self, event):
        for a in self.getSpritesbyClass(Player):
            a.vx = 0  
            
    def jump(self,event):
        for a in self.getSpritesbyClass(Player):
            if a.collidingWithSprites(Box):
                a.vy = -4.3
                
    def jumpstop(self, event):
        for a in self.getSpritesbyClass(Player):
            a.vy += 0.2
   
    #-----------------------------------------------------------------------
                
    def right2(self, event):
        for a in self.getSpritesbyClass(Player2):
            a.vx = 1.8
    
    def left2(self,event):
        for a in self.getSpritesbyClass(Player2):
            a.vx = -1.8
            
    def stop2(self, event):
        for a in self.getSpritesbyClass(Player2):
            a.vx = 0  
            
    def jump2(self,event):
        for a in self.getSpritesbyClass(Player2):
            if a.collidingWithSprites(Box):
                a.vy = -4.3
                
    def jumpstop2(self, event):
        for a in self.getSpritesbyClass(Player):
            a.vy += 0.2
    
    #-----------------------------------------------------------------------
                
    def bulletright(self, event):
        for a in self.getSpritesbyClass(Bullet):
            a.vx = 1.8
    
    def bulletleft(self,event):
        for a in self.getSpritesbyClass(Bullet):
            a.vx = -1.8
            
    def bulletstop(self, event):
        for a in self.getSpritesbyClass(Bullet):
            a.vx = 0  
            
    def bulletjump(self,event):
        for a in self.getSpritesbyClass(Bullet):
            if a.collidingWithSprites(Box):
                a.vy = -4.3

    def bulletjumpstop(self, event):
        for a in self.getSpritesbyClass(Bullet):
            a.vy += 0.2
            
    def bulletshot(self,event):
        for a in self.getSpritesbyClass(Bullet):
            a.vy = 0
            a.vx = 2
            
    def bulletshotleft(self,event):
        for a in self.getSpritesbyClass(Bullet):
            a.vy = 0

            a.vx = -2
    
     #-----------------------------------------------------------------------
                
    def bulletright2(self, event):
        for a in self.getSpritesbyClass(Bullet2):
            a.vx = 1.8
    
    def bulletleft2(self,event):
        for a in self.getSpritesbyClass(Bullet2):
            a.vx = -1.8
            
    def bulletstop2(self, event):
        for a in self.getSpritesbyClass(Bullet2):
            a.vx = 0  
            
    def bulletjump2(self,event):
        for a in self.getSpritesbyClass(Bullet2):
            if a.collidingWithSprites(Box):
                a.vy = -4.3

    def bulletjumpstop2(self, event):
        for a in self.getSpritesbyClass(Bullet2):
            a.vy += 0.2
            
    def bulletshot2(self,event):
        for a in self.getSpritesbyClass(Bullet2):
            a.vy = 0
            a.y -= 20
            a.vx = 2
            
    def bulletshotleft2(self,event):
        for a in self.getSpritesbyClass(Bullet2):
            a.vy = 0
            a.y -= 20
            a.vx = -2
    #-----------------------------------------------------------------------
    
    def step(self):
        for b in self.getSpritesbyClass(Spring):
            b.y += b.vy
    
            if b.collidingWithSprites(Box):
                b.vy = 0
            
            else:
                b.vy = 5    
    
        for a in self.getSpritesbyClass(Player):
            a.x += a.vx
            a.y += a.vy
    
            if a.collidingWithSprites(Box):
                a.vy = 0
                a.y -= 0.2
            
            elif a.collidingWithSprites(Bullet2):
                a.destroy()
                print("Player 2 Wins!")

            else:
                a.vy += 0.2
             
            for a in self.getSpritesbyClass(Player):
                a.x += a.vx
                a.y += a.vy  
                
                if a.collidingWithSprites(Line):
                    a.vx = -1
                
                if a.collidingWithSprites(Line2):
                    a.vx = 1
                
                if a.collidingWithSprites(Line3):
                    a.vy = 1
                
                if a.collidingWithSprites(Spring):
                    a.vy = -6 
                    
        #-----------------------------------------------------------------------
        
        for a in self.getSpritesbyClass(Player2):
            a.x += a.vx
            a.y += a.vy
    
            if a.collidingWithSprites(Box):
                a.vy = 0
                a.y -= 0.2
                
            elif a.collidingWithSprites(Bullet):
                a.destroy()
                print("Player 1 Wins!")
            

            else:
                a.vy += 0.2
             
            for a in self.getSpritesbyClass(Player2):
                a.x += a.vx
                a.y += a.vy  
                
                if a.collidingWithSprites(Line):
                    a.vx = -1
                
                if a.collidingWithSprites(Line2):
                    a.vx = 1
                
                if a.collidingWithSprites(Line3):
                    a.vy = 1
                
                if a.collidingWithSprites(Spring):
                    a.vy = -6   
                    
        #-----------------------------------------------------------------------
                    
        for a in self.getSpritesbyClass(Bullet):
            a.x += a.vx
            a.y += a.vy
    
            if a.collidingWithSprites(Box):
                a.vy = 0
                a.y -= 0.2
                
            else:
                a.vy += 0.2
             
            for a in self.getSpritesbyClass(Bullet):
                a.x += a.vx
                a.y += a.vy  
                
                if a.collidingWithSprites(Line):
                    a.vx = -1
                
                if a.collidingWithSprites(Line2):
                    a.vx = 1
                
                if a.collidingWithSprites(Line3):
                    a.vy = 1
                
                if a.collidingWithSprites(Spring):
                    a.vy = -6   
        
        #-----------------------------------------------------------------------
                
        for a in self.getSpritesbyClass(Bullet2):
            a.x += a.vx
            a.y += a.vy
    
            if a.collidingWithSprites(Box):
                a.vy = 0
                a.y -= 0.2
                
            else:
                a.vy += 0.2
             
            for a in self.getSpritesbyClass(Bullet2):
                a.x += a.vx
                a.y += a.vy  
                
                if a.collidingWithSprites(Line):
                    a.vx = -1
                
                if a.collidingWithSprites(Line2):
                    a.vx = 1
                
                if a.collidingWithSprites(Line3):
                    a.vy = 1
                
                if a.collidingWithSprites(Spring):
                    a.vy = -6   
                    
        
myapp = Game()
myapp.run()