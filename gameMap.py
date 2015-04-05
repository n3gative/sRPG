import pygame
from pygame import *
from os import path
class Map():
	def __init__(self,imgFile):#imgFile = file containing all images or specific set
		self.imageFile = open(imgFile,'r')
		self.imageNames = self.imageFile.readlines()
		self.images = {}
		for i in xrange(0,len(self.imageNames)):
			print self.imageNames[i]
			self.images[self.imageNames[i]] = image.load(path.join("images2",self.imageNames[i].rstrip()))
		self.imageFile.close()
	def initTest(self,surface):
		clock = time.Clock()
		for i in xrange(0,len(self.imageNames)):
			surface.fill((0,0,0))
			surface.blit(self.images[self.imageNames[i]],(12,12))
			display.flip()
			clock.tick(1)
