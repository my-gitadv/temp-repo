# How to get keyboard input in PyGame ?


# Detecting if a key is pressed:
# Whenever a key is pressed or released, pygame.event() queue methods pygame.KEYDOWN and pygame.KEYUP events respectively.

# For example, if we want to detect if a key was pressed, we will track if any event of pygame.KEYDOWN occurred or not and, accordingly, 
# we will get to know if any key was pressed or not. The code for detecting if any key was pressed or not can be written as:
# https://www.geeksforgeeks.org/how-to-get-keyboard-input-in-pygame/?ref=lbp


# importing pygame module
import pygame

# importing sys module
import sys

# initialising pygame
pygame.init()

# creating display
display = pygame.display.set_mode((300, 300))

# creating a running loop
while True:
	
	# creating a loop to check events that
	# are occurring
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		
		# checking if keydown event happened or not
		if event.type == pygame.KEYDOWN:
		
			# if keydown event happened
			# than printing a string to output
			print("A key has been pressed")
