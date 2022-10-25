import pygame
from settings import *

class Transition:
	def __init__(self, reset, player):

		#setup
		self.display_surface = pygame.display.get_surface() #get th display surface
		self.reset = reset
		self.player = player

		#overlay image
		#create a black image and change the transparency
		self.image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)) #surface the size of window
		self.color = 255
		self.speed = -2

	def play(self):
		self.color += self.speed
		#prevent crashing
		if self.color <=0:
			self.speed *= -1
			self.color = 0
			self.reset()
		if self.color > 255:
			self.color = 255
			self.player.sleep = False
			self.speed = -2
		self.image.fill((self.color,self.color,self.color,))
		#blends so its more of an alpha adjustment then an actual white to black
		self.display_surface.blit(self.image,(0,0), special_flags = pygame.BLEND_RGBA_MULT) #gets rid of th white values
