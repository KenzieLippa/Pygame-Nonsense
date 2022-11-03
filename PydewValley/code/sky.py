import pygame
from settings import *
from support import import_folder
from sprites import Generic
from random import randint, choice
class Drop(Generic):
	#import the generic class
	def __init__(self, surf, pos, moving, groups, z):
		#kind of like a particle, create for short period and then destroy it
		#general setup
		super().__init__(pos, surf, groups, z)
		self.lifetime = randint(400,500)
		self.start_time = pygame.time.get_ticks()

		#need to work on moving
		#if we have a rain drop then it goes down whereas the ones on th bottom stay in place
		self.moving = moving
		if self.moving:
			self.pos = pygame.math.Vector2(self.rect.topleft)
			self.direction = pygame.math.Vector2(-2,4) #this is th direction we are going
			self.speed = randint(200,250) #similar to the player method for moving, need these to move things
	def update(self, dt):
		if self.moving:
			self.pos += self.direction * self.speed *dt
			self.rect.topleft = (round(self.pos.x), round(self.pos.y)) #round avoids truncation

		#need a timer
		if pygame.time.get_ticks() - self.start_time >= self.lifetime:
			self.kill() #murder self if exceeded lifetime

class Rain:
	def __init__(self, all_sprites):
		#so we can draw in here without leaving th class
		self.all_sprites = all_sprites
		#have two folders, one for drops and one for floor
		#have an animation for th floor
		self.rain_drops = import_folder('../graphics/rain/drops/')
		self.rain_floor = import_folder('../graphics/rain/floor/')

		#need the size of the entire map
		#want to create random animations in each area
		self.floor_w, self.floor_h = pygame.image.load('../graphics/world/ground.png').get_size()


	def create_floor(self):
		Drop(surf = choice(self.rain_floor), 
		pos = (randint(0,self.floor_w),randint(0, self.floor_h)),
		moving = False,
		groups = self.all_sprites, 
		z = LAYERS['rain floor']) #create a drop class


	def create_drops(self):
		Drop(surf = choice(self.rain_drops), 
		pos = (randint(0,self.floor_w),randint(0, self.floor_h)),
		moving = True,
		groups = self.all_sprites, 
		z = LAYERS['rain drops'])


	def update(self):
		self.create_floor()
		self.create_drops()




