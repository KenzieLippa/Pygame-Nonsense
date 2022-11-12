import pygame, sys
from settings import * #import all variables from setting
from player import Player
from car import Car

class AllSprites(pygame.sprite.Group):
	#take original group and make changes
	def __init__(self):
		super().__init__()
		self.offset = pygame.math.Vector2(0,0) #changing this changes where he is but allows you to still move everything th same
		self.bg = pygame.image.load('../graphics/main/map.png').convert()
		self.fg = pygame.image.load('../graphics/main/overlay.png').convert_alpha()
		#this offsets everything by x pixels
	def customize_draw(self):
		#change the offset vector
		self.offset.x = player.rect.centerx -WINDOW_WIDTH/2
		self.offset.y = player.rect.centery - WINDOW_HEIGHT/2

		#blit th bg
		display_surface.blit(self.bg, -self.offset)
		#display surf is global
		for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery): #accesses all sprites
			#looks at all sprites and passes into lambda function, looks for th y positions and then th sprite looks at th list in th order of tht
			#will want to sort by th y position
			#an excersize to draw a rectangle instead
			# size = sprite.rect.size
			# surf = pygame.Surface(size)#new surface
			# surf.fill('green')
			#give an offset to drawing
			offset_pos = sprite.rect.topleft - self.offset #subtract instead so offset is a negative value and moves in th opposite direction
			display_surface.blit(sprite.image, offset_pos) #blit th rect and th image
		display_surface.blit(self.fg, -self.offset)

#basic stuff
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Frogger')
clock = pygame.time.Clock()

#group
all_sprites = AllSprites() #all same group

#sprites
player = Player((600,400), all_sprites)
car = Car((600,200), all_sprites)

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
	#all_sprites.draw(display_surface)
	all_sprites.customize_draw()

	#update the display surface -> drawing the frame
	pygame.display.update()