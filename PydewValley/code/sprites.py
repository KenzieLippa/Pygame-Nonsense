import pygame
from settings import *
from random import randint, choice
from timer import Timer
class Generic(pygame.sprite.Sprite):
	def __init__(self,pos,surf,groups, z= LAYERS['main']):
		#need position, surface going to import or use and its group
		#might add diff things and what group part of
		super().__init__(groups)
		self.image = surf
		self.rect = self.image.get_rect(topleft = pos)
		self.z = z
		self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.2, -self.rect.height * 0.75)#for width u dnt wanna shrink too much
		#for height u want a larger number so u can interact better and actually go behind things


class Water(Generic):
	def __init__(self, pos, frames, groups):
		#water is going to be animated

		#animation setup
		self.frames = frames
		self.frame_index = 0

		#sprite setup
		super().__init__(pos, self.frames[self.frame_index], groups, LAYERS['water'])

	def animate(self, dt):
		self.frame_index += 5 * dt
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]

	def update(self, dt):
		self.animate(dt)#run the animation

class WildFlower(Generic):
	def __init__(self, pos, surf, groups):
		super().__init__(pos, surf, groups)
		self.hitbox = self.rect.copy().inflate(-20, -self.rect.height * 0.9)
class Particle(Generic):
	def __init__(self, pos, surf, groups, z, duration = 200):
		super().__init__(pos,surf,groups, z)
		self.start_time = pygame.time.get_ticks()#only taken once
		self.duration = duration

		#white surface
		mask_surf = pygame.mask.from_surface(self.image)
		new_surf = mask_surf.to_surface()
		new_surf.colorkey((0,0,0))
		self.image = new_surf

	def update(self,dt):
		current_time = pygame.time.get_ticks()#updated continuously
		if current_time - self.start_time > self.duration:
			self.kill()


class Tree(Generic):
	def __init__(self, pos, surf, groups, name):
		#will need a name for the tree to see if small or large
		super().__init__(pos, surf, groups) #later will be more extenssive but this gets them in
		#can take the hitbox from the generic
		#tree attributes
		self.health = 5
		self.alive = True
		stump_path = f'../graphics/stumps/{"small" if name == "Small" else "large"}.png'
		self.stump_surf = pygame.image.load(stump_path).convert_alpha()
		self.invul_timer = Timer(200) #make a new timer
		#apples
		self.apple_surf = pygame.image.load('../graphics/fruit/apple.png')

		#list of possible positions for th apple
		self.apple_pos = APPLE_POS[name] #figure out th possible using small or large
		self.apple_sprites = pygame.sprite.Group()
		self.create_fruit()

	def damage(self):
		#damages the tree
		self.health -= 1
		#print(self.health)

		#remove an apple if there is one if hit
		if len(self.apple_sprites.sprites()) > 0:
			#pick a random apple
			random_apple = choice(self.apple_sprites.sprites())
			random_apple.kill()

	def check_death(self):
		if self.health <= 0:
			self.image = self.stump_surf
			self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
			self.hitbox = self.rect.copy().inflate(-10, -self.rect.height * 0.6)
			self.alive = False
	def update(self,dt):
		if self.alive:
			self.check_death()#if your currently alive check to see if you arent
			#always start with implementing func first then add th actual function

	def create_fruit(self):
		for pos in self.apple_pos:
			#random number generator to see if u wanna make an apple or na
			if randint(0,10) < 2 :
				#create an apple if random number less than 2
				x =pos[0]+ self.rect.left #this is the x, it tells how far from th tree we wanna go
				y = pos[1] + self.rect.top #these are where the object is, basically adds the coords from th setting to th position of th tree to get th pos of th apple
				Generic((x,y), self.apple_surf, [self.apple_sprites, self.groups()[0]], LAYERS['fruit'])#will be a generic object and call the sprite groups to get access to the first group bc there is no all sprites group here
				#positions are based on th tree not th game window

