import pygame
from pygame import *
import math
# from pygame import K_RETURN, K_S, K_W, K_UP, K_DOWN

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

keys = {
	'top': False,
	'right': False,
	'bottom': False,
	'left':False
}

running = True
playerpos = [300, 100] 

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

	mouse_position = pygame.mouse.get_pos()
	angel = math.atan2(mouse_position[1] - (playerpos[1]+32), mouse_position[0] - (playerpos[0]+26))
	player_rotation = pygame.transform.rotate(player, 360 - angel * 57.29)
	new_playerpos = (playerpos[0] - player_rotation.get_rect().width / 2, playerpos[1] - player_rotation.get_rect().height / 2)
	screen.blit(player_rotation, new_playerpos)

	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)

		if event.type == pygame.KEYDOWN:
			if event.key == K_w:
				keys['top'] = True
			elif event.key == K_d:
				keys['right'] = True
			elif event.key == K_s:
				keys['bottom'] = True
			elif event.key == K_a:
				keys['left'] = True
		if event.type == pygame.KEYUP:
			if event.key == K_w:
				keys['top'] = False
			elif event.key == K_d:
				keys['right'] = False
			elif event.key == K_s:
				keys['bottom'] = False
			elif event.key == K_a:
				keys['left'] = False
	
	if keys['top']:
		playerpos[1] -= 5
	elif keys['bottom']:
		playerpos[1] += 5
	if keys['right']:
		playerpos[0] += 5
	elif keys['left']:
		playerpos[0] -= 5
		


