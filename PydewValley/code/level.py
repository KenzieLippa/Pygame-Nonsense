import pygame
from settings import *
from player import Player
from overlay import Overlay
from sprites import Generic, Water, WildFlower, Tree
from pytmx.util_pygame import load_pygame
from support import *

class Level:
	#only has one method
	def __init__(self):
		#allows the level to draw on the display
		self.display_surface = pygame.display.get_surface()

		#sprite groups
		self.all_sprites = CameraGroup() #replace the default camera group with this custom one
		self.collision_sprites = pygame.sprite.Group() #keep track of which sprites people can collide with
		self.tree_sprites = pygame.sprite.Group() #all of trees we create add to this

		self.setup()
		self.overlay = Overlay(self.player)


	def setup(self):

		#want to import map tmx
		tmx_data = load_pygame('../data/map.tmx')
		#build the house by importing all layers seperately
		#house furniture is being created after and this is critical in makign sure you can see the floor and the rugs
		for layer in ['HouseFloor', 'HouseFurnitureBottom']:
			for x,y, surf in tmx_data.get_layer_by_name(layer).tiles(): #import them by tiles
				Generic((x*TILE_SIZE, y* TILE_SIZE), surf, self.all_sprites, LAYERS['house bottom'])

		for layer in ['HouseWalls', 'HouseFurnitureTop']:
			for x,y, surf in tmx_data.get_layer_by_name(layer).tiles(): #import them by tiles
				Generic((x*TILE_SIZE, y* TILE_SIZE), surf, self.all_sprites)

		#also need the fence
		for x,y, surf in tmx_data.get_layer_by_name('Fence').tiles(): #import them by tiles
				Generic((x*TILE_SIZE, y* TILE_SIZE), surf, [self.all_sprites, self.collision_sprites])

		#water
		water_frames = import_folder('../graphics/water')
		for x,y, surf in tmx_data.get_layer_by_name('Water').tiles(): #import them by tiles
			Water((x*TILE_SIZE, y* TILE_SIZE), water_frames, self.all_sprites)

		#trees
		for obj in tmx_data.get_layer_by_name('Trees'):
			#all sprites has to be first
			Tree((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites, self.tree_sprites], obj.name)

		#wildflowers
		#theyre on an object layer so its a bit different, watch his tiled video after this course to learn more
		for obj in tmx_data.get_layer_by_name('Decoration'):
			#obj has location and surface
			WildFlower((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites])#actual pixel positions so no mult

		#collision tiles
		for x,y, surf in tmx_data.get_layer_by_name('Collision').tiles():
			Generic((x*TILE_SIZE,y*TILE_SIZE), pygame.Surface((TILE_SIZE, TILE_SIZE)), self.collision_sprites) #not in all sprites so it isnt drawn or updated

		Generic((0,0),pygame.image.load('../graphics/world/ground.png').convert_alpha(),self.all_sprites, LAYERS['ground'])
		for obj in tmx_data.get_layer_by_name('Player'):
			if obj.name == 'Start':
				self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites, self.tree_sprites) # create the player
		#player is not in th collision sprites but has access to th list


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
			for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery): #rn just cycling through but we want to sort this instead
				#th further down th center the later it shld be drawn
			#all tht happens in a normal group with th draw method
				if sprite.z == layer:
					offset_rect = sprite.rect.copy()
					offset_rect.center -=self.offset
					#only if its th current layer draw it
					#draws in order of layer value rather than the order they called
					self.display_surface.blit(sprite.image, offset_rect)

				#analytics
					# if sprite == player:
					# 	#print(sprite.image)
					# 	#drawing two rects and a circle
					# 	#player rectangle
					# 	pygame.draw.rect(self.display_surface, 'red', offset_rect, 5)
					# 	hitbox_rect = player.hitbox.copy()
					# 	#player hitbox
					# 	hitbox_rect.center = offset_rect.center
					# 	pygame.draw.rect(self.display_surface, 'green', hitbox_rect, 5)
					# 	#player target position
					# 	target_pos = offset_rect.center + PLAYER_TOOL_OFFSET[player.status.split('_')[0]]
					# 	pygame.draw.circle(self.display_surface, 'blue', target_pos, 5)