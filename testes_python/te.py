import pygame

from pygame.locals import *
from sys import exit
from random import randint


pygame.init()

pygame.mixer_music.set_volume(0.5)
musica_fundo = pygame.mixer.music.load('smw_course_clear.wav')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin.wav')
barulho_colisao.set_volume(0.9)

largura = 640
altura = 480

x = int(largura/2)
y = int(altura/2)

pontos = 0

x_azul = randint(40, 600)
y_azul = randint(50, 450)

fonte = pygame.font.SysFont('lato', 40, bold=True, italic=True)


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

while True:
    relogio.tick(50)
    tela.fill((0, 0, 0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (222, 222, 222))
    for event in pygame.event.get():
        if event.type == QUIT:
           pygame.quit() 
           exit()
        # if event.type == KEYDOWN:
        #     if event.key == K_a:
        #         x = x - 20
        #     if event.key == K_d:
        #         x = x + 20
        #     if event.key == K_w:
        #         y = y - 20
        #     if event.key == K_s:
        #         y = y + 20
        
        if pygame.key.get_pressed()[K_a]:
            x = x - 20
                
        if pygame.key.get_pressed()[K_d]:
            x = x + 20
            
        if pygame.key.get_pressed()[K_w]:
            y = y + 20
                
        if pygame.key.get_pressed()[K_s]:
            y = y - 20
    
    cobra = pygame.draw.rect(tela, (0, 255, 0), (x, y, 40, 50))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_azul, y_azul, 40, 50))
    
    if cobra.colliderect(maca):
        
        x_azul = randint(40, 600)
        y_azul = randint(50, 450)
        pontos = pontos + 1
        barulho_colisao.play()
    
    tela.blit(texto_formatado, (450, 40))



        
 
    
    pygame.display.update()
        

