import pygame
from settings import *
from player import Player
from overlay import Overlay
from sprites import Generic
from pytmx.util_pygame import load_pygame

class Level:
	#only has one method
	def __init__(self):
		#allows the level to draw on the display
		self.display_surface = pygame.display.get_surface()

		#sprite groups
		self.all_sprites = CameraGroup() #replace the default camera group with this custom one

		self.setup()
		self.overlay = Overlay(self.player)

	def setup(self):

		Generic((0,0),pygame.image.load('../graphics/world/ground.png').convert_alpha(),self.all_sprites, LAYERS['ground'])
		self.player = Player((640,360), self.all_sprites) # create the player


	def run(self, dt):
		#print('run game')
		self.display_surface.fill('black') #dont see th previous frame
		
		#hve both methods, calls on all children
		#self.all_sprites.draw(self.display_surface)
		#dont need display surface for this
		self.all_sprites.custom_draw(self.player)
		#calls players update method 
		self.all_sprites.update(dt) #updates all sprites
		self.overlay.display()


class CameraGroup(pygame.sprite.Group):
	#create special type of group and get camera here
	def __init__(self):
		super().__init__() #once have this implimented u can customize
		self.display_surface = pygame.display.get_surface() #can draw on surface right away
		self.offset = pygame.math.Vector2()

	def custom_draw(self,player):
		#actually draw the map in the offset chords even tho it looks like th camera is moving, th image is in th same place but th rect is moving
		self.offset.x = player.rect.centerx-SCREEN_WIDTH/2
		self.offset.y = player.rect.centery-SCREEN_HEIGHT/2 #how much shift every stride by the player
		for layer in LAYERS.values():
			#check if sprite.z is the layer
			for sprite in self.sprites():
			#all tht happens in a normal group with th draw method
				if sprite.z == layer:
					offset_rect = sprite.rect.copy()
					offset_rect.center -=self.offset
					#only if its th current layer draw it
					#draws in order of layer value rather than the order they called
					self.display_surface.blit(sprite.image, offset_rect)
