import pygame

class Timer:
	def __init__(self, duration, func = None):
		#func for if we want to execute code when wheres off
		self.duration = duration
		self.func = func
		self.start_time = 0
		self.active = False

	def activate(self):
		self.active = True
		self.start_time = pygame.time.get_ticks() #numbers all relative

	def deactivate(self):
		self.active = False
		self.start_time = 0

	def update(self):
		current_time = pygame.time.get_ticks() #will always get th current time
		if current_time - self.start_time >= self.duration:
			self.deactivate()
			if self.func:
				self.func
