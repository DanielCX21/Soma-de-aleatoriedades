import pygame
import sys
from pygame.locals import QUIT
import random

pygame.init()

largura = 1500
altura = 750
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Simulação')

icone = pygame.image.load(r"fotos\Jogotipo.png")
pygame.display.set_icon(icone)

quantidade_somada = 10
numeros_experimentados = 100
numero_testes = 1000000
quantidade_retangulos = quantidade_somada * numeros_experimentados
tamanho_retangulo_x = largura / quantidade_retangulos
tamanho_retangulo_y = altura / 10000

clock = pygame.time.Clock()
fps_alvo = 1000

pygame.font.init()
fonte = pygame.font.Font(None, 20)

soma = 0
i = 0

lista = [0] * quantidade_retangulos

pausar_tela = False

while True:
    i += 1
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if i > (numero_testes):
        pausar_tela = True

    if not pausar_tela:
        soma = 0
        pygame.draw.rect(tela, (0,0,0), (0,0,300,22))
        texto = fonte.render(f' Quantidade somada: {i}', True, (0, 255, 0))
        rect = texto.get_rect()
        rect.center = (90, 10)
        tela.blit(texto, rect)
        for j in range (0,quantidade_somada):
            soma += random.randint(0,numeros_experimentados)
        lista[soma-1] += 1
        pygame.draw.rect(tela, (0,255,0), ((soma * tamanho_retangulo_x),altura - (tamanho_retangulo_y * lista[soma-1]),tamanho_retangulo_x ,(tamanho_retangulo_y * lista[soma-1])))

    clock.tick(fps_alvo)
    pygame.display.update()

