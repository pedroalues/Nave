
import random

import pygame


pygame.init()

x = 1280
y = 720

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('Meu jogo em Python')


gb = pygame.image.load('assets/fundo4.jpg').convert_alpha()
gb = pygame.transform.scale(gb, (x, y))

nave = pygame.image.load('assets/enemy_1.png').convert_alpha()
nave = pygame.transform.scale(nave, (50,50))

playerImg = pygame.image.load('assets/player1.png').convert_alpha()
playerImg = pygame.transform.scale(playerImg, (50,50))#conversão do tamanho da nave
playerImg = pygame.transform.rotate(playerImg, -90)

missil = pygame.image.load('assets/missil.png').convert_alpha()
missil = pygame.transform.scale(missil, (25,25))
missil = pygame.transform.rotate(missil, -45)

pos_nave_x = 500
pos_nave_y = 360

pos_player_x = 200
pos_player_y = 300

vel_missil_x = 0
pos_missil_x = 200
pos_missil_y = 300

triggered = False 

rodando = True


#funções
def respawn():
    x = 1350
    y = random.randint(1,640)
    return [x,y]

def respawn_missil():
    triggered = False
    respawn_missil_x = pos_player_x
    respawn_missil_y = pos_player_y
    vel_missil_x = 0
    return [respawn_missil_x, respawn_missil_y, triggered, vel_missil_x]

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    screen.blit(gb, (0,0))

    rel_x = x % gb.get_rect().width
    screen.blit(gb, (rel_x - gb.get_rect().width,0)) #cria background
    if rel_x < 1280:
        screen.blit(gb, (rel_x, 0))

    #teclas

    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_player_y > 1:
        pos_player_y -=1
        if not triggered:
            pos_missil_y -= 1


    if tecla[pygame.K_DOWN] and pos_player_y < 665:
        pos_player_y += 1 

        if not triggered:
            pos_missil_y += 1 


    if tecla [pygame.K_SPACE]:
        triggered = True
        vel_missil_x = 1


    # respawn

    if pos_nave_x == 50:
        pos_nave_x = respawn()[0]
        pos_nave_y = respawn()[1]

    if pos_missil_x == 1300:
        pos_missil_x, pos_missil_y, triggered, vel_missil_x = respawn_missil()
    

    #movimento
    x-=2
    pos_nave_x -=1

    pos_missil_x += vel_missil_x

    pygame.draw.rect(screen, (255, 0, 0), player_rect, 4)
    pygame.draw.rect(screen, (255, 0, 0), missil_rect, 4)
    pygame.draw.rect(screen, (255, 0, 0), enemy_rect, 4)


    #criar imagens
    screen.blit(nave, (pos_nave_y, pos_nave_y))
    screen.blit(missil, (pos_missil_x, pos_missil_y))
    screen.blit(playerImg, (pos_player_x, pos_player_y))


    pygame.display.update()


