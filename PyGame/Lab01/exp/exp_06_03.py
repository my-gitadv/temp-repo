# pygame.Surface.set_colorkey: Set the current color key for the surface. 
# When blitting this surface onto a destination, any pixels that have the 
# same color as the colorkey will be transparent.
# Syntax: set_colorkey(Color, flags=0)  

# Importing the library
import pygame

# Initializing Pygame
pygame.init()

# creating the display surface
display_surface = pygame.display.set_mode((500, 500 ))

# Creating the image surface
image = pygame.image.load('logo.png')

# putting our image surface on display surface
# making the white colored part 
# of the surface as transparent
pygame.Surface.set_colorkey (image, [255,255,255])

display_surface.blit(image,(100,100))

# updating the display
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
