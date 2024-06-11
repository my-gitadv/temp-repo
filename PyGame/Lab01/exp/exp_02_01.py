# # How to get the size of PyGame Window?

# Step-by-step Approach:

# 1. Import pygame.
# 2. Initialize pygame.
# 3. Form a screen by using pygame.display.set_mode() method.
# 4. Get size of formed screen by using screen.get_size() method.
# 5. Quit pygame.


# import package pygame
import pygame

# initialize pygame
pygame.init()

# Form screen
screen = pygame.display.set_mode()

# get the default size
x, y = screen.get_size()

# quit pygame
pygame.display.quit()

# view size (width x height)
print(x, y)
