import pygame
from pygame import *
from os import path

class ButtonBox():
	def __init__(self, font, buttonText, border = False):
		self.text = buttonText
		self.hasBorder = border
		self.rect = rect.Rect(0,0,100,100)
		print self.rect.topleft
def main():
	#Usual settin,gs like res and stuff
	editorRes = [800,800] #TODO: Change later
	pygame.display.set_mode(editorRes)
	layers = 5 #amount of layes to put tiles on
	rectColor = (155,155,155)
	rectList = [] #for invisible walls n stuff
	rectPt1,rectPt2 = [0,0],[0,0] # start and end point for invisible Rects
	isMakingRect = False
	isMovingRect = False
	editorFont = font.Font(None,24)
	sampleBox = ButtonBox(editorFont, "New", True) 
	
	# FIX LATER 
	#pygame.display.set_title("Map Editor")
	
	
	while True:
		display.flip()



if __name__ == "__main__":
	main()
