import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
pygame.display.set_caption("jogo da cobrinha")

largura = 640
altura = 480
x = largura/2
y = altura/2
xm = randint(40,600)
ym = randint(50,430)
xc = 10
yc = 0

velocidade = 10
pontos = 0
caule = []  
tamanho_pinton = 0
morreu = False

verde = (0,255,0)
azul = (0,0,255)
vermelho = (255,0,0)
preto = (0,0,0)
branco = (255,255,255)

tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont("arial", 40, True, False)

def aumenta_pinton(caule):
    for quadrado in caule:
        pygame.draw.rect(tela, verde, (quadrado[0],quadrado[1],20,20))
    
def restart():
    global morreu,pontos, caule, tamanho_pinton, x, y, xm, ym
    morreu = False
    pontos = 0
    caule = []  
    tamanho_pinton = 0
    x = largura/2
    y = altura/2
    xm = randint(40,600)
    ym = randint(50,430)

    
while True:  
  
  if len(caule) > tamanho_pinton:
        del caule[0]
        
  if pontos%2 == 0:
        analise = "Sim"
  else:
    analise = "Nao"
    
  tela.fill(branco)
  relogio.tick(30)
  mensagem = "Pontos: {}".format(pontos)
  aparece_mensagem = fonte.render(mensagem, True, preto)  
    
  '''if pygame.key.get_pressed()[K_d]:
        x+=velocidade 
  if pygame.key.get_pressed()[K_a]:
        x-=velocidade 
  if pygame.key.get_pressed()[K_w]:
        y-=velocidade 
  if pygame.key.get_pressed()[K_s]:
        y+=velocidade '''  
          
  x = x + xc
  y = y + yc
    
  if x > largura:
        x = 0
  elif x < 0:
        x = largura

  if y > altura:
        y = 0
  elif y < 0:
        y = altura
  

  pinton = pygame.draw.rect(tela, verde, (x,y,20,20)) 
  maca = pygame.draw.rect(tela, vermelho, (xm,ym,10,10))    

  cabeca = []
  cabeca.append(x)
  cabeca.append(y)
  caule.append(cabeca) 
  aumenta_pinton(caule)
  
  if caule.count(cabeca) > 1:
        morreu = True
        while morreu:
            tela.fill(branco)
            fonte2 = pygame.font.SysFont("arial", 20, False, False)
            mensagem = "Game over, sua pontuacao foi: {} pontos!! Precione R para recomecar".format(pontos)
            aparece_mensagem = fonte2.render(mensagem, True, preto)
            tela.blit(aparece_mensagem, (100,150))
            pygame.display.update()
            
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    exit()
                if evento.type == KEYDOWN:
                    if evento.key == K_r:
                        restart()    

  if   pinton.colliderect(maca):
        xm = randint(40,600)
        ym = randint(50,430)
        pontos+=1
        tamanho_pinton+=1

  for evento in pygame.event.get():
    if evento.type == QUIT:
      pygame.quit()
      exit()
    if evento.type == KEYDOWN:
        if evento.key == K_a:
            if xc == velocidade:
                pass
            else:
                xc = -velocidade
                yc = 0
        if evento.key == K_d:
            if xc == -velocidade:
                pass
            else:
                xc = +velocidade
                yc = 0
        if evento.key == K_w:
            if yc == velocidade:
                pass
            else:
                xc = 0
                yc = -velocidade
        if evento.key == K_s:
            if yc == -velocidade:
                pass
            else:            
                xc = 0
                yc = +velocidade     

  tela.blit(aparece_mensagem, (400,40))
  pygame.display.update() 
