#import stuff
import pygame, sys
from random import randint, uniform
class Ship(pygame.sprite.Sprite):
	#taking the basics of the sprite class and then changing it
	#use masks for pixel perfect collisions
	def __init__(self, groups):
		#runs when we create an object
		super().__init__(groups) # init the parent class
		#need a surface image
		self.image = pygame.image.load('../graphics/ship.png').convert_alpha() # load up image into image property
		self.rect = self.image.get_rect(center = (WINDOW_WIDTH/ 2, WINDOW_HEIGHT/2))
		#need all of these in order to avoid errors
		#timer variables
		self.mask = pygame.mask.from_surface(self.image)#needs to be called mask, data structure to tell which pixels are occupied and which are not
		self.can_shoot = True
		self.shoot_time = None

		#sound 
		self.laser_sound = pygame.mixer.Sound('../sounds/laser.ogg')
	#can create more methods and then call them in th update method instead of game loop for cleanliness
	def laser_timer(self):
		if not self.can_shoot:
			#if you use attributes then it recognizes that its the same as the property and therefore does not need to be returned
			#only runs if can shoot is false, otherwise no reason to recharge
			current_time = pygame.time.get_ticks()
			#self.shoottime is a class specific property
			if current_time - self.shoot_time > 500:
				self.can_shoot = True

	def input_position(self):
		pos = pygame.mouse.get_pos()#get mouse position
		self.rect.center = pos #get the rectangle and set th center to the mouse position

	def laser_shoot(self):


		#easy to foget how things are called, google is so nice
		if(pygame.mouse.get_pressed()[0] and self.can_shoot):
			#print('shoot lalser')
			self.can_shoot = False #set false after shooting and then cant run
			self.shoot_time = pygame.time.get_ticks() #get the time that its shot as
			Laser(self.rect.midtop, laser_group)
			self.laser_sound.play()

	def meteor_collisions(self):
		if pygame.sprite.spritecollide(self, meteor_group, False, pygame.sprite.collide_mask):
			pygame.quit()
			sys.exit()

	def update(self):
		self.laser_timer() #can call anywhere but maybe at the beginning of the frame
		self.input_position()
		self.laser_shoot()
		self.meteor_collisions()

class Laser(pygame.sprite.Sprite):
	def __init__(self, pos, groups):
		super().__init__(groups)
		self.image = pygame.image.load('../graphics/laser.png').convert_alpha()
		self.rect = self.image.get_rect(midbottom = (pos)) #this is so that we can place teh laser next to the ship
		self.mask = pygame.mask.from_surface(self.image)
		#float based position
		#vector with top point of rect
		self.pos = pygame.math.Vector2(self.rect.topleft) #can pass a touple 
		
		#tells which direction the laser is going
		self.direction = pygame.math.Vector2(0,-1)
		self.speed = 800
		#pass in the top left spot

		#sound
		self.explosion_sound = pygame.mixer.Sound('../sounds/explosion.wav')

	def meteor_collision(self):
		#last argument is the sprite collision
		if pygame.sprite.spritecollide(self, meteor_group, True, pygame.sprite.collide_mask):
			self.kill() #kill what ever object created by this class
			self.explosion_sound.play()

	def update(self):
		#update this vector
		#mult and create a new vector for th placement
		self.pos += self.direction * self.speed * dt#only change the y chord
		#start for the positioning
		#turn into rect position
		self.rect.topleft = (round(self.pos.x), round(self.pos.y)) #set the rectangle to the new position and then run to prevent truncation
		#self.rect.y -= 10
		if self.rect.bottom < 0:
			self.kill()
		self.meteor_collision()

class Meteor(pygame.sprite.Sprite):
	def __init__(self, pos, groups):
		super().__init__(groups)
		#randomize the size
		meteor_surf = pygame.image.load('../graphics/meteor.png').convert_alpha()
		meteor_size = pygame.math.Vector2(meteor_surf.get_size()) * uniform(0.5,1.5)#want proportionate
		self.scaled_surf = pygame.transform.scale(meteor_surf
			, meteor_size) #original surface
		self.image = self.scaled_surf
		self.rect = self.image.get_rect(center = pos)
		self.mask = pygame.mask.from_surface(self.image)
		#float based positioning
		self.pos = pygame.math.Vector2(self.rect.topleft)
		self.direction = pygame.math.Vector2(uniform(-0.5, 0.5),1)
		self.speed = randint(400,600)

		#rotation logic
		self.rotation = 0
		self.rotation_speed = randint(20,50)

	def rotate(self):
		self.rotation += self.rotation_speed * dt #for anything animated
		rotate_surf = pygame.transform.rotozoom(self.scaled_surf, self.rotation, 1)
		#rotate image and set it as th main image
		self.image = rotate_surf
		self.rect = self.image.get_rect(center = self.rect.center)#reset the rect 
		#have to rewrite the mask too
		self.mask = pygame.mask.from_surface(self.image)

	def update(self):
		self.pos += self.direction * self.speed * dt#only change the y chord
		
		self.rect.topleft = (round(self.pos.x), round(self.pos.y)) #set the rectangle to the new position and then run to prevent truncation
		self.rotate()
		if self.rect.top > WINDOW_HEIGHT:
			self.kill()


class Score:
	def __init__(self):
		self.font = pygame.font.Font('../graphics/subatomic.ttf', 50)

	def display(self):
		#display the score of the player
		#used only in th func so keep them here
		score_text = f'Score: {pygame.time.get_ticks()//1000}'
		text_surf = self.font.render(score_text, True, (255,255,255))
		text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH /2, WINDOW_HEIGHT -80))
		display_surface.blit(text_surf, text_rect)
		pygame.draw.rect(
			display_surface, 
			(255,255,255), 
			text_rect.inflate(30,30), 
			width = 8, 
			border_radius = 5)

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
spaceship_group = pygame.sprite.GroupSingle()
laser_group = pygame.sprite.Group()
meteor_group = pygame.sprite.Group()
#sometimes a group only has one sprite instead, there is a specific group
#sprite creation
ship = Ship(spaceship_group) #to display a sprite you need a sprite group which is responsible for drawing sprites
#laser = Laser((100,300), laser_group)
#spaceship_group.add(ship)
#main gameplay loop
#timer
meteor_timer = pygame.event.custom_type() #make a new event flag
pygame.time.set_timer(meteor_timer, 400) #pygame timer sets off meteor creation every 400 mil
#create score
score = Score()

#music
bg_music = pygame.mixer.Sound('../sounds/music.wav')
bg_music.play(loops = -1)

while True:

	#event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == meteor_timer:
			meteor_y_pos = randint(-150,150)#second needs to be larger
			meteor_x_pos = randint(- 100, WINDOW_WIDTH +100)
			Meteor((meteor_x_pos, meteor_y_pos),meteor_group)

	#delta time
	dt = clock.tick()/1000

	#background
	display_surface.blit(background_surf,(0,0))


	#update
	#call the group itself and it will call the update method on all sprites in group
	#can do this with other methods and then call them inside the update method instead of the game loop
	spaceship_group.update()
	laser_group.update()
	meteor_group.update()
	#score
	score.display()
	#graphics 
	spaceship_group.draw(display_surface) #draws the sprite onto the surface
	laser_group.draw(display_surface)
	meteor_group.draw(display_surface)
	#draw frame
	pygame.display.update()