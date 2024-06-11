# pygame.time.wait
# This function is used to pause the running of the program for few seconds. 
# it takes time in milliseconds as parameter.

# pygame.time.wait


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
pygame.time.wait(5000)

# creating a running loop
while True:

	# creating a loop to check events that are occurring
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	# updating the display
	pygame.display.flip()
