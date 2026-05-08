import pygame, sys

# cores 
WHITE       = (255,255,255)
RED         = (255,0,0)

size        = (800,600)
screen      = pygame.display.set_mode(size)

pygame.mouse.set_visible(0)
game_over = False

clock = pygame.time.Clock()

rect_pos_y = 10
speed_rect = 5

# posição da bolinha
pos_x = 300
pos_y = 400

speed_x = 3
speed_y = 3

background = pygame.image.load("background.png").convert()
gameover = pygame.image.load("gameover.png").convert()

pygame.mixer.init()


while not game_over:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    screen.fill(WHITE)
    screen.blit(background,[0,0])
    
    if rect_pos_y > 490 or rect_pos_y < 0:
        speed_rect *= -1
    
    rect_pos_y += speed_rect
    
    if pos_x > 790 or pos_x < 10:
        speed_x *= -1
        pos_x = 400
        pos_y = 300
        #screen.blit(gameover,[0,0])
        #pygame.display.flip()
        #import time
        #time.sleep(3)
        
    
    if pos_y > 590 or pos_y < 10:
        speed_y *= -1
    
    pos_x += speed_x
    pos_y += speed_y

    mouse = pygame.mouse.get_pos()
    
    # retangulo 1
    jogador1 = pygame.draw.rect(screen, RED, (50,mouse[1],10,100))
    jogador2 = pygame.draw.rect(screen, RED, (770,rect_pos_y,10,250))
    # bolinha
    bolinha = pygame.draw.circle(screen, RED, [pos_x,pos_y], 10)
    
    if bolinha.colliderect(jogador1):
        speed_x *= -1
        speed_y *= -1
    if bolinha.colliderect(jogador2):
        speed_x *= -1
        speed_y *= -1
        #musica = pygame.mixer.music.load("som.mp3")
        #pygame.mixer.music.play(1,0.50)

    #clock.tick(300)
    
    pygame.display.flip()
    
pygame.quit()