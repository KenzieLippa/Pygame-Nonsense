import pygame
from settings import *

class Generic(pygame.sprite.Sprite):
	def __init__(self,pos,surf,groups, z= LAYERS['main']):
		#need position, surface going to import or use and its group
		#might add diff things and what group part of
		super().__init__(groups)
		self.image = surf
		self.rect = self.image.get_rect(topleft = pos)
		self.z = z
		
