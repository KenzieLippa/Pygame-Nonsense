import pygame, sys


pygame.init() #dont have to worry about what this inits
#delta time measures how long to create one frame, need speed regardless of framerate
#div by the current frame
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))#opens window for a milisecond
pygame.display.set_caption('Asteroid Killer')
clock = pygame.time.Clock() #can limmit th max fram rate
#rectangles are used to store the location info
#importing images
ship_surf = pygame.image.load('../graphics/ship.png').convert_alpha() #convert to something pygame can work with easily
#can put this in a variable
ship_reversed_surf = pygame.transform.flip(ship_surf, False, True) #ships surface and then flipped on the y axis
#can scale it
ship_surf_scaled = pygame.transform.scale(ship_surf, (600, 50))
ship_surf_rotated = pygame.transform.rotate(ship_surf, 45)
#ship_y_pos = 500
#place by center
#create th rect based on th ship size, only used for specific positioning
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))#can specify where your putting it, location is based off of input
print(ship_rect) #stores location 
background_surf = pygame.image.load('../graphics/background.png').convert()
	#gets rid of of transparency without alpha#.. goes up a folder level from current
#add a font object
laser_surf = pygame.image.load('../graphics/laser.png').convert_alpha()
laser_rect = laser_surf.get_rect(midbottom = ship_rect.midtop)
font = pygame.font.Font('../graphics/subatomic.ttf', 50)#have a ttf for text
text_surf = font.render('Space', True, 'White') #antialiasing softens the edges

text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH/2, WINDOW_HEIGHT-80))
#code ends so the display does too
#keeps the code going
#excersize: research, the documentation for pygame is really good
#create a surface
#pygame has built in colors but u can also use a rgb tuple
#test_surf = pygame.Surface((400,100))#needs width and height
#need to attach the surface to the display surface or it wont be shown
#both the display surface and the surface are black
#uses the blit method
#position always th top left of th surface
#speed to run while loop dictates how fast th game runs
test_rect = pygame.Rect(100,200,400,500)
while True:
	#runs forever -> keeps game running
	#do not run the code until i tell you, its game loop

	#most logic will run in here
	#check input then update then place graphics
	#impliment 3 things
	#1. input -> events(mouseclick, mousemovement, pressbutton, controller or touch screen)
	#get all events with
	for event in pygame.event.get():
		if event.type == pygame.QUIT: #if the x button is pressed
			pygame.quit()#quits the game
			sys.exit() #ends any kind of code currently running, everything else will quit
		'''can check the documentation to see what built in python apps are available'''
	# 	if event.type == pygame.MOUSEMOTION:
	# 		#each event has different attributes
	# 		#print(event.pos) #which button are u pressing, rel is relative speed, and then pos is position
	# 		# ship_rect.x = event.pos[0] - ship_rect.width/2
	# 		# ship_rect.y = event.pos[1] - ship_rect.height/2
	# 		#my attempt
	# 		ship_rect.center = event.pos #take the center and make it th event position
	# 	if event.type == pygame.MOUSEBUTTONDOWN:
	# 		#releasing mouse button
	# 		print(event.pos) #print where ur pressing th mouse down
	# #framerate limit
	clock.tick(120)	#delta time can get the frame rate and then standardize it per computer
	print(clock.get_fps())
	#mouse input
	# print(pygame.mouse.get_pos()) # dont need an event for this
	# print(pygame.mouse.get_pressed()) #see what is pressed
	ship_rect.center = pygame.mouse.get_pos()

	#2. updates
	display_surface.fill((0, 0, 0)) #can find the colors built in if you go through th documentation
	#test_surf.fill((199, 154, 64))
	#draws in order down
	#need to fill whole surface each time or else ull get blurs
	display_surface.blit(background_surf, (0,0))
	# if ship_rect.y > 0:
	# 	ship_rect.top -=4
		#needs to be greater than cause it never actually equals 0

	#if the top of th ship is at th top then stop

	#will eventually learn how to fix the placement of th surface
	display_surface.blit(text_surf, text_rect)
	#can move any point u want and they will stay rellitive
	#place the surface, surface and then position
	#display_surface.blit(test_surf, (WINDOW_WIDTH - test_surf.get_width(),200))
	display_surface.blit(laser_surf, laser_rect)

	laser_rect.y -= 10 #mult by delta time
	pygame.draw.rect(display_surface, 'purple', text_rect.inflate(30,30), width = 8, border_radius = 5)

	display_surface.blit(ship_surf, ship_rect) # in exact center of screen
	#ship_y_pos -= 4 
	#3. show the frame to the player/update the display surface
	pygame.display.update() #put all stuff on the window
	#after closing pygame we dont technically quit th game so this bottom part still runs

	#display surface is the main canvas, only one and will always be shown
	#surface, an image, unlimmited and surface is only visable if on the display surface
	#can create surfaces in three ways, can import an image(png and jpeg mostly), can also create one in pygame
	#whenever you create text you  create it on a surface