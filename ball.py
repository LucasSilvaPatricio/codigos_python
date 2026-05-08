import pygame
import random

BLACK = (0,0,0)
cores = [(45, 237, 237), (252, 126, 231), (255, 66, 66), (140, 230, 162),(232, 218, 19)]

size = (600,600)

screen = pygame.display.set_mode(size)

bolinhas = []

raio = 20

count = 0

pygame.mouse.set_visible(0)

for x in range(2000):
    x = random.randint(0,600)
    y = random.randint(0,600)
    bolinhas.append([x,y])
    
game_over = False

while not game_over:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
     
    mouse = pygame.mouse.get_pos()
    print(mouse)  
    
    bola = pygame.draw.circle(screen, cores[1], [mouse[0],mouse[1]],30)
        
    for bolinha in bolinhas:
        balls = pygame.draw.circle(screen, cores[random.randint(0,4)], bolinha,5)
        if balls.colliderect(bola):
            bolinha[0] = -50
            bolinha[1] = -50
            count += 1
            if count == 10:
                raio += 1
                count = 0
        
    
    pygame.display.flip()
    
pygame.quit()