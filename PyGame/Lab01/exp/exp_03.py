
# Allowing resizing window in PyGame

# Step-by-step Approach:

# 1. Import pygame.
# 2. Form a screen by using pygame.display.set_mode() method and allow resizing using pygame.RESIZABLE .
# 3. Set the title and add content.
# 4. Run pygame.
# 5. Quit pygame.


# import package pygame 
import pygame 

# Form screen with 400x400 size 
# and with resizable 
screen = pygame.display.set_mode((400, 400), 
								pygame.RESIZABLE) 

# set title 
pygame.display.set_caption('Resizable') 

# run window 
running = True
while running: 
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			running = False

# quit pygame after closing window 
pygame.quit() 
