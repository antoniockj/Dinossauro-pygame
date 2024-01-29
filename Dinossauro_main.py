import pygame
from pygame.locals import *  
from sys import exit
from random import randint, randrange, choice
import os


pygame.init()
pygame.mixer.init()
pygame.display.set_caption("UTF Killed me!")

largura = 640
altura = 480
nivel = 0

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, "Imagens")
diretorio_sons = os.path.join(diretorio_principal, "sons")
som_morte = pygame.mixer.Sound(os.path.join(diretorio_sons, "death_sound.wav"))
som_ponto = pygame.mixer.Sound(os.path.join(diretorio_sons, "score_sound.wav"))
som_morte.set_volume(1)
som_ponto.set_volume(1)

branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
azul = (0,0,255)
verde = (0,255,0)
azulCeu = (0,191,255)
verdeGrama = (46,139,87)
tela = pygame.display.set_mode((largura, altura))
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, "Sprite.png")).convert_alpha()
relogio = pygame.time.Clock()

while True: 
        if nivel ==0:
            import Dinossauro_menu
            nivel = Dinossauro_menu.nivel
        if nivel == 1:
            import Dinossauro_calculo
            if Dinossauro_calculo.proximo_nivel == True:
                nivel = Dinossauro_calculo.nivel
        elif nivel == 2:
            import Dinossauro_comunicacao
            if Dinossauro_comunicacao.proximo_nivel == True:
                nivel = 3
        elif nivel == 3:
            import Dinossauro_Introducao
            if Dinossauro_Introducao.proximo_nivel == True:
                nivel = 4
        elif nivel == 4:
            import Dinossauro_Fisica
            if Dinossauro_Fisica.proximo_nivel == True:
                nivel = 0

