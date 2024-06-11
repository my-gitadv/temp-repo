# Drawing Circle Shape:
# Syntax : pygame.draw.circle(surface, color, center, radius, width)

# Parameters :

# 1. surface :- Here we can pass the surface on which we want to draw our circle. In the above example, we created a surface object named ‘window’.
# 2. color :- Here we can pass the color for our circle. We are using green color in our example.
# 3. center :- Here we can pass the ( x, y ) coordinates for the center of the circle.
# 4. radius :- Here we can pass the radius of our circle.
# 5. width :- Here we can pass the line thickness. we can also create a solid circle by changing the value of this width parameter. So let’s look at that.


# Example 2: Drawing a circle.

# Importing pygame module
import pygame
from pygame.locals import *

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))

# Fill the scree with white color
window.fill((255, 255, 255))

# Using draw.rect module of
# pygame to draw the hollow circle
pygame.draw.circle(window, (0, 255, 0), 
				[300, 300], 170, 3)

# pygame to draw the hollow circle
# pygame.draw.circle(window, (0, 255, 0), 
# 				[300, 300], 170, 0)

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