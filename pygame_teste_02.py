import pygame

pygame.init()

size = (640,480)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
loop = False

# carrega imagens do jogo
pista = pygame.image.load("pista.jpg").convert()
x = 0
y = 0

pos_x = 0
pos_y = 0

eixo_x = False
eixo_y = False

speed_x = 5
speed_y = 5

while not loop:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            loop = True
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_a:
                eixo_x = False
            
            if event.key == pygame.K_d:
                eixo_x = True
                
            if event.key == pygame.K_w:
                eixo_y = False
                
            if event.key == pygame.K_s:
                eixo_y = True
               
                
    if not eixo_x:
        pos_x -= speed_x
    else:
        pos_x += speed_x
    
    if not eixo_y:
        pos_y -= speed_y
    else:
        pos_y += speed_y
        
    #screen.blit(pista,[0,10])
 
    caixa = pygame.draw.rect(screen, (255,0,255),(pos_x,100, 50, 50))
    clock.tick(60)
    pygame.display.flip()
pygame.quit()