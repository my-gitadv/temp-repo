# Creating a surface
# Creating surfaces in pygame is quite easy. We just have to pass the height and the width with a tuple
#  to pygame.Surface() method. We can use various methods to format our surface as we want. For example,
#  we can use pygame.draw() to draw shapes, we can use surface.fill() method to fill on the surface. 
#  Now, the implementation of these functions. Let’s discuss syntax and parameters.


# Importing the library
import pygame
import time

# Initializing Pygame
pygame.init()

# Creating the surface
sample_surface = pygame.display.set_mode((400,300))

# Choosing yellow color for the rectangle
color = (255,255,0)

# Drawing Rectangle
pygame.draw.rect(sample_surface, color, 
				pygame.Rect(30, 30, 60, 60))




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

	# The pygame.display.flip() method is used 
	# to update content on the display screen
	pygame.display.flip()