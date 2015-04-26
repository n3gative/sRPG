import pygame
import Tkinter,tkFileDialog
from pygame import *
from os import path
from gameMap import *
import inputbox
class Controller():
	def __init__(self):
		pass
	def loadMap(self,mapObj): #for loading maps from hdd
		root = Tkinter.Tk()
		root.withdraw()
		file_path = tkFileDialog.askopenfilename(
					defaultextension=".dat",initialdir=path.join("data"),title="Open map*.dat")
		print file_path
		mapObj.loadCurrMap(file_path)
	def newMap(self):
		mapObj = Map(path.join("images","imgdb.dat"))
		mapObj.loadCurrMapLegend(path.join("data","emptyMapLegend.dat"))
		mapObj.loadCurrMap(path.join("data","emptyMap.dat"))
		return mapObj
	def loadLegend(self,mapObj): #for loading map legend ,call both loadMap() and loadLegend() at same time
		root = Tkinter.Tk()
		root.withdraw()
		file_path = tkFileDialog.askopenfilename(
					defaultextension=".dat",initialdir=path.join("data"),title="Open map*Legend.dat")
		print file_path
		mapObj.loadCurrMapLegend(file_path)
	def loadTileSet(self,mapObj):
		root = Tkinter.Tk()
		root.withdraw()
		file_path = tkFileDialog.askopenfilename(
					defaultextension=".dat",initialdir=path.join("images"),title="Open imagedb.dat")
		mapObj.reloadTileSet(file_path)
class Button():
	def __init__(self,imagepath,pos):
		self.image = image.load(imagepath).convert()
		self.rect = self.image.get_rect()
		self.rect.topleft = pos
	def blitSelf(self,surface):
		surface.blit(self.image,self.rect)
class newButton(Button):
	def __init__(self,imagepath,pos):
		Button.__init__(self,imagepath,pos)
	def pressedNewButton(self,bBox):
		mappy = Map(path.join("images","imgdb.dat"))
		return bBox.newMap()
class loadButton(Button):
	def __init__(self,imagepath,pos):
		Button.__init__(self,imagepath,pos)
	def pressedLoadButton(self,bBox):
		loadedMap = Map(path.join("data","empty.dat")) 
		bBox.loadTileSet(loadedMap)
		bBox.loadLegend(loadedMap)
		bBox.loadMap(loadedMap)
		return loadedMap

class MyDialog():
	def __init__(self,parent):
		top = self.top = Tkinter.Toplevel(parent)
		Tkinter.Label(top,text="What size terrain You want?(x y)").pack()
		self.e = Tkinter.Entry(top)
		self.e.pack(padx=7)
		b = Tkinter.Button(top,text="Ok",command=self.ok)
		b.pack(pady=5)
	def ok(self):
		return self.e.get()
		
		
class genButton(Button):
	def __init__(self,imagepath,pos):
		Button.__init__(self,imagepath,pos)
	def pressedGenButton(self,screen,bBox):
		size = inputbox.ask(screen,"Terrain size in tiles (x y)")
		print size
		size = size.split("x")
		print size
		size = [int(size[0]),int(size[1])]
		print size
		file_path = path.join("data","tempMap.dat")
		tempMapFile = open(file_path,"w")
		tempMapFile.write(str(size[0])+","+str(size[1])+"\n")
		for i in xrange(int(size[1])):
			tempMapFile.write("x"*int(size[0])+"\n")
		tempMapFile.close()
		tempMap = Map(path.join("images","imgdb.dat"))
		tempLegend = tempMap.loadCurrMapLegend(path.join("data","map1legend.dat"))
		tempMap.loadCurrMap(path.join("data","tempMap.dat"))
		return tempMap
class Grid():
	def __init__(self,size):
		self.size = size
		self.color = (0,0,0)
		self.spacing = [32,32]
		self.count = [size[0]/self.spacing[0], size[1] / self.spacing[1]]
	def displaySelf(self,surface):
		for i in xrange(self.size[0]):
			draw.line(surface,self.color,(0,i*32),(self.size[0]*32,i*32))
		for x in xrange(self.size[1]):
			draw.line(surface,self.color,(x*32,0),(x*32,self.size[1]*32))
			
def main():
	#Usual settin,gs like res and stuff
	editorRes = [1366,768] #TODO: Change later
	grid = Grid([10*32,10*32])
	screen = pygame.display.set_mode(editorRes)
	layers = 5 #amount of layes to put tiles on
	rectColor = (155,155,155)
	rectList = [] #for invisible walls n stuff
	rectPt1,rectPt2 = [0,0],[0,0] # start and end point for invisible Rects
	isMakingRect = False
	isMovingRect = False
	bBox = Controller()
	stButton = newButton(path.join("images", "button_newmap.png"),(1366-128,0))
	loButton = loadButton(path.join("images","button_loadmap.png"),(1366-128,37))
	gnButton = genButton(path.join("images","button_genTerrain.png"),(1366-128,74))
	nMap = Map(path.join("images","imgdb.dat"))
	nMap = bBox.newMap()
	mouseRect = rect.Rect(3,3,3,3)
	# FIX LATER 
	#pygame.display.set_title("Map Editor")
	
	
	while True:
		for event in pygame.event.get():	
			if event.type == MOUSEBUTTONDOWN:
				if stButton.rect.colliderect(mouseRect):
					stButton.pressedNewButton(bBox)
				elif loButton.rect.colliderect(mouseRect):
					nMap = loButton.pressedLoadButton(bBox)
				elif gnButton.rect.colliderect(mouseRect):
					nMap = gnButton.pressedGenButton(screen,bBox)
		mouseRect.topleft = mouse.get_pos()
		screen.fill((200,0,0))
		nMap.displayMap(screen)
		stButton.blitSelf(screen)
		loButton.blitSelf(screen)
		gnButton.blitSelf(screen)
		grid.displaySelf(screen)
		display.flip()



if __name__ == "__main__":
	main()
