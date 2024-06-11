# pygame.Surface.set_alpha: The alpha value set for the full surface image.
# Pass 0 for invisible and 255 for fully opaque.
# Syntax: set_alpha(value, flags=0) or set_alpha(None)

# Importing the library
import pygame

# Initializing Pygame
pygame.init()

# creating the display surface
display_surface = pygame.display.set_mode((500, 500 ))

# Creating the image surface
image = pygame.image.load('D:\Tom_inofficial_dev\PyGame\Lab01\logo.png')

# putting our image surface on display surface
# making the alpha value of surface as 100
pygame.Surface.set_alpha(image, 100)

display_surface.blit(image,(100,100))

# printing the alpha value of the surface
print(pygame.Surface.get_alpha(image))



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

	# updating the display
	pygame.display.flip()