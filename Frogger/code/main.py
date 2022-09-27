import pygame, sys
from settings import * #import all variables from setting
from player import Player

#basic stuff
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Frogger')
clock = pygame.time.Clock()

#group
all_sprites = pygame.sprite.Group() #all same group

#sprites
player = Player((600,400), all_sprites)

#game loop
while True:

	#event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# #other type of keyboard input
	# 	if event.type == pygame.KEYDOWN:
	# 		print('key down')
	# 		if event.key == pygame.K_a:
	# 			print('a')

	#delta time
	dt = clock.tick()/1000
#draw a background
	display_surface.fill('black')
	#updates 
	all_sprites.update(dt)

	#draw
	all_sprites.draw(display_surface)

	#update the display surface -> drawing the frame
	pygame.display.update()