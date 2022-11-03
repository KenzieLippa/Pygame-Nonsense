import pygame
from settings import *
from pytmx.util_pygame import load_pygame
from support import *
from random import choice
class SoilTile(pygame.sprite.Sprite):
	def __init__(self, pos, surf, groups):
		super().__init__(groups)
		self.image = surf
		self.rect = self.image.get_rect(topleft = pos)
		self.z = LAYERS['soil']

class WaterTile(pygame.sprite.Sprite):
	def __init__(self, pos, surf, groups):
		super().__init__(groups)
		self.image = surf
		self.rect = self.image.get_rect(topleft= pos)
		self.z = LAYERS['soil water']

class Plant(pygame.sprite.Sprite):
	def __init__(self, plant_type, groups, soil):
		super().__init__(groups) #pass groups into super class

		#setup
		self.plant_type = plant_type
		self.frames = import_folder(f'../graphics/fruit/{plant_type}')#pick th folder with th passed in plant type
		self.soil = soil
		#plant growing
		self.age = 0 #how old is th plant
		self.max_age = len(self.frames) - 1 
		self.grow_speed = GROW_SPEED[plant_type] #how fast it grows

		#sprite setup
		self.image = self.frames[self.age]
		self.y_offset = -16 if plant_type == 'corn' else -8 #plants diff in size
		self.rect = self.image.get_rect(midbottom = soil.rect.midbottom + pygame.math.Vector2(0,self.y_offset))
		self.z = LAYERS['ground plant']

	def grow(self):
		#need to know if it was watered

class SoilLayer:
	def __init__(self, all_sprites):
		#need them visible 

		#sprite groups
		self.all_sprites = all_sprites
		self.soil_sprites = pygame.sprite.Group()
		self.water_sprites = pygame.sprite.Group()
		self.plant_sprites = pygame.sprite.Group()

		#graphics
		#self.soil_surf = pygame.image.load('../graphics/soil/o.png')
		#dont use the support cause we need to know what we working with
		self.soil_surfs = import_folder_dict('../graphics/soil/')
		self.water_surfs =  import_folder('../graphics/soil_water')
		#print(self.soil_surfs)

		self.create_soil_grid()
		self.create_hit_rects()

		#requirements

		#if the area is farmable

		#if the soil has been watered

		#if the soil has a plant already

	def create_soil_grid(self):
		ground = pygame.image.load('../graphics/world/ground.png') #dont have to convert cause not showing to th player
		h_tiles, v_tiles = ground.get_width() //TILE_SIZE, ground.get_height()//TILE_SIZE #floor divide to round down
		# print(h_tiles)
		# print(v_tiles)
		#list comprehension
		#create a list for each tile so we can put th info in there
		#list of lists, in each list we have a list for each row of the game and then inside that list we have a list for each column
		#so for the bg it goes bg1 [row1 [col1[], col2[]], row2[col1[],col2[]]]
		self.grid = [[[] for col in range(h_tiles)] for row in range(v_tiles)]
		#func returns these three elements, using a for loop u can store all th elements in th respective variables
		for x, y, surf in load_pygame('../data/map.tmx').get_layer_by_name('Farmable').tiles(): #allows us to use it all in a for loop
			self.grid[y][x].append('F') #y gets list and so does x then from this list append the F too it so we know its farmable
			# for row in self.grid: #the row is just a variable its not anything created before
			# 	print(row)

	def create_hit_rects(self):
		self.hit_rects = []
		#cycle through th grid and convert into actual positions
		#go through all lists
		#because enumerate the outside argument goes to th first var and th inside argument goes to th second
		for index_row, row in enumerate(self.grid):
			#go through all cells
			for index_col, cell in enumerate(row):
				#list that contains cell lists
				if 'F' in cell:
					x = index_col * TILE_SIZE
					y =  index_row * TILE_SIZE
					rect = pygame.Rect(x,y, TILE_SIZE, TILE_SIZE)
					self.hit_rects.append(rect) #if farmable then you can hit it so add it to th list

	def get_hit(self, point):
		#see if th player has hit th squares
		#you should always code test by test to see if shit works
		for rect in self.hit_rects:
			if rect.collidepoint(point):
				#check to see if coliding
				x = rect.x//TILE_SIZE
				y = rect.y//TILE_SIZE

				if 'F' in self.grid[y][x]:
					self.grid[y][x].append('X')
					self.create_soil_tiles()
					if self.raining:
						self.water_all() #soil layer doesnt know if raining or not

	def water(self, target_pos):
		#check if the target pos hits any of th soil sprites
		for soil_sprite in self.soil_sprites.sprites():
			if soil_sprite.rect.collidepoint(target_pos):
				#print('This tile is now watered')
				#add an entry to the soil grid
				x = soil_sprite.rect.x//TILE_SIZE
				y = soil_sprite.rect.y//TILE_SIZE
				#can use these to find the grid
				
				self.grid[y][x].append('W') #if we watered this tile add a W
				#then create a water sprite to indicate there is water on this tile
				#same position as th soil sprite, surf import the folder with th path and then select randomly a surface
				pos = soil_sprite.rect.topleft
				surf = choice(self.water_surfs)
				WaterTile(pos,surf, [self.all_sprites, self.water_sprites])

	def water_all(self):
		#go through all cells
		for index_row, row in enumerate(self.grid):
			#go through all cells
			for index_col, cell in enumerate(row):
				if 'X' in cell and 'W' not in cell:
					#check if soil tile but hasnt been watered yet
					cell.append('W')
					#have all positions in grid and pixel positions in game
					x = index_col * TILE_SIZE
					y = index_row * TILE_SIZE
					WaterTile((x,y),choice(self.water_surfs), [self.all_sprites, self.water_sprites])


	def remove_water(self):
		#destroy the water sprites
		#clean up the grid
		for sprite in self.water_sprites.sprites():
			sprite.kill()

		for row in self.grid:
			for cell in row:
				if 'W' in cell:
					cell.remove('W')
					#if theres a W then you should remove it

	def check_watered(self, pos):
		#are given pixel position and we need to convert to a grid position
		x = soil_sprite.rect.x // TILE_SIZE
		y = soil_sprite.rect.y // TILE_SIZE
		cell = self.grid[y][x]
		is_watered = 'W' in cell #could either be true or false
		
	def plant_seed(self, target_pos, seed):
		for soil_sprite in self.soil_sprites.sprites():
			if soil_sprite.rect.collidepoint(target_pos):
				#is colliding with th target
				x = soil_sprite.rect.x // TILE_SIZE
				y = soil_sprite.rect.y // TILE_SIZE
				if 'P' not in self.grid[y][x]:
					self.grid[y][x].append('P') # now we know we have a plant in this cell
					Plant(plant_type = seed, groups = [self.all_sprites, self.plant_sprites], soil = soil_sprite) #create plant object

	def create_soil_tiles(self):
		self.soil_sprites.empty() #get rid of all existing soil sprites
		for index_row, row in enumerate(self.grid):
			#go through all cells
			for index_col, cell in enumerate(row):
				#list that contains cell lists
					#print('Farmable')
				if 'X' in cell:

					#tile options
					#know what th neighbors are doing
					t = 'X' in self.grid[index_row-1][index_col]
					b = 'X' in self.grid[index_row+1][index_col]
					r = 'X' in row[index_col+1]
					l = 'X' in row[index_col-1]

					#can add in th corneres later if u want
					tyle_type = 'o'

					#all sides
					if all((t,r,l,b)): tyle_type = 'x'

					#horizontal tyles only, if i have a tile and if theres to th right and to th left
					if l and not any((t,r,b)): tyle_type = 'r' #if only to th left and no where else then it creates it
					if r and not any((t,l,b)): tyle_type = 'l'
					if r and l and not any((t, b)): tyle_type = 'lr'

					#vertical only
					if t and not any((r,l,b)): tyle_type = 'b'
					if b and not any((r,l,t)): tyle_type = 't'
					if b and t and not any((r,l)): tyle_type = 'tb'

					#coreners
					if l and b and not any((t,r)): tyle_type = 'tr'
					if r and b and not any((t,l)): tyle_type = 'tl'
					if l and t and not any((b,r)): tyle_type = 'br'
					if r and t and not any((b,l)): tyle_type = 'bl'

					#t shapes


					if all((t,b,r)) and not l: tyle_type = 'tbr'
					if all((t,b,l)) and not r: tyle_type = 'tbl'
					if all((l,t,r)) and not b: tyle_type = 'lrb'
					if all((b,l,r)) and not t: tyle_type = 'lrt'

					SoilTile((index_col * TILE_SIZE, index_row * TILE_SIZE), self.soil_surfs[tyle_type], [self.all_sprites, self.soil_sprites])




