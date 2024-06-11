# From exc_03.py draw randomly flower colors in every click

import pygame
import random
from pygame.locals import *

WIDTH,HEIGHT = 1000, 1000
size = WIDTH,HEIGHT

def toHumanPos(x,y):
	x = x - WIDTH/2
	y = (y - HEIGHT/2)*(-1)
	return x,y

def rePosition(xi,yi):
	x = xi + WIDTH/2
	y = yi*(-1) + HEIGHT/2

	return x,y

def cornerPetals(x,y,size):

	x,y = rePosition(x,y)

	x1,y1 = x, y + size
	x2,y2 = x + size, y
	x3,y3 = x, y -size
	x4,y4 = x - size, y

	return x1,y1,x2,y2,x3,y3,x4,y4


def createPetal(x,y,color,size):
	global screen

	x1,y1,x2,y2,x3,y3,x4,y4 = cornerPetals(x,y,size)
	
	pygame.draw.polygon(screen, color, [(x1, y1), (x2, y2),(x3, y3), (x4, y4)],3) 


def posPetal(x,y,size):

	x1, y1 = x, y + (size + size/2)
	x2, y2 = x + (size + size/2), y
	x3, y3 = x, y - (size + size/2)
	x4, y4 = x - (size + size/2), y
	
	return x1,y1,x2,y2,x3,y3,x4,y4

def cornerLeaf(x,y,size):


	x1, y1 = x, y - size*5
	x2, y2 = x+size , y - size*5
	x3, y3 = x + 2*size , y - size * 4
	x4, y4 = x + size, y - size * 4

	x1,y1 = rePosition(x1,y1)
	x2,y2 = rePosition(x2,y2)
	x3,y3 = rePosition(x3,y3)
	x4,y4 = rePosition(x4,y4)

	return x1,y1,x2,y2,x3,y3,x4,y4 

def cornerLeaf2(x,y,size):

	x1, y1 = x, y - size*5
	x2, y2 = x-size , y - size*5
	x3, y3 = x - 2*size , y - size * 4
	x4, y4 = x - size, y - size * 4


	x1,y1 = rePosition(x1,y1)
	x2,y2 = rePosition(x2,y2)
	x3,y3 = rePosition(x3,y3)
	x4,y4 = rePosition(x4,y4)

	return x1,y1,x2,y2,x3,y3,x4,y4 


def createLeaf(x,y,size):
	x1,y1,x2,y2,x3,y3,x4,y4 = cornerLeaf(x,y,size)
	pygame.draw.polygon(screen, "lightgreen", [(x1, y1), (x2, y2),(x3, y3), (x4, y4)],3) 

	x1,y1,x2,y2,x3,y3,x4,y4 = cornerLeaf2(x,y,size)
	pygame.draw.polygon(screen, "lightgreen", [(x1, y1), (x2, y2),(x3, y3), (x4, y4)],3)


def crateFlower(x,y,clr_pollen,clr_petal,size):
	global screen



	x0,y0 = rePosition(x,y)
	x5, y5 = rePosition(x,(y - size*7))

	pygame.draw.line(screen, "lightgreen", [x0, y0], [x5,y5], 5)
	pygame.draw.circle(screen, clr_pollen,[x0, y0], size/4)
	
	x1,y1,x2,y2,x3,y3,x4,y4 = posPetal(x,y,size)
	createPetal(x1,y1,clr_petal,size)
	createPetal(x2,y2,clr_petal,size)
	createPetal(x3,y3,clr_petal,size)
	createPetal(x4,y4,clr_petal,size)

	createLeaf(x,y,size)





pygame.init()


screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))



# x = 0
# y = 150
pollen_color = (255,255,0)
petal_color = "lightblue"
size = 50

# crateFlower(x,y,pollen_color,petal_color,size)

positions = []



# Prepare loop condition
running = False

# Event loop
while not running:

	# Close window event
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = True
		elif event.type == MOUSEBUTTONDOWN:
			x,y = event.pos
			x,y = toHumanPos(x,y)
			petal_color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
			pollen_color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
			crateFlower(x,y,pollen_color,petal_color,size)
			pygame.display.update()