# Drawing shapes with the mouse:


# Importing pygame module
import pygame
import random
from pygame.locals import *

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))

# Fill the scree with white color
window.fill((255, 255, 255))

# creating list in which we will store
# the position of the circle
circle_positions = []
circle_colors = []
# radius of the circle
circle_radius = 60



# Creating a variable which we will use
# to run the while loop
run = True

# Creating a while loop
while run:

	# Iterating over all the events received from
	# pygame.event.get()
	for event in pygame.event.get():

		# If the type of the event is quit
		# then setting the run variable to false
		if event.type == QUIT:
			run = False

		# if the type of the event is MOUSEBUTTONDOWN
		# then storing the current position
  		# Color of the circle
		elif event.type == MOUSEBUTTONDOWN:
			position = event.pos
			color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))

			circle_positions.append(position)
			circle_colors.append(color)

			
	# Using for loop to iterate
	# over the circle_positions
	# list
	for i in range(len(circle_positions)):

		# Drawing the circle
		pygame.draw.circle(window, circle_colors[i], circle_positions[i],
						circle_radius)	

	# Draws the surface object to the screen.
	pygame.display.update()