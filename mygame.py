import pygame
# from pygame.locals import *

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

running = True
playerpos = [100, 100] 

#use resource
player = pygame.image.load("./resources/images/dude.png")
grass = pygame.image.load("./resources/images/grass.png")
castle = pygame.image.load("./resources/images/castle.png")

while(running):
	screen.fill(0)

	#? Draww Grass
	for x in range(int(width/grass.get_width()+1)):
		for y in range(int(height/grass.get_height()+1)):
			screen.blit(grass, (x*100, y*100))
			
	#? Draw castle
	screen.blit(castle, (0,30))
	screen.blit(castle, (0, 135))
	screen.blit(castle, (0, 240))
	screen.blit(castle, (0, 345))

	screen.blit(player, playerpos)
	pygame.display.flip()
	for event in pygame.event.get():
		pygame.quit()
		exit(0)


