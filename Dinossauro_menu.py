import pygame
from pygame.locals import *  
from sys import exit
from random import  randrange
import os

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("UTF Killed me!")

largura = 640
altura = 480

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, "Imagens")
diretorio_sons = os.path.join(diretorio_principal, "sons")
som_jogo = pygame.mixer.Sound(os.path.join(diretorio_sons, "NFS_sound.mp3"))
som_jogo.set_volume(1)

x = 100
y = altura - 63
yc = y+4
yv = 300
yd = y - 74//2
velocidade = 2.5
tamanho = 30
escolha_nivel = False
nivel_escolhido = False
nivel = 0

conter = 0
branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
azul = (0,0,255)
verde = (0,255,0)
azulCeu = (0,191,255)
verdeGrama = (46,139,87)
tela = pygame.display.set_mode((largura, altura))
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, "Sprite.png")).convert_alpha()
sprite_sheet_boss = pygame.image.load(os.path.join(diretorio_imagens, "Logo.png")).convert_alpha()
relogio = pygame.time.Clock()

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, "Imagens")
Nivel1_img = pygame.image.load(os.path.join(diretorio_imagens,"Nivel_1.png")).convert_alpha()
Nivel2_img = pygame.image.load(os.path.join(diretorio_imagens,"Nivel_2.png")).convert_alpha()
Nivel3_img = pygame.image.load(os.path.join(diretorio_imagens,"Nivel_3.png")).convert_alpha()
Nivel4_img = pygame.image.load(os.path.join(diretorio_imagens,"Nivel_4.png")).convert_alpha()
Nivel5_img = pygame.image.load(os.path.join(diretorio_imagens,"Nivel_5.png")).convert_alpha()

def mensagem(texto, fonte, cor, x, y):
    frase = fonte.render(texto, True, cor)
    tela.blit(frase,(x,y))
        
class Nuvem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((0,5 * 74), (83,74))
        self.image = pygame.transform.scale(self.image, (83*1.5,74*1.5))
        self.rect = self.image.get_rect()
        self.rect.y = randrange(50,200,50)
        self.rect.x = randrange(30, 600, 90)

    def update(self):
        self.rect.x -= velocidade  
        if self.rect.topright[0] < 0:
            self.rect.x = largura
            self.rect.y = randrange(50,200,50)
           

class Chao(pygame.sprite.Sprite):
    def __init__(self, posicao):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((0,10 * 74), (83,74))
        self.rect = self.image.get_rect()
        self.rect.y = yc
        self.rect.x = posicao * 74

    def update(self):
          if self.rect.topright[0] < 0:
            self.rect.x = largura
          self.rect.x -= 10

class Botao():
    def __init__(self, x, y, image, scale):
        largura = image.get_width()
        altura = image.get_height()
        self.image = pygame.transform.scale(image, (int(largura * scale), int(altura *scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def desenha(self,surface):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action

class Logo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet_boss
        self.image = pygame.transform.scale(self.image, (200*2,100*2))
        self.rect = self.image.get_rect()
        self.rect.center = (largura//2,altura//2 - 100)

todas_as_sprites = pygame.sprite.Group()
logos = pygame.sprite.Group()
logo = Logo()
logos.add(logo)

for i in range(largura*2//74+1):
    chao = Chao(i)
    todas_as_sprites.add(chao)

for i in range(3):
    nuvem = Nuvem()
    todas_as_sprites.add(nuvem)

Nivel1_botao = Botao(260, 10, Nivel1_img, 4)
Nivel2_botao = Botao(260, 10 + 84, Nivel2_img, 4)
Nivel3_botao = Botao(260, 10 + 2*84, Nivel3_img, 4)
Nivel4_botao = Botao(260, 10 + 3*84, Nivel4_img, 4)
'''Nivel5_botao = Botao(260, 10 + 4*84, Nivel5_img, 4)'''

som_jogo.play()
    
while True: 
     relogio.tick(30)
     tela.fill(azulCeu)
     pygame.draw.rect(tela, verdeGrama, (0,altura-27,largura,32))
     todas_as_sprites.draw(tela)
     todas_as_sprites.update()

     if escolha_nivel == True:
        if Nivel1_botao.desenha(tela):
            nivel = 1
            nivel_escolhido = True
        if Nivel2_botao.desenha(tela):
            nivel = 2
            nivel_escolhido = True
        if Nivel3_botao.desenha(tela):
            nivel = 3
            nivel_escolhido = True
        if Nivel4_botao.desenha(tela):
            nivel = 4
            nivel_escolhido = True
        '''if Nivel5_botao.desenha(tela):
            nivel = 4
            nivel_escolhido = True'''

     else:
         logos.draw(tela)
         if int(conter) %2 == 0:
             tamanho = 30
             xiss = 140
         else:
             tamanho = 31
             xiss = 135
         fonte = pygame.font.SysFont("arialblack", tamanho)
         mensagem("Press ESPACE To Start", fonte, preto, xiss, altura//2 + 60)
         conter += 0.1

     for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                escolha_nivel = True 
        if evento.type == QUIT:
          pygame.quit()
          exit()
              
     if nivel_escolhido == True:
         som_jogo.stop()
         break
         

     else:pass
     pygame.display.flip() 