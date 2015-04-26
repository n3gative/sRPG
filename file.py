import pygame
from pygame import *
import os
import classes
from classes import *
from gameMap import Map
def main():
    pygame.init()
    #resolution for 20 tiles horizontally,10 vertically
    blitRes = (640,320)#res = (1366,768)
    realRes = (640,320)
    screen = display.set_mode(blitRes)
    running = 1
    #map file
    mm = Map(os.path.join("images","imgdb.dat"))
    map1 = open(os.path.join('data','map1.dat'),'r')
    tileList = []
    me = Player()
    pos = 0
    clock = pygame.time.Clock()
    fontas = pygame.font.Font(None,20)
    #adding NPC's, you can add as much of them as you want
    Tom = NPC('Tom','Hi,my name is Tom . Nice to meet you',(100,100),1)
    Jim = NPC('Jim','Yo man ! I am called Jim',(200,200),2)
    Twin = NPC('player','I am you and you are me',(300,100),4)
    mazasFont = pygame.font.Font(None,12)
    x,y = -1,0
    doAnswer = 0
    answer = fontas.render('Fuck you Tom !',False,(255,255,255))
    mm.loadCurrMapLegend(os.path.join("data","map1legend.dat"))
    mm.loadCurrMap(os.path.join("data","map1.dat"))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    me.up = 1
                if event.key == K_DOWN:
                    me.down = 1
                if event.key == K_LEFT:
                    me.left = 1
                if event.key == K_RIGHT:
                    me.right = 1
                if event.key == K_RETURN:
                    Tom.exit = 1
                if event.key == K_a:
                   doAnswer = 1 
                if event.key == K_q:
					running = 0
            if event.type == KEYUP:
                if event.key == K_UP:
                    me.up = 0
                if event.key == K_DOWN:
                    me.down = 0
                if event.key == K_LEFT:
                    me.left = 0
                if event.key == K_RIGHT:
                    me.right = 0
        screen.fill((0,0,0))
        screen.fill((0,0,0))
        mm.displayMap(screen)
        me.move()
        Tom.displayText(screen,me,fontas,mazasFont)
        Jim.displayText(screen,me,fontas,mazasFont)
        Twin.displayText(screen,me,fontas,mazasFont)
        screen.blit(me.image,me.rect)
        display.update()
        clock.tick(60)




main()
