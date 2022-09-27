import pygame
from os import walk #walks through folder and gives you the names of folders and names of items inside
class Player(pygame.sprite.Sprite):
	def __init__(self, pos, groups):
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
	def import_assets(self):
		path = '../graphics/player/right/' #add the starter path for th animation
		self.animation = [pygame.image.load(f'{path}{frame}.png').convert_alpha() for frame in range(4)]#could either write a list comprehension or a for loop

		#better import
		self.animations  = {}
		for index, folder in enumerate(walk('../graphics/player')):
			#enumerate returns the touple and the index, can store in another variable
			if index == 0:
				for name in folder[1]:
					self.animations[name] = []
					#now getting the folder key
			else:
				#want to turn all items in the folder to create surfaces
				for file_name in folder[2]:
					path = folder[0] + '/' +file_name #turn second slash is th character .replace('\\', '/')
					print(path)
					surf = pygame.image.load(path).convert_alpha()
					key = folder[0].split("/")[-1] #get the second index off the folder
					print(key)
					self.animations[key].append(surf)
					print(self.animations)
			#first touple gives the folders that are within player, 
			#then we get a list for each of the folders. no more folders and then pngs
			#first is the name of the folder, then all th folders in the folder and then all the files

	#import the stuff
		for frame in range(4):
			#surf = pygame.image.load(f'{path}{frame}.png').convert_alpha()
			self.animation.append(surf)
	def move(self, dt):
		#normalize the vector so the length is 1 even when its diagnol
		if self.direction.magnitude() != 0:
			#check th magnitude to find the length of th func then check to see if not 0
			self.direction = self.direction.normalize()#returns new vector
		self.pos += self.direction * self.speed * dt #but where do we get delta time from if its not in this file
		self.rect.center = (round(self.pos.x), round(self.pos.y))
	#need position direction and speed
	def input(self):

		keys = pygame.key.get_pressed()
		if keys[pygame.K_d]:
			#print('right')
			#moves right continuously
			self.direction.x = 1 #change direction
		elif keys[pygame.K_a]:
			self.direction.x = -1
		else:
			self.direction.x = 0

		if keys[pygame.K_w]:
			self.direction.y = -1
		elif keys[pygame.K_s]:
			self.direction.y = 1
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
		self.frame_index += 10 *dt #will run out of indexes quickly
		if self.frame_index >= len(current_animation):
			self.frame_index = 0
		self.image = current_animation[int(self.frame_index)]
	def update(self, dt):
		self.input() #pass in the delta time
		self.move(dt)
		self.animate(dt)

