# pygame.time.get_ticks
# This function gives a time which has been running in milliseconds.


# # pygame.time.get_ticks


# importing pygame module
import pygame

# initialising pygame
pygame.init()

# creating a variable 
i=0
while i<5:
	
	# storing the time in ticks variable
	ticks=pygame.time.get_ticks()
	
	# printing the variable ticks
	print(ticks)
	
	# increasing the value of i by 1
	i=i+1
	
	# pausing the script for 1 second
	pygame.time.wait(1000)
