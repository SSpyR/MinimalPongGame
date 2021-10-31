# import the pygame module, so you can use it
import pygame, random
from paddle import Paddle
from ball import Ball
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    # logo = pygame.image.load("logo32x32.png")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    WIDTH=800
    HEIGHT=400
    BORDER=15
    VELOCITY=1
    FPS=30 # framerate
    screen = pygame.display.set_mode((WIDTH,HEIGHT))

    # color variable
    fgcolor=pygame.Color('Yellow')
    bgcolor=pygame.Color('Black')

    # add a solid background as r,g,b:
    screen.fill((0,0,0))
    pygame.display.update()

    # top wall
    pygame.draw.rect(screen, fgcolor, ((0,0), (WIDTH, BORDER)))
    # left wall
    pygame.draw.rect(screen, fgcolor, ((0,0), (BORDER, HEIGHT)))
    # bottom wall
    pygame.draw.rect(screen, fgcolor, ((0,385), (WIDTH, BORDER)))

    # ball variable init
    x0=WIDTH-Ball.RADIUS
    y0=HEIGHT//2
    vx0=-VELOCITY
    vy0=random.randint(-VELOCITY, VELOCITY)

    # ball object init
    ball0=Ball(x0,y0,vx0,vy0,screen,fgcolor,bgcolor,BORDER,HEIGHT)
    ball0.show(fgcolor)

    pygame.display.update()
    
    # define a variable to control the main loop
    running = True
    clock=pygame.time.Clock()
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        pygame.display.update()
        clock.tick(FPS)
        # ball
        ball0.update()
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()