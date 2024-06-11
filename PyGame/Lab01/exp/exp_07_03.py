# pygame.time.delay
# This function works the same as pygame.time.wait function the difference is that 
# this function will use the processor (rather than sleeping) in order to make the delay more accurate. 
# The sample code can be written the same as pygame.time.wait function by just replacing the name:


# # pygame.time.delay

# importing pygame module
import pygame

# importing sys module
import sys

# initialising pygame
pygame.init()

# creating display
display = pygame.display.set_mode((500, 500))

# Creating the image surface
image = pygame.image.load('logo.png')

# putting our image surface on display surface
display.blit(image,(100,100))

# making the script wait for 5000 seconds
pygame.time.delay(5000)

# creating a running loop
while True:

	# creating a loop to check events that are occurring
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	# updating the display
	pygame.display.flip()
