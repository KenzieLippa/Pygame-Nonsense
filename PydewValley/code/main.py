#import stuff
#keep clean as possible
import pygame, sys
from settings import *
from level import Level
class Game:
	def __init__(self):
		#initiate and create basics
		pygame.init()
		self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		pygame.display.set_caption('Pydew valley')
		self.clock = pygame.time.Clock()
		self.level = Level()

	def run(self):
		#game loop
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			#get delta time
			dt = self.clock.tick()/1000
			#call here before the update, can run game in this methoda
			self.level.run(dt) #need this in order to run
			pygame.display.update()


#check if in main file, create an object and then run it
if __name__ == '__main__':
	game = Game()
	game.run()
		