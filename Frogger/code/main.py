import pygame, sys
from settings import * #import all variables from setting
from player import Player
from car import Car
from random import choice, randint
from sprite import SimpleSprite, LongSprite

class AllSprites(pygame.sprite.Group):
	#take original group and make changes
	def __init__(self):
		super().__init__()
		self.offset = pygame.math.Vector2() #changing this changes where he is but allows you to still move everything th same
		self.bg = pygame.image.load('graphics/main/map.png').convert()
		self.fg = pygame.image.load('graphics/main/overlay.png').convert_alpha()
		#this offsets everything by x pixels
	def customize_draw(self):
		#change the offset vector
		self.offset.x = player.rect.centerx -WINDOW_WIDTH/2
		self.offset.y = player.rect.centery - WINDOW_HEIGHT/2

		#blit th bg
		display_surface.blit(self.bg, -self.offset)
		#display surf is global
		#updates and draws every frame
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
#cant check this for collision because then would be checking if it collided with itself which is always true
#create a new group for collisions
obstacle_sprites = pygame.sprite.Group() #can assign to multiple groups easily

#sprites
player = Player((2062,3274), all_sprites, obstacle_sprites)
#car = Car((600,200), all_sprites)
#remove the car that isnt needed anymore

#timer
car_timer = pygame.event.custom_type()
pygame.time.set_timer(car_timer, 500) #slowed down to prevent crashing
pos_list = []

#font
font = pygame.font.Font(None, 50)
text_surf = font.render('VICTORY!!', True, 'White')
text_rect = text_surf.get_rect(center = (WINDOW_WIDTH /2, WINDOW_HEIGHT /2))
#music
music = pygame.mixer.Sound('audio/music.mp3')
music.play(loops = -1)
#create sprite setup
#look at simple objects in settings and cycle through
#value of the key is all th positions where we wanna create the sprite
for file_name, pos_list in SIMPLE_OBJECTS.items():
	#getting keys in values in one cycle
	#getting and saving info
	path = f'graphics/objects/simple/{file_name}.png' #no file pngs in th thingy
	#load the surface
	surf = pygame.image.load(path).convert_alpha()
	for pos in pos_list:
		#we want to create a simple sprite at the location
		#passing to two groups as a list and passing in th super init method to assign
		SimpleSprite(surf, pos, [all_sprites, obstacle_sprites])

#setting up the long objects sprites
#need a sprite class and then we need to cycle over th dict
for file_name, pos_list in LONG_OBJECTS.items():
	surf = pygame.image.load(f'graphics/objects/long/{file_name}.png').convert_alpha()
	for pos in pos_list:
		#create our long sprite
		LongSprite(surf, pos, [all_sprites, obstacle_sprites])

#game loop
while True:

	#event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == car_timer:
			#print('car') #see if this works, if the event type is the car timer then print
			random_pos = choice(CAR_START_POSITIONS)
			if random_pos not in pos_list:
				#add pos to the pos list so it cant be added again
				pos_list.append(random_pos)
				pos = (random_pos[0], random_pos[1] + randint(-8,8)) #can add to it because we are creating a new tuple
			#my attempt to spawn the cars
				Car(pos, [all_sprites, obstacle_sprites]) #in both groups and can be accessed from either
			if len(pos_list) > 5:
				del pos_list[0]
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
	if player.pos.y >= 1180:
		all_sprites.update(dt)

		#draw
		#all_sprites.draw(display_surface)
		all_sprites.customize_draw()
	else:
		display_surface.blit(text_surf, text_rect)

	#update the display surface -> drawing the frame
	pygame.display.update()