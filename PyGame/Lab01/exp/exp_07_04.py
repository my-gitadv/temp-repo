# pygame.time.Clock
# This function is used to create a clock object which can be used to keep track of time. 
# The various methods of clock object are below:

# tick():This method should be called once per frame. 
# It will compute how many milliseconds have passed since the previous call. 
# If you pass the optional framerate argument the function will delay to keep the game 
# running slower than the given ticks per second. For example if we pass 10 as argument 
# the program will never run at more than 10 frames per second.

# get_time():It is used to obtain a number of milliseconds used between two tick().

# get_fps():it gives information regarding the clock frame rate. it returns the output in floating-point value.



# # pygame.time.Clock

# importing the pygame module
import pygame

# initialising the pygame
pygame.init()

# declaring a variable i with value 0
i=0

# creating a clock object
clock=pygame.time.Clock()

# creating a loop for 5 iterations
while i<5:
	
	# setting fps of program to max 1 per second
	clock.tick(1)
	
	# printing time used in the previous tick
	print(clock.get_time())
	
	# printing compute the clock framerate
	print(clock.get_fps())
	i=i+1