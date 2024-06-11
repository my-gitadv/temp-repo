# Recreate the exc_04.py using class (OOP)
import pygame as pg

class Flower:
    def __init__(self,screen,WIDTH,HEIGHT, x, y, clr_pollen, clr_pettal, size):
        self.screen = screen
        self.x_pol = x
        self.y_pol = y
        self.clr_pollen = clr_pollen
        self.clr_pettal = clr_pettal
        self.size = size
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT    
        
        # create 4 positions of each pettals
    def createPosPettals(self):
        x,y = self.x_pol, self.y_pol + 1.5*self.size
        self.createPosSinglePettal(x,y)

        x,y = self.x_pol + 1.5*self.size, self.y_pol
        self.createPosSinglePettal(x,y)

        x,y = self.x_pol, self.y_pol - 1.5*self.size
        self.createPosSinglePettal(x,y)

        x,y = self.x_pol - 1.5*self.size, self.y_pol
        self.createPosSinglePettal(x,y)



        # create 4 positions of corner of a pettal
    def createPosSinglePettal(self,x,y):
        x_01, y_01 = x, y + self.size
        x_02, y_02 = x + self.size, y
        x_03, y_03 = x, y - self.size
        x_04, y_04 = x - self.size, y

        x_01, y_01 = self.rePosition(x_01,y_01)
        x_02, y_02 = self.rePosition(x_02,y_02)
        x_03, y_03 = self.rePosition(x_03,y_03)
        x_04, y_04 = self.rePosition(x_04,y_04)
        pg.draw.polygon(self.screen,self.clr_pettal,[(x_01,y_01),(x_02,y_02),(x_03,y_03),(x_04,y_04)], 4)


        # Turn Math's coordinate to pygame coordinate
    def rePosition(self,xi,yi):
        x = xi + self.WIDTH/2
        y = yi*(-1) + self.HEIGHT/2
        return x,y

    def createPollen(self):
         
        x,y = self.rePosition(self.x_pol,self.y_pol)
        pg.draw.circle(self.screen,self.clr_pollen,(x,y),self.size/4)



    def createFlower(self):
        self.createPollen()
        self.createPosPettals()
        
        

        



WIDTH,HEIGHT = 1000, 800
size = WIDTH,HEIGHT
pg.init()
screen = pg.display.set_mode(size)
screen.fill((0, 0, 0))



flower1 = Flower(screen,WIDTH,HEIGHT,0,0,"green","blue",50)
flower1.createFlower()

flower2 = Flower(screen,WIDTH,HEIGHT,100,100,"lightgreen","lightblue",50)
flower2.createFlower()

pg.display.flip()



# Prepare loop condition
running = False

# Event loop
while not running:

	# Close window event
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = True
