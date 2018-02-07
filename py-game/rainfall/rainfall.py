import pygame,random
from pygame.locals import *
from random import *
pygame.init()

black = 0,0,0
size  = width, height = 1100, 665
gameDisplay = pygame.display.set_mode(size)
clock = pygame.time.Clock()
dropimg = pygame.image.load("drop.png")

def transform(oldvalue,oldmin,oldmax,newmin,newmax):
    return (((oldvalue-oldmin)*(newmax-newmin))/(oldmax-oldmin))+newmin

x,y,res,speed,transimg=[],[],[],[],[]
for i in range(0,600):
    x.append(randrange(0,size[0]))
    y.append(randrange(-665,0))
    res.append(randrange(10,randrange(15,30)))
    speed.append(transform(res[i],10,30,10,20))
    transimg.append(pygame.transform.scale(dropimg,(res[i],res[i])))

while True:
    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                quit()
    gameDisplay.fill(black)
    for i in range(0,600):
        gameDisplay.blit(transimg[i],(x[i],y[i]))
        if y[i] > 665:
            x[i] = randrange(0,size[0])
            y[i] = randrange(-665,0)
        else:
            y[i]+=speed[i]
    pygame.display.update()
    clock.tick(30)
