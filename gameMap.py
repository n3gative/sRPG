import pygame
from pygame import *
from os import path
from classes import Tile
class Map():
	def __init__(self,imgFile):#imgFile = file containing all images or specific set
		self.imageFile = open(imgFile,'r')
		self.imageNames = self.imageFile.readlines()
		self.images = {}
		for i in xrange(0,len(self.imageNames)):
			self.imageNames[i] = self.imageNames[i].rstrip('\n')
			imgName = self.imageNames[i][:-4]
			print imgName
			self.images[imgName] = image.load(path.join("images",self.imageNames[i].rstrip('\n')))
		self.imageFile.close()
		self.mapLegend = {}
		self.tileMap = []
		self.mapSize = []
		self.mapObj = ""
		print self.imageNames
	def reloadTileSet(self,imgFile):
		self.imageFile = open(imgFile,'r')
		self.imageNames = self.imageFile.readlines()
		self.images = {}
		for i in xrange(0,len(self.imageNames)):
			self.imageNames[i] = self.imageNames[i].rstrip('\n')
			imgName = self.imageNames[i][:-4]
			print imgName
			self.images[imgName] = image.load(path.join("images",self.imageNames[i].rstrip('\n')))
		self.imageFile.close()
	def initTest(self,surface):
		clock = time.Clock()
		for i in xrange(0,len(self.imageNames)):
			surface.fill((0,0,0))
			surface.blit(self.images[self.imageNames[i]],(12,12))
			display.flip()
			clock.tick(1)
	def loadCurrMapLegend(self, mapFileName):
		self.mapLegend = {}
		mapfile = open(mapFileName,"r")
		for i in xrange(int(mapfile.readline())):
			legendData = mapfile.readline()
			legendData = legendData.split("=")
			self.mapLegend[str(legendData[0])] = legendData[1].rstrip('\n')
		mapfile.close()
		print self.mapLegend
	def loadCurrMap(self, mapFileName):
		self.tileMap = []
		mapFile = open(mapFileName,"r")
		size = mapFile.readline().split(",")
		self.mapSize = [int(size[0]),int(size[1])]
		print self.mapSize
		for i in xrange(self.mapSize[1]):
			templist = []
			mapLine = mapFile.readline()
			print mapLine
			for d in xrange(self.mapSize[0]):
				tempTile = Tile(self.mapLegend[ str(mapLine[d])],(d*32,i*32))
				templist.append(tempTile)
			self.tileMap.append(templist)
		mapFile.close()
	def displayMap(self,surface):
		for i in xrange(self.mapSize[1]):
			for x in xrange(self.mapSize[0]):
				surface.blit(self.images[ self.tileMap[i][x].imageName ], self.tileMap[i][x].rect)

