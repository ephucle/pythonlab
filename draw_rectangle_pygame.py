import pygame, sys
from pygame.locals import *

def main():
    pygame.init()
    X = 500
    Y = 500
    DISPLAY=pygame.display.set_mode((X,Y),0,32)

    WHITE=(255,255,255)
    BLUE=(0,0,255)
    LIGHTBLUE= (0, 0, 255)
    GREEN = (0, 255, 0)
    RED= (200, 0, 0 )
    PURPLE = (102, 0, 102)
    DISPLAY.fill(WHITE)

    #pygame.draw.rect(DISPLAY,BLUE,(200,150,100,50))
    #draw circle at center of DISPLAY
    pygame.draw.circle(DISPLAY, RED, (X//2, Y//2), 100)
    pygame.draw.rect(DISPLAY,GREEN,(0,0,100,100)) #test diem goc, corner 1, goc tren ben trai
    pygame.draw.rect(DISPLAY,PURPLE,(X-100,0,X,100)) #test diem goc, corner 2, goc tren ben phai
    pygame.draw.rect(DISPLAY,RED,(X-100,Y-100,X,Y)) #test diem goc, corner 3, goc duoi ben phai
    pygame.draw.rect(DISPLAY,LIGHTBLUE,(0,Y-100,100,Y)) #test diem goc, corner 4, goc duoi ben trai

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()