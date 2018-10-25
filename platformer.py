"""
platformer.py
Author: Meg
Credit: http://brythonserver.github.io/ggame/#ggame.Sprite.collidingWithSprites
https://github.com/HHS-IntroProgramming/Platformer
https://runpython.org/?user=BrythonServer&repo=Platformer&name=platformer.py
Noah
Assignment:
Write and submit a program that implements the sandbox platformer game:

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
from math import floor
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
grey = Color(0x5b6672, 1.0)
teal = Color(0x9fffff, 1.0)
coral = Color(0xff9664, 1.0)
clear = Color(0x000000, 0.0)

thinline = LineStyle(2, black)
blkline = LineStyle(1, black)
noline = LineStyle(0, white)
coolline = LineStyle(1, grey)
blueline = LineStyle(2, blue)
redline = LineStyle(1, red)
greenline = LineStyle(1, green)
gridline = LineStyle(1, grey)
clearline = LineStyle(1, clear)
tealline =  LineStyle(1, teal)
grid=RectangleAsset(30,30,gridline,white)


class Wall(Sprite):
    """
    Create Wall
    """
    asset = RectangleAsset(30,30,gridline,white)

    def __init__(self, position):
        super().__init__(Wall.asset, position)
        
class Spring(Sprite):
    """
    Create Spring
    """
    asset = RectangleAsset(15,5,gridline,coral)

    def __init__(self, position):
        super().__init__(Spring.asset, position)
        self.vx = 0
        self.vy = 0
       

class Player(Sprite):
    """
    Create Player
    """
    asset = RectangleAsset(15,30,tealline,teal)

    def __init__(self, position):
        super().__init__(Player.asset, position)

        self.vx = 0
        self.vy = 0
class PlayerL(Sprite):
    """
    Create Player surface
    """
    asset = RectangleAsset(1,20,redline,teal)

    def __init__(self, position):
        super().__init__(PlayerL.asset, position)

        self.vx = 0
        self.vy = 0
        
class PlayerR(Sprite):
    """
    Create Player surface
    """
    asset = RectangleAsset(1,20,redline,teal)

    def __init__(self, position):
        super().__init__(PlayerR.asset, position)

        self.vx = 0
        self.vy = 0
        
        
class PlayerD(Sprite):
    """
    Create Player surface
    """
    asset = RectangleAsset(10,1,redline,teal)

    def __init__(self, position):
        super().__init__(PlayerD.asset, position)

        self.vx = 0
        self.vy = 0
class PlayerU(Sprite):
    """
    Create Player surface
    """
    asset = RectangleAsset(10,1,redline,teal)

    def __init__(self, position):
        super().__init__(PlayerU.asset, position)

        self.vx = 0
        self.vy = 0
class Platform(App):
    """
    Tutorial4 space game example.
    """
    
    def __init__(self):
        super().__init__()
        # Backgroundw
        bg_asset = RectangleAsset(self.width, self.height, noline, grey)
        bg = Sprite(bg_asset, (0,0))
        Platform.listenKeyEvent("keydown", "w", self.wallMaker)
        Platform.listenKeyEvent("keydown", "p", self.playerMaker)
        Platform.listenKeyEvent("keydown", "s", self.springMaker)
        self.asset = [0,0]
        Platform.listenMouseEvent('mousemove', self.mouseMove)
        Platform.listenKeyEvent("keydown", "right arrow", self.right)
        Platform.listenKeyEvent("keyup", "right arrow", self.right2)
        Platform.listenKeyEvent("keydown", "left arrow", self.left)
        Platform.listenKeyEvent("keyup", "left arrow", self.left2)
        Platform.listenKeyEvent("keydown", "up arrow", self.up)

    # Handle the mouse click
    def mouseMove(self, event):
        self.asset[0] = event.x
        self.asset[1] = event.y
        
    def wallMaker(self, event):
        Wall((30*floor((self.asset[0])/30),30*floor((self.asset[1])/30)))
        
    def playerMaker(self, event):
        for a in Platform.getSpritesbyClass(Player):
            a.destroy()
        for a in Platform.getSpritesbyClass(PlayerL):
            a.destroy()
        for a in Platform.getSpritesbyClass(PlayerR):
            a.destroy()
        for a in Platform.getSpritesbyClass(PlayerU):
            a.destroy()
        for a in Platform.getSpritesbyClass(PlayerD):
            a.destroy()
        Player((self.asset[0],self.asset[1]))
        PlayerL((self.asset[0],self.asset[1]+7))
        PlayerR((self.asset[0]+13,self.asset[1]+7))
        PlayerD((self.asset[0]+3,self.asset[1]+29))
        PlayerU((self.asset[0]+3,self.asset[1]))
        
    def springMaker(self, event):
        Spring((self.asset[0],self.asset[1]))
        
    def step(self):
        
        for player in self.getSpritesbyClass(Player):
            for playerL in self.getSpritesbyClass(PlayerL):
                for playerR in self.getSpritesbyClass(PlayerR):
                    for playerU in self.getSpritesbyClass(PlayerU):
                        for playerD in self.getSpritesbyClass(PlayerD):
                            m=0
                            n=0
                            o=0
                            p=0
                            for wall in self.getSpritesbyClass(Wall):
                                if playerL.collidingWith(wall):
                                    m+=1
                                elif playerR.collidingWith(wall):
                                    p+=1
                                elif playerD.collidingWith(wall):
                                    n+=2
                                elif playerU.collidingWith(wall):
                                    n+=1
                            for spring in self.getSpritesbyClass(Spring):
                                if playerD.collidingWith(spring):
                                    o+=1
                            if n>0 and player.vy>=0:
                                player.vy =0
                                playerL.vy =0
                                playerR.vy =0
                                playerD.vy =0
                                playerU.vy =0
                            else:
                                player.vy = player.vy+.5  
                                playerL.vy = playerL.vy+.5
                                playerR.vy =playerR.vy+.5
                                playerD.vy =playerD.vy+.5
                                playerU.vy =playerU.vy+.5
                            if m>0:
                                player.vx =((player.vx)**2)**(1/2)
                                playerL.vx =((playerL.vx)**2)**(1/2)
                                playerR.vx =((playerR.vx)**2)**(1/2)
                                playerD.vx =((playerD.vx)**2)**(1/2)
                                playerU.vx =((playerU.vx)**2)**(1/2)
                            if p>0:
                                player.vx =-1*((player.vx)**2)**(1/2)
                                playerL.vx =-1*((playerL.vx)**2)**(1/2)
                                playerR.vx =-1*((playerR.vx)**2)**(1/2)
                                playerD.vx =-1*((playerD.vx)**2)**(1/2)
                                playerU.vx =-1*((playerU.vx)**2)**(1/2)
                            if o>0:
                                player.vy =-1*player.vy
                                playerL.vy =-1*playerL.vy
                                playerR.vy =-1*playerR.vy
                                playerD.vy =-1*playerD.vy
                                playerU.vy =-1*playerU.vy
                            player.y += player.vy
                            playerL.y += playerL.vy
                            playerR.y += playerR.vy
                            playerD.y += playerD.vy
                            playerU.y += playerU.vy
                            player.x += player.vx
                            playerL.x += playerL.vx
                            playerR.x += playerR.vx
                            playerD.x += playerD.vx
                            playerU.x += playerU.vx
                            if player.y>1000:
                                player.destroy()
                                playerL.destroy()
                                playerR.destroy()
                                playerD.destroy()
                                playerU.destroy()
        for spring in self.getSpritesbyClass(Spring):        
            m=0
            for wall in self.getSpritesbyClass(Wall):
                if spring.collidingWith(wall):
                    m+=1
            if m>0:
                spring.vy =0    
            else:
                spring.vy = spring.vy+.5        
            spring.y += spring.vy
            if spring.y>1000:
                spring.destroy()
             
        
    def right(self, event):
        for player in self.getSpritesbyClass(Player):
            player.vx = 2
        for playerL in self.getSpritesbyClass(PlayerL):
            playerL.vx = 2
        for playerR in self.getSpritesbyClass(PlayerR):
            playerR.vx = 2
        for playerD in self.getSpritesbyClass(PlayerD):
            playerD.vx = 2
        for playerU in self.getSpritesbyClass(PlayerU):
            playerU.vx = 2
    def left(self, event):
        for player in self.getSpritesbyClass(Player):
            player.vx = -2
        for playerL in self.getSpritesbyClass(PlayerL):
            playerL.vx = -2
        for playerR in self.getSpritesbyClass(PlayerR):
            playerR.vx = -2
        for playerD in self.getSpritesbyClass(PlayerD):
            playerD.vx = -2
        for playerU in self.getSpritesbyClass(PlayerU):
            playerU.vx = -2
    def right2(self, event):
        for player in self.getSpritesbyClass(Player):
            player.vx=0
        for playerL in self.getSpritesbyClass(PlayerL):
            playerL.vx = 0
        for playerR in self.getSpritesbyClass(PlayerR):
            playerR.vx = 0
        for playerD in self.getSpritesbyClass(PlayerD):
            playerD.vx = 0
        for playerU in self.getSpritesbyClass(PlayerU):
            playerU.vx = 0
    def left2(self, event):
        for player in self.getSpritesbyClass(Player):
            player.vx=0 
        for playerL in self.getSpritesbyClass(PlayerL):
            playerL.vx = 0
        for playerR in self.getSpritesbyClass(PlayerR):
            playerR.vx = 0
        for playerD in self.getSpritesbyClass(PlayerD):
            playerD.vx = 0
        for playerU in self.getSpritesbyClass(PlayerU):
            playerU.vx = 0
    def up(self, event):
        for player in self.getSpritesbyClass(Player):
            if player.vy==0:
                for player in self.getSpritesbyClass(Player):
                    player.vy = -10
                for playerL in self.getSpritesbyClass(PlayerL):
                    playerL.vy = -10
                for playerR in self.getSpritesbyClass(PlayerR):
                    playerR.vy = -10
                for playerD in self.getSpritesbyClass(PlayerD):
                    playerD.vy = -10
                for playerU in self.getSpritesbyClass(PlayerU):
                    playerU.vy = -10
myapp = Platform()
myapp.run()



