# Drawing Objects and Shapes in PyGame



# Drawing Rectangle shape: 
# Syntax: pygame.draw.rect(surface, color, rect, width-of-border)


# Example 1: Drawing rectangle using pygame.

# Importing pygame module
import pygame
#from pygame.locals import *

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))

# Fill the screen with white color
window.fill((255, 255, 255))

# Using draw.rect module of
# pygame to draw the outlined rectangle
pygame.draw.rect(window, (0, 0, 255), 
				[100, 100, 400, 100], 2)

# pygame to draw the solid rectangle
# pygame.draw.rect(window, (0, 0, 255), 
# 				[100, 100, 400, 100], 0)

# Draws the surface object to the screen.
pygame.display.update()



# creating a bool value which checks 
# if game is running
running = True

# Game loop
# keep game running till running is true
while running:

	# Check for event if user has pushed 
	# any event in queue
	for event in pygame.event.get():
	
		# if event is of type quit then set
		# running bool to false
		if event.type == pygame.QUIT:
			running = False
			
