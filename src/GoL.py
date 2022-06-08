import pygame as pg
import pygame.draw as draw
import Container as cont
from MaxwellMatrices import *

# Variables

WinW = WinH = 520
Win = pg.display.set_mode((WinW,WinH))

FPS = 165
WinRefresh = int(1 / FPS * 1000)


# Colors
ClrBg = (0,0,0)

ClrBorder = (255,255,255)

ClrCell = (255,255,255)


# Elements
ContRoot = cont.Container(pos=[0,0],size=[WinW,WinH],padding=[])
(ContFooter := cont.Container(parent=ContRoot,pos=[0,0],size=[516,32])).position(("bot","left"))



def preInit():
    # init pygame modules
    pg.init()

def init():
    # border
    draw.rect(Win, ClrBorder, ContRoot.getRect())
    draw.rect(Win, ClrBg, (add(ContRoot.pos, [2,2]),
                           sub(ContRoot.size, [4,4])))

    draw.rect(Win, (0,0,128), ContFooter.getRect())





def main():
    events = pg.event.get()

    for event in events:
        triggerQuit(event)


    updateScreen()



def updateScreen(regions=None):
    pg.display.update()

def triggerQuit(event):
    if event.type == pg.QUIT:
        pg.quit()



if __name__ == "__main__":
    preInit()
    init()
    while True:
        pg.time.delay(WinRefresh)
        main()
