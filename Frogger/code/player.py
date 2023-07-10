import pygame, sys
from os import walk #walks through folder and gives you the names of folders and names of items inside
class Player(pygame.sprite.Sprite):
	def __init__(self, pos, groups, collision_sprites):
		super().__init__(groups)
		self.import_assets()
		#for animation then change it fast
		#will have to import a lot of different graphics
		self.frame_index = 0
		self.status = 'up' #one key value pair in animations, returns a list
		#self.image = self.animation[self.frame_index]
		self.image = self.animations[self.status][self.frame_index] #return th image
		#self.image.fill('green')
		self.rect = self.image.get_rect(center = pos) #pass in position

		#float based movement
		self.pos = pygame.math.Vector2(self.rect.center)#using the center for now, important for collisions
		self.direction = pygame.math.Vector2()
		self.speed = 200

		#collisions
		self.collision_sprites = collision_sprites
		self.hitbox = self.rect.inflate(0, -self.rect.height /2)

	def collision(self, direction):
		#option 1
		#pygame.sprite.spritecollide(self, self.collision_sprites, True)
		#option 2
		# for sprite in self.collision_sprites.sprites():
		# 	#check to see if colliding with our rect
		# 	if sprite.rect.colliderect(self.rect):
		# 		print('collision')
		#what we actually wanna do
		if direction == 'horizontal':
			#horizontal collision
			for sprite in self.collision_sprites.sprites():
				if sprite.hitbox.colliderect(self.rect):
					#check to see if it has a name attribute and tht its car
					#want to do this for every time we have an attribute in something
					#makes sure it has the attribute to prevent it from crashing if it doesnt
					if hasattr(sprite, 'name') and sprite.name == 'car':
						#print('car collided')
						pygame.quit()
						sys.exit()
					#know its collided with something on right or left
					#need to figure out if th collision is on th right or left
					if self.direction.x > 0: #moving right
						self.hitbox.right = sprite.hitbox.left #moves it to where the left edge is
						#update th position
						self.pos.x = self.hitbox.centerx # th x chord of th center of our rectangle
					if self.direction.x <0: #moving left
						self.hitbox.left = sprite.hitbox.right
						self.pos.x = self.hitbox.centerx #update again, is the same as above

		else:
			for sprite in self.collision_sprites.sprites():
				if sprite.hitbox.colliderect(self.hitbox):
					if hasattr(sprite, 'name') and sprite.name == 'car':
						pygame.quit()
						sys.exit()
					#know its collided with something on right or left
					#need to figure out if th collision is on th right or left
					if self.direction.y > 0:  # moving down
						self.hitbox.bottom = sprite.hitbox.top  # moves it to where the left edge is
						#update th position
						self.pos.y = self.hitbox.centery # th x chord of th center of our rectangle
					if self.direction.y < 0:  # moving left
						self.hitbox.top = sprite.hitbox.bottom
						self.pos.y = self.hitbox.centery  # update again, is the same as above

	def import_assets(self):
		# path = '../graphics/player/right/' #add the starter path for th animation
		# self.animation = [pygame.image.load(f'{path}{frame}.png').convert_alpha() for frame in range(4)]#could either write a list comprehension or a for loop

		#better import
		self.animations  = {}
		for index, folder in enumerate(walk('graphics/player')):
			#enumerate returns the touple and the index, can store in another variable
			if index == 0:
				for name in folder[1]:
					self.animations[name] = []
					#now getting the folder key
			else:
				#want to turn all items in the folder to create surfaces
				#loads out of order unless u sort it
				for file_name in sorted(folder[2]):
					path = folder[0] + '/' +file_name #turn second slash is th character .replace('\\', '/')
					#print(path)
					surf = pygame.image.load(path).convert_alpha()
					key = folder[0].split("/")[-1] #get the second index off the folder
					#print(key)
					self.animations[key].append(surf)
					#print(self.animations)
			#first touple gives the folders that are within player, 
			#then we get a list for each of the folders. no more folders and then pngs
			#first is the name of the folder, then all th folders in the folder and then all the files

		#import the stuff
		# for frame in range(4):
		# 	#surf = pygame.image.load(f'{path}{frame}.png').convert_alpha()
		# 	self.animation.append(surf)
	
	def move(self, dt):
		#normalize the vector so the length is 1 even when its diagnol
		if self.direction.magnitude() != 0:
			#check th magnitude to find the length of th func then check to see if not 0
			self.direction = self.direction.normalize()#returns new vector
		#seperate into vertical and horizontal 
		#horizontal movement
		self.pos.x += self.direction.x * self.speed * dt #not the whole direction just th x
		#collision
		self.hitbox.centerx = round(self.pos.x)
		#drawing
		#need the same center
		self.rect.centerx = self.hitbox.centerx
		self.collision('horizontal')
		#after this will want to get th horizontal collisions
		#vertical movement
		self.pos.y += self.direction.y * self.speed * dt
		self.hitbox.centery = round(self.pos.y)
		self.rect.centery = self.hitbox.centery
		self.collision('vertical')
		#.y accesses the axis
		
		#does for both, dnt need it anymore
		#self.pos += self.direction * self.speed * dt #but where do we get delta time from if its not in this file
		#self.rect.center = (round(self.pos.x), round(self.pos.y))
		#need position direction and speed

	def input(self):

		keys = pygame.key.get_pressed()
		if keys[pygame.K_d]:
			#print('right')
			#moves right continuously
			self.direction.x = 1 #change direction
			self.status = 'right'
		elif keys[pygame.K_a]:
			self.direction.x = -1
			self.status = 'left'
		else:
			self.direction.x = 0

		if keys[pygame.K_w]:
			self.direction.y = -1
			self.status = 'up'
		elif keys[pygame.K_s]:
			self.direction.y = 1
			self.status = 'down'
		else:
			self.direction.y = 0

		# if keys[pygame.K_a]:
		# 	print('left')
		# if keys[pygame.K_w]:
		# 	print('up')
		# if keys[pygame.K_s]:
		# 	print('down') 

	def animate(self, dt):
		current_animation = self.animations[self.status] 
		if self.direction.magnitude() != 0:
			#know there is some kind of movement
			self.frame_index += 10 *dt #will run out of indexes quickly
			if self.frame_index >= len(current_animation):
				self.frame_index = 0 #first item in th list for th animations
		else:
			self.frame_index = 0

		self.image = current_animation[int(self.frame_index)]

	def update(self, dt):
		self.input() #pass in the delta time
		self.move(dt)
		self.animate(dt)
		

