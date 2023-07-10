import pygame    
from settings import *
from support import *
from timer import Timer

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, group, collision_sprites, tree_sprites, interaction, soil_layer, toggle_shop):
		#as created becomes in th class
		super().__init__(group)
		#run this early
		self.import_assets()
		#which one are we in rn
		#this one will be th folder
		self.status = 'down_idle'
		#what is our current frame
		self.frame_index = 0 

		#when creating the image will need th animation
		#general setup
		self.image = self.animations[self.status][self.frame_index] #using the dictionary key and then specify the frame
		#self.image.fill('green')
		#want ints for this instead of floating points
		self.rect = self.image.get_rect(center = pos) #create player rectangle
		
		self.z = LAYERS['main']

		#movement variables
		self.direction = pygame.math.Vector2()#changes with 1 and -1 depending on ur direction
		self.pos = pygame.math.Vector2(self.rect.center)
		self.speed = 400 #player speed

		#collision
		self.hitbox = self.rect.copy().inflate((-126, -70))#keeps it centered but changes size
		self.collision_sprites = collision_sprites
		self.soil_layer = soil_layer
		self.toggle_shop = toggle_shop

		#timers
		self.timers = {
		#the name and then th timer
			'tool_use': Timer(350, self.use_tool),
			'tool_switch': Timer(200),
			'seed_use': Timer(350, self.use_seed),
			'seed_switch': Timer(200)
		}

		#tools
		self.tools = ['hoe', 'axe', 'water']
		self.tool_index = 0
		self.selected_tool = self.tools[self.tool_index]

		#seeds
		self.seeds = ['corn', 'tomato']
		self.seed_index = 0
		self.selected_seed = self.seeds[self.seed_index]
		#dont use the rect for collisions bc it is much larger than th image and u dnt want tht to be ur collision cause it will look terrible

		#inventory
		self.item_inventory = {
			'wood': 0,
			'apple': 0,
			'corn': 0,
			'tomato': 0
		}
		self.seed_inventory = {
			'corn':5,
			'tomato':5
		}

		self.money = 200 #starting money

		#interaction
		self.tree_sprites = tree_sprites
		self.interaction = interaction #now player knows where these types of sprites are
		self.sleep = False

		#sound
		self.watering = pygame.mixer.Sound('audio/water.mp3')
		self.watering.set_volume(0.2)

	def use_tool(self):
		#make sure it works
		#print(self.selected_tool)
		if self.selected_tool == 'hoe':
			self.soil_layer.get_hit(self.target_pos)
		if self.selected_tool == 'axe':
			#print('the axe was attempted')
			for tree in self.tree_sprites.sprites():
				if tree.rect.collidepoint(self.target_pos):
					tree.damage()
					#print('tool was used')
		if self.selected_tool == 'water':
			self.soil_layer.water(self.target_pos)
			self.watering.play()

	def get_target_pos(self):
		self.target_pos = self.rect.center + PLAYER_TOOL_OFFSET[self.status.split('_')[0]]#creates the target position
	def use_seed(self):
		if self.seed_inventory[self.selected_seed] >0:
			self.soil_layer.plant_seed(self.target_pos, self.selected_seed) #where are we hitting and what are we planting
			self.seed_inventory[self.selected_seed] -= 1

	def import_assets(self):
		#animations dictionary with all th categories


		#same as folder
		self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
							'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
							'right_hoe': [], 'left_hoe': [], 'up_hoe': [], 'down_hoe': [],
							'right_axe': [], 'left_axe': [], 'up_axe': [], 'down_axe': [],
							'right_water': [], 'left_water': [], 'up_water': [], 'down_water': []}
		for animation in self.animations.keys():
			full_path = 'graphics/character/' + animation #name is also th folder name
			self.animations[animation] = import_folder(full_path) #use this method to import th folder
		#print(self.animations)


	def animate(self,dt):
		self.frame_index += 5* dt #increase to hit all values but this will return a float
		#print(int(self.frame_index))
		#a bit clunky but can always fix later
		if self.frame_index >= len(self.animations[self.status]):
			self.frame_index = 0
		self.image = self.animations[self.status][int(self.frame_index)]
		

	def input(self):
		keys = pygame.key.get_pressed() #returns list of all things potentially being pressed

		#directions
		if not self.timers['tool_use'].active and not self.sleep:
			if keys[pygame.K_w]:
				#print('up')
				self.direction.y = -1
				self.status = 'up'

			elif keys[pygame.K_s]:
				#print('down')
				self.direction.y = 1
				self.status = 'down'
			else:
				#make sure it gets reset so it doesnt move forever
				self.direction.y = 0


			if keys[pygame.K_d]:
				#print('right')
				self.direction.x = 1
				self.status = 'right'
			elif keys[pygame.K_a]:
				#print('left')
				self.direction.x = -1
				self.status = 'left'
			else:
				self.direction.x = 0

			#print(self.direction)

			#tool use
			if keys[pygame.K_SPACE]:
				#timer for the tool use
				self.timers['tool_use'].activate()
				self.direction = pygame.math.Vector2() #set vector to 0 so you cant move while ur using th tool
				#want to play a new animation but th old animation cld be on a different frame so u shld reset it
				self.frame_index = 0 #make sure it starts at the beginning

			#change tool
			if keys[pygame.K_q] and not self.timers['tool_switch'].active:
				self.timers['tool_switch'].activate()
				self.tool_index += 1
				print(self.tool_index)
				#if tool index greater than tool length then set to 0
				self.tool_index = self.tool_index if self.tool_index < len(self.tools) else 0
				self.selected_tool = self.tools[self.tool_index]


			#seed use
			if keys[pygame.K_p]:
				#timer for the tool use
				self.timers['seed_use'].activate()
				self.direction = pygame.math.Vector2() #set vector to 0 so you cant move while ur using th tool
				#want to play a new animation but th old animation cld be on a different frame so u shld reset it
				self.frame_index = 0 #make sure it starts at the beginning
				#print('use seed')

			#change seed
			if keys[pygame.K_e] and not self.timers['seed_switch'].active:
				self.timers['seed_switch'].activate()
				self.seed_index += 1
				print(self.seed_index)
				#if tool index greater than tool length then set to 0
				self.seed_index = self.seed_index if self.seed_index < len(self.seeds) else 0
				self.selected_seed = self.seeds[self.seed_index]
				print(self.selected_seed)

			if keys[pygame.K_RETURN]:
				#self.toggle_shop()
				collided_interaction_sprite = pygame.sprite.spritecollide(sprite = self, group = self.interaction, dokill = False)
				if collided_interaction_sprite:
					if collided_interaction_sprite[0].name == 'Trader':
						self.toggle_shop() #basically will toggle a shop
					else:
						self.status = 'left_idle' #player point towards the bed 
						self.sleep = True #now the player is sleeping, can start transition
	def get_status(self):
		#check if the player is not moving, then add _idle to th status
		#idle
		if self.direction.magnitude() == 0:
			self.status = self.status.split('_')[0] + '_idle' #break at th underscore so tht there wont be more than one underscore idle


		#tool use
		if self.timers['tool_use'].active:
			#print('tool is being used')
			self.status = self.status.split('_')[0] + '_' + self.selected_tool

	def update_timers(self):
		for timer in self.timers.values():
			#call th update method on th timer
			timer.update()

	def collision(self, direction):
		for sprite in self.collision_sprites.sprites():
			#look for th hit box
			if hasattr(sprite, 'hitbox'):
				#checks to see if the sprite has a hitbox, make sure anyhow in case theres an error
				if sprite.hitbox.colliderect(self.hitbox):
					#if the hitbox on th sprite collides with us
					#seperate the direction
					if direction == 'horizontal':
						if self.direction.x > 0:
							#this means we moving right
							self.hitbox.right = sprite.hitbox.left #set our hitbox to be at tht beginning of th obstacles left side
						if self.direction.x <0:
							self.hitbox.left = sprite.hitbox.right
						#update the self rect
						self.rect.centerx = self.hitbox.centerx
						self.pos.x = self.hitbox.centerx #this is for th horizontal
					if direction == 'vertical':
						if self.direction.y > 0: #moving down
							#this means we moving right
							self.hitbox.bottom = sprite.hitbox.top#put th bottom of th player at th top of th obstacle
						if self.direction.y <0: #moving up
							self.hitbox.top = sprite.hitbox.bottom
						#update the self rect
						self.rect.centery = self.hitbox.centery
						self.pos.y = self.hitbox.centery #this is for th horizontal



	def move(self, dt):
		#move self.pos, 
		#normalize the vector to make sure its 1 instead of 1.4 on th diags
		#needs to know the direction cause cant normalize 0
		if self.direction.magnitude() >0:
			self.direction = self.direction.normalize()

		#later for collisions this will be helpful
		#horizontal movement
		#update x only
		self.pos.x += self.direction.x * self.speed * dt
		self.hitbox.centerx = round(self.pos.x)#dont truncate the value from 1.9 to 1 
		self.rect.centerx = self.hitbox.centerx
		self.collision('horizontal') #this is why we seperated from length to width


		#vertical movement
		self.pos.y += self.direction.y * self.speed * dt
		self.hitbox.centery = round(self.pos.y)
		self.rect.centery = self.hitbox.centery
		self.collision('vertical')


	

	def update(self, dt):
		self.input()
		self.get_status()

		self.update_timers()
		self.get_target_pos()
		self.move(dt)
		self.animate(dt)
