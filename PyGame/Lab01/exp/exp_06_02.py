# Loading image on the surface
# Syntax: pygame.image.load(img) 




# Importing the library
import pygame


# Initializing Pygame
pygame.init()

# creating the display surface
display_surface = pygame.display.set_mode((500, 500 ))

# Creating the image surface
image = pygame.image.load('icon.png')

# putting our image surface on display 
# surface
#(0,0) means top left corner
display_surface.blit(image,(0,0))

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
