# draw a rectangle with rounded corner

# Functions Used:

# pygame.display.set_mode(): This function is used to initialize a surface for display. This function takes the size of the display as a parameter.
# pygame.display.flip(): This function is used to update the content of the entire display surface of the screen.
# pygame.draw.rect(): This function is used to draw a rectangle. It takes surface, color, and pygame Rect objects as input parameters and draws a rectangle on the surface.

# This example draws a rectangle with all corner rounded

# Importing the library
import pygame

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400, 300))

# Initializing Color
color = (48, 141, 70)

# Drawing Rectangle
pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60), 2, 3)
pygame.display.flip()


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