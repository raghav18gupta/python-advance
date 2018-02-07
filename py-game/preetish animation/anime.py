import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
catImg = pygame.image.load('cat.png')
cat1Img = pygame.image.load('cat1.png')
cat2Img = pygame.image.load('cat2.png')
cat3Img = pygame.image.load('cat3.png')
catx = 10
caty = 10
direction = 'right'

pygame.mixer.music.load('SmellyCat.mp3')
pygame.mixer.music.play(-1, 0.0)
pygame.time.wait(1000) #background music

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Smelly Cat', True, BLACK)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150) #text


while True: # the main anime loop

    DISPLAYSURF.fill(WHITE) 
    
    if direction == 'right':
        DISPLAYSURF.fill(BLUE)
        catx += 5
        DISPLAYSURF.blit(cat3Img, (catx, caty))
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        DISPLAYSURF.fill(GREEN)
        caty += 5
        DISPLAYSURF.blit(cat2Img, (catx+40, caty))
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        if caty == 180:
            direction = 'left'
    elif direction == 'left':
        DISPLAYSURF.fill(RED)
        catx -= 5
        DISPLAYSURF.blit(catImg, (catx, caty+40))
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        DISPLAYSURF.fill(WHITE)
        caty -= 5
        DISPLAYSURF.blit(cat1Img, (catx, caty))
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        if caty == 10:
            direction = 'right'


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
    
pygame.mixer.music.stop()    