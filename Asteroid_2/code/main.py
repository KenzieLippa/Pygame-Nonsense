#import stuff
import pygame, sys

class Ship(pygame.sprite.Sprite):
	#taking the basics of the sprite class and then changing it
	def __init__(self, groups):
		#runs when we create an object
		super().__init__(groups) # init the parent class
		#need a surface image
		self.image = pygame.image.load('../graphics/ship.png').convert_alpha() # load up image into image property
		self.rect = self.image.get_rect(center = (WINDOW_WIDTH/ 2, WINDOW_HEIGHT/2))
		#need all of these in order to avoid errors

class laser(pygame.sprite.Sprite):
	def __init__(self, groups, xpos, ypos):
		super().__init__(groups)
		self.image = pygame.image.load('../graphics/laser.png').convert_alpha()
		self.rect = self.image.get_rect(bottomcenter = (xpos, ypos))
#initialize
pygame.init()

#putting in variables
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720

#create the window
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Astroid Killer Improved')

#clock object
clock = pygame.time.Clock()
#background
background_surf = pygame.image.load('../graphics/background.png').convert_alpha()
#sprite groups 
spaceship_group = pygame.sprite.Group()
#sprite creation
ship = Ship(spaceship_group) #to display a sprite you need a sprite group which is responsible for drawing sprites
#spaceship_group.add(ship)
#main gameplay loop
while True:

	#event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	#delta time
	dt = clock.tick()/1000

	#background
	display_surface.blit(background_surf,(0,0))

	#graphics 
	spaceship_group.draw(display_surface) #draws the sprite onto the surface
	#draw frame
	pygame.display.update()