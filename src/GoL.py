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
ClrDark = (48,48,48)
ClrDarker = (32,32,32)
ClrYetDarker = (24,24,24)

ClrBorder = (255,255,255)

ClrCell = (255,255,255)


# Elements
ContRoot = cont.Container(pos=[0,0],size=[WinW,WinH],padding=2)
(ContFooter := cont.Container(parent=ContRoot,size=[516,32])).position("bot")
(ContFooterAccent := cont.Container(parent=ContFooter,size=[516,2])).position("top")



def preInit():
    # init pygame modules
    pg.init()

def init():
    # border
    draw.rect(Win, ClrBorder, ContRoot.getRect())
    draw.rect(Win, ClrBg, (add(ContRoot.pos, [2,2]),
                           sub(ContRoot.size, [4,4])))

    draw.rect(Win, ClrDarker, ContFooter.getRect())
    draw.rect(Win, ClrDark, ContFooterAccent.getRect())





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
