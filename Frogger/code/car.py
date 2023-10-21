import pygame
from os import walk
from random import choice

class Car(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.name = 'car'
		#random car from th cars folder
		#how to pick one item from a list at random random.choice(list)
		#walk gives you these three variables when you use it
		for folder_name, sub_folders, img_list in walk('graphics/cars'):
			car_name = choice(img_list) #just a name at this point

		self.image  = pygame.image.load('graphics/cars/' +car_name).convert_alpha()
		self.rect = self.image.get_rect(center = pos)
		#print('car made')

		#float based movement 
		self.pos = pygame.math.Vector2(self.rect.center)

		if pos[0] < 200:
			#will do bellow 0 later
			self.direction = pygame.math.Vector2(1,0)

		else:
			self.direction = pygame.math.Vector2(-1,0)
			self.image = pygame.transform.flip(self.image, True, False) #first flips x then flips y and we only wanna flip x
		
		self.speed = 300
		self.hitbox = self.rect.inflate(0, -self.rect.height / 2)

	def update(self, dt):
		#need self and delta time
		self.pos += self.direction*self.speed*dt
		self.hitbox.center = (round(self.pos.x), round(self.pos.y))
		self.rect.center = self.hitbox.center
		#kill car if out of th window
		if not -200 < self.rect.x < 3000:
			#if th car is not in this range
			#then destroy the car
			#print('car killed')
			self.kill()
