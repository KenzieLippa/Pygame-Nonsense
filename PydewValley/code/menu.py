import pygame
from settings import *
from timer import Timer

class Menu:
	def __init__(self, player, toggle_menu):

		#general setup
		self.player = player
		self.toggle_menu = toggle_menu
		#these are attributes
		self.display_surface = pygame.display.get_surface()
		self.font = pygame.font.Font('../font/LycheeSoda.ttf' , 30) #first is lower second is upper

		#options
		self.width = 400
		self.space = 10
		self.padding = 8

		#create the actual menu entries
		self.options = list(self.player.item_inventory.keys()) + list(self.player.seed_inventory.keys()) #.keys() extracts all th keys from the dictionary and list() turns them into a list
		#print(self.options)
		#check index and see if smaller than th border
		self.sell_border = len(self.player.item_inventory)-1
		self.setup()

		#movement
		self.index = 0 #when creating show entry
		self.timer = Timer(200)

	def setup(self):
		#create text surf
		self.text_surfs = []
		self.total_height = 0
		for item in self.options:
			#the list we created up there
			text_surf = self.font.render(item,False,'Black')
			#once we have out new surface we need to append
			self.text_surfs.append(text_surf)
			self.total_height += text_surf.get_height() + (self.padding * 2)

		self.total_height += (len(self.text_surfs) -1) * self.space
		self.menu_top = SCREEN_HEIGHT /2 - self.total_height /2 #menu in th middle

		self.main_rect = pygame.Rect(SCREEN_WIDTH /2 - self.width/2, self.menu_top,self.width, self.total_height)

		#buy or sell surface
		self.buy_text = self.font.render('Buy',False, 'Black')
		self.sell_text = self.font.render('Sell',False, 'Black')

	def display_money(self):
		text_surf = self.font.render(f'${self.player.money}',False, 'Black') #dnt antialias with pixel fonts
		text_rect = text_surf.get_rect(midbottom = (SCREEN_WIDTH/2, SCREEN_HEIGHT-20))

		pygame.draw.rect(self.display_surface, 'White', text_rect.inflate(10,10), 0, 6) #border radius is the last one which is with rounding
		self.display_surface.blit(text_surf, text_rect)

	def input(self):
		keys = pygame.key.get_pressed()
		self.timer.update()

		if keys[pygame.K_ESCAPE]:
			self.toggle_menu()

		if not self.timer.active:
			if keys[pygame.K_w]:
				self.index -=1
				self.timer.activate()

			if keys[pygame.K_s]:
				self.index +=1
				self.timer.activate()
			if keys[pygame.K_SPACE]:
				self.timer.activate()

				#get item
				current_item = self.options[self.index]
				#print(current_item)

				#sell
				if self.index <= self.sell_border:
					if self.player.item_inventory[current_item] > 0:
						self.player.item_inventory[current_item] -=1
						self.player.money +=SALE_PRICES[current_item]

				#buy
				else:	
					seed_price = PURCHACE_PRICES[current_item]
					#check if player can afford
					if self.player.money >=seed_price:
						self.player.seed_inventory[current_item] +=1
						self.player.money -= seed_price

		if self.index < 0:
			self.index = len(self.options) -1 #goes to the end of th list

		if self.index > len(self.options) -1:
			self.index = 0


	def show_entry(self, text_surf, amount, top, selected):
		#background
		bg_rect = pygame.Rect(self.main_rect.left, top, self.width, text_surf.get_height() + self.padding * 2)
		pygame.draw.rect(self.display_surface, 'White', bg_rect, 0,4)

		#text
		text_rect = text_surf.get_rect(midleft = (self.main_rect.left +20, bg_rect.centery))
		self.display_surface.blit(text_surf, text_rect)

		#amount
		amount_surf = self.font.render(str(amount),False,'Black')
		amount_rect =  amount_surf.get_rect(midright = (self.main_rect.right -20, bg_rect.centery))
		self.display_surface.blit(amount_surf, amount_rect)

		if selected:
			pygame.draw.rect(self.display_surface, 'black', bg_rect, 4,6)
			if self.index <= self.sell_border: #checks the length of th inventory for th buy partition
				pos_rect = self.sell_text.get_rect(midleft = (self.main_rect.left +150,bg_rect.centery))
				#pos_rect = (0,0)
				self.display_surface.blit(self.sell_text, pos_rect)
			else:
				pos_rect = self.buy_text.get_rect(midleft = (self.main_rect.left +150,bg_rect.centery))
				self.display_surface.blit(self.buy_text, pos_rect)

		#go to left of right side
	def update(self):
		self.input()
		self.display_money()
		#pygame.draw.rect(self.display_surface, 'White', self.main_rect)
		#self.display_surface.blit(pygame.Surface((1000,1000)), (0,0)) #place a small rect
		for text_index,text_surf in enumerate(self.text_surfs):
			top = self.main_rect.top +text_index * (text_surf.get_height() + (self.padding * 2)+self.space)
			amount_list = list(self.player.item_inventory.values()) + list(self.player.seed_inventory.values())
			amount = amount_list[text_index]
			#get distance downwards
			self.show_entry(text_surf,amount,top, self.index == text_index)
			#self.display_surface.blit(text_surf, (100,text_index*50))

