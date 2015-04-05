import pygame
from pygame import *
import os
#class of Tile
class Tile:
    def __init__(self,char,pos,solid):
        self.image = image.load(os.path.join('images',char+'.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.solid = solid
    def blit(self,player,surface):
        #collision system
        if self.solid:
            if self.rect.colliderect(player.rect):
                if self.rect.top+31 == player.rect.top:
                    player.up = 0
                    player.rect.move(0,3)
                elif self.rect.top+1 == player.rect.bottom:
                    player.down = 0
                    player.rect.move_ip(0,-1)
                elif self.rect.left+1 == player.rect.right:
                    player.right = 0
                    player.rect.move_ip(-1,0)
                elif self.rect.right-1 == player.rect.left:
                    player.left = 0
                    player.rect.move_ip(1,0)
                    print(player.up,player.down,player.left,player.right)
        surface.blit(self.image,self.rect)
#player duh
class Player:
    def __init__(self):
        self.image = image.load(os.path.join('images','player.png'))
        self.rect = self.image.get_rect()
        self.rect.topleft = (64,64)
        self.left,self.right,self.up,self.down = 0,0,0,0
    def move(self):
        if self.up:
            self.rect.move_ip(0,-1)
        if self.down:
            self.rect.move_ip(0,1)
        if self.left:
            self.rect.move_ip(-1,0)
        if self.right:
            self.rect.move_ip(1,0)
class NPC:
    def __init__(self,npcimage,text,pos,walkType):
        self.image = image.load(os.path.join('images',npcimage+'.png'))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.text = text
        self.white = (255,255,255)
        self.exit = 1
        self.name = npcimage
        self.dir = 1
        self.steps = 0
        self.textRendered = False
        self.timeBeforeTurn = 100
        #just a variable to set radius of npc walking
        self.type = walkType
    def displayText(self,surface,player,fontas,smallfont):
        if self.textRendered == False:
            self.textImg = fontas.render(self.text,False,self.white)
            self.nameImg = smallfont.render(self.name,False,(100,180,0))
            self.textRendered = True
        if self.rect.colliderect(player.rect):
            if self.rect.bottom-1 == player.rect.top:
                player.up = 0
                player.rect.move(0,3)
            elif self.rect.top+1 == player.rect.bottom:
                player.down = 0
                player.rect.move_ip(0,-1)
            elif self.rect.left+1 == player.rect.right:
                player.right = 0
                player.rect.move_ip(-1,0)
            elif self.rect.right-1 == player.rect.left:
                player.left = 0
                player.rect.move_ip(1,0)
            self.exit = 0
        else:
            self.exit = 1
            
        if not self.exit:
            surface.blit(self.textImg,(0,320))
            
        #automatic npc walking
            
        if self.steps <10*self.type:
            if self.dir == 1:
                self.rect.move_ip(0,-1)
                self.steps+=1
            if self.dir == 2:
                self.rect.move_ip(-1,0)
                self.steps +=1
            if self.dir == 3:
                self.rect.move_ip(0,1)
                self.steps +=1
            if self.dir == 4:
                self.rect.move_ip(1,0)
                self.steps += 1
        else:
            self.steps = 0
            if self.dir == 4:
                self.dir = 1
            else:
                self.dir +=1
            if self.timeBeforeTurn == 0:
                self.dir = 1
            
        surface.blit(self.image,self.rect)
        surface.blit(self.nameImg,(self.rect.left+5,self.rect.top - 10))
