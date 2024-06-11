# Event Handling


# Using pygame.event.post() method
# We can directly post our events using pygame.event.post() method. 
# This method adds our event to the end of the events on the queue. 
# In order to execute this, we need to convert our event to Pygame’s event type 
# inorder to match the attributes of the post method and avoid errors.

# Syntax:

"""

# Step 1 – Convert event into event datatype of pygame 





ADD_event = pygame.event.Event(event)

# Step 2 – Post the event

pygame.event.post(ADD_event)    # event_name as parameter

"""



# Using pygame.time.set_timer() method
# Broadcasting the event periodically by using PyGame timers. 
# Here, we’ll be using another method to publish the event by using set_timer() function, 
# which takes two parameters, a user event name and time interval in milliseconds.

# Syntax:

"""

# event_name, time in ms
pygame.time.set_timer(event, duration)  

"""

# Python program to add Custom Events 
import pygame 


pygame.init() 

# Setting up the screen and timer 
screen = pygame.display.set_mode((500, 500)) 
timer = pygame.time.Clock() 

# set title 
pygame.display.set_caption('Custom Events') 

# defining colours 
WHITE = (255, 255, 255) 
RED = (255, 0, 0) 
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 

# Keep a track of active variable 
bg_active_color = WHITE 
screen.fill(WHITE) 

# custom user event to change color 
CHANGE_COLOR = pygame.USEREVENT + 1

# custom user event to inflate defalte 
# box 
ON_BOX = pygame.USEREVENT + 2

# creating Rectangle 
box = pygame.Rect((225, 225, 50, 50)) 
grow = True

# posting a event to switch color after 
# every 500ms 
pygame.time.set_timer(CHANGE_COLOR, 2000) 

running = True
while running: 
	
	# checks which all events are posted 
	# and based on that perform required 
	# operations 
	for event in pygame.event.get(): 
		
		# switching colours after every 
		# 500ms 
		if event.type == CHANGE_COLOR: 
			if bg_active_color == GREEN: 
				screen.fill(GREEN) 
				bg_active_color = WHITE 
			elif bg_active_color == WHITE: 
				screen.fill(WHITE) 
				bg_active_color = GREEN 

		if event.type == ON_BOX: 
			
			# to inflate and deflate box 
			if grow: 
				box.inflate_ip(3, 0) 
				grow = box.width < 75
			else: 
				box.inflate_ip(-3, 0) 
				grow = box.width < 50

		if event.type == pygame.QUIT: 
			
			# for quitting the program 
			running = False

	# Posting event when the cursor is on top 
	# of the box 
	if box.collidepoint(pygame.mouse.get_pos()): 
		pygame.event.post(pygame.event.Event(ON_BOX)) 

	# Drawing rectangle on the screen 
	pygame.draw.rect(screen, RED, box) 

	# Updating Screen 
	pygame.display.update() 
	
	# Setting Frames per Second 
	timer.tick(30) 

pygame.quit() 
