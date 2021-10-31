import pygame

class Ball:
    # pass
    # class variables
    RADIUS=10

    def __init__(self,x,y,vx,vy,screen,fgcolor,bgcolor,border,height):
        # instanced variables
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.screen=screen
        self.fgcolor=fgcolor
        self.bgcolor=bgcolor
        self.border=border
        self.height=height

    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.RADIUS)

    def update(self):
        # np=op+dp
        # delete old ball
        self.show(self.bgcolor)
        self.x=self.x+self.vx
        self.y=self.y+self.vy
        if self.x<self.border:
            self.vx=-self.vx
        if self.y>self.height:
            self.vy=-self.vy
        if self.y<self.border:
            self.vy=-self.vy
        self.show(self.fgcolor)
        
        