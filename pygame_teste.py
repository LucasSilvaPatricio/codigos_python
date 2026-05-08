import pygame, sys, time
from pygame.locals import *
import random

pygame.init()
screen = pygame.display.set_mode((800,600))

clock = pygame.time.Clock()

WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
#x = 0
#speed = 3

coord = []

for i in range(0,100):
    x = random.randint(0,800)
    y = random.randint(0,600)
    coord.append([x,y])
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    screen.fill(WHITE)
        
    #for x in range(100,800, 10):
    #    pygame.draw.line(screen,(255,0,0),[10,x],[600,x],1)
    #    clock.tick(20)
    
    #if x > 740 or x < 0:
        #speed *= -1
    #print(speed)
    
    #x += speed
   
    mouse = pygame.mouse.get_pos()
    
    
    for _coord in coord:
        _coord[1] += 3
        _coord[0] += 3
        pygame.draw.rect(screen,BLUE , (_coord[0],_coord[1], 5,5))
        
        pygame.draw.line(screen,RED,[mouse[0],0],[mouse[0],600],1)
        pygame.draw.line(screen,RED,[0,mouse[1]],[800,mouse[1]],1)
        
        if _coord[1] > 600:
            _coord[1] = 0

        if _coord[0] > 800:
            _coord[0] = 0
                
    pygame.display.flip()
        
        