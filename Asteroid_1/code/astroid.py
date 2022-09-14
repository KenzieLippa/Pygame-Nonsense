import pygame, sys
from random import randint, uniform
def laser_update(laser_list, speed = 600):
	for rect in laser_list:
		rect.y -= speed *dt
		if rect.bottom <0:
			laser_list.remove(rect)

def meteor_update(meteor_list, speed = 300):
	for meteor_tuple in meteor_list:
		direction = meteor_tuple[1] #move down 
		meteor_rect = meteor_tuple[0]
		meteor_rect.center += direction * speed * dt 
		#rect.y += speed * dt
		if meteor_rect.top > WINDOW_HEIGHT:
			#contains tuples so need to remove both
			meteor_list.remove(meteor_tuple)
def display_score():
	score_text = f'Score: {pygame.time.get_ticks()//1000}'
	text_surf = font.render(score_text, True, 'White') #antialiasing softens the edges

	text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH/2, WINDOW_HEIGHT-80))
	display_surface.blit(text_surf, text_rect)
	#can move any point u want and they will stay rellitive
	#place the surface, surface and then position
	#display_surface.blit(test_surf, (WINDOW_WIDTH - test_surf.get_width(),200))
	#display_surface.blit(laser_surf, laser_rect)

	#laser_rect.y -= round(200 * dt)#mult by delta time
	pygame.draw.rect(display_surface, 'purple', text_rect.inflate(30,30), width = 8, border_radius = 5)

def laser_timer(can_shoot, duration = 500):
	if not can_shoot:
		#only if not true cause can shoot so who cares
		current_time = pygame.time.get_ticks()
		if current_time - shoot_time > duration:
			can_shoot = True
	return can_shoot

#move rectangle by vecotrs rect.center += direction * speed * dt
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
#laser_rect = laser_surf.get_rect(midbottom = ship_rect.midtop)
laser_list = []

#laser timer
can_shoot = True
shoot_time = None

font = pygame.font.Font('../graphics/subatomic.ttf', 50)#have a ttf for text
meteor_surf = pygame.image.load('../graphics/meteor.png').convert_alpha()
meteor_list = []


meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 500)


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

#import sound
laser_sound = pygame.mixer.Sound('../sounds/laser.ogg')
explosion_sound = pygame.mixer.Sound('../sounds/explosion.wav')
background_music = pygame.mixer.Sound('../sounds/music.wav')
background_music.play(loops = -1) #loop forever
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
		if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
			#print('Shoot Lazer')
			laser_rect = laser_surf.get_rect(midbottom = ship_rect.midtop)
			laser_list.append(laser_rect)

			can_shoot = False

			shoot_time = pygame.time.get_ticks() #only run when its shot
			laser_sound.play()


		if event.type == meteor_timer:

			#random position
			x_pos = randint(-100, WINDOW_WIDTH + 100)
			y_pos = randint(-140, -50)

			#creating a rect 
			meteor_rect = meteor_surf.get_rect(center= (x_pos, y_pos))
			
			#create a random direction
			direction = pygame.math.Vector2(uniform(-0.5, 0.5), 1 )

			meteor_list.append((meteor_rect, direction))

		

			#create a meteor when timer hits 0
			#timer
			#if event.type == pygame.MOUSEMOTION:
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
	dt = clock.tick(120)/1000 #divide by miliseconds, 1000 miliseconds in one second
		#since using rects it will always place integers but with dt we are moving with float numbers
		#pygame is converting the numbers into ints and not rouding so its not moving very fast
		#since rounds down doesnt actually add anything and therefore doesnt move
		#truncates not rounds
		#delta time can get the frame rate and then standardize it per computer
		#in th positive situation u rnt moving cause of th truncation
	#print(clock.get_fps())
	#mouse input
	# print(pygame.mouse.get_pos()) # dont need an event for this
	# print(pygame.mouse.get_pressed()) #see what is pressed
	ship_rect.center = pygame.mouse.get_pos()

	laser_update(laser_list)
	meteor_update(meteor_list)
	can_shoot = laser_timer(can_shoot, 400) # will execute the function and give the value the returned value
	
	#meteor ship collisions 
	for meteor_tuple in meteor_list:
		meteor_rect = meteor_tuple[0]
		if ship_rect.colliderect(meteor_rect): # returns true or false
			pygame.quit()
			sys.exit()

	#laser meteor collissions
	for laser in laser_list:
		for meteor_tuple in meteor_list:
			meteor_rect = meteor_tuple[0]
			if laser.colliderect(meteor_rect):
				#print('collision!')
				meteor_list.remove(meteor_tuple)
				laser_list.remove(laser)
				explosion_sound.play()
	#pygame.time.get_ticks()
	#2. updates
	display_surface.fill((0, 0, 0)) #can find the colors built in if you go through th documentation
	#test_surf.fill((199, 154, 64))
	#draws in order down
	#need to fill whole surface each time or else ull get blurs
	display_surface.blit(background_surf, (0,0))
	# if ship_rect.y > 0:
	# 	ship_rect.top -=4
		#needs to be greater than cause it never actually equals 0
	display_score()
	#if the top of th ship is at th top then stop

	#will eventually learn how to fix the placement of th surface
	
	#create a for loop that draws the laser surface where the rects are
	for laser in laser_list:
		display_surface.blit(laser_surf, laser)
	for meteor_tuple in meteor_list:
		display_surface.blit(meteor_surf, meteor_tuple[0])

	display_surface.blit(ship_surf, ship_rect) # in exact center of screen
	#ship_y_pos -= 4 
	#3. show the frame to the player/update the display surface
	pygame.display.update() #put all stuff on the window
	#after closing pygame we dont technically quit th game so this bottom part still runs

	#display surface is the main canvas, only one and will always be shown
	#surface, an image, unlimmited and surface is only visable if on the display surface
	#can create surfaces in three ways, can import an image(png and jpeg mostly), can also create one in pygame
	#whenever you create text you  create it on a surface