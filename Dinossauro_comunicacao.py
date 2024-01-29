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

x = 100
y = altura - 63
yc = y+4
yv = 300
yd = y - 74//2
altura_pulo = 200
velocidade = 10
velocidadeS = 20
pontos = 0
vidas = 7

quant_palavras = 10
md = randrange(0,quant_palavras)
palavras = ["batata", "corrida", "pinhata", "coracao", "homem" , "paralelepipedo", "rapido", "museu", "engenharia", "lugar"]
z = palavras[md]
n = len(z)

m = "-" * n
M = []
L = ''
font = pygame.font.SysFont(None, 30)
text = ""
vida = "<3<3<3<3<3<3<3"

for i in range(n):
  M.append(m[i])

input_active = True
ganhou = False
colidiu = False
proximo_nivel = False
fim = False
escolha = choice([0,1,2])
indice = choice([0,1])

tela = pygame.display.set_mode((largura, altura))
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, "Sprite.png")).convert_alpha()
sprite_sheet_boss = pygame.image.load(os.path.join(diretorio_imagens, "Boss.png")).convert_alpha()
relogio = pygame.time.Clock()

def exibe_mensagem(msg, tamanho, cor):
   fonte = pygame.font.SysFont("comicsansms", tamanho, True, False)
   mensagem = "{}".format(msg)
   texto_formatado = fonte.render(mensagem, True, cor)
   return texto_formatado

def  reiniciarJogo():
    global pontos, velocidade, colidiu, escolha, ganhou, md, z, vida, vidas, m, M, L
    md = randrange(0,quant_palavras)
    z = palavras[md]
    vida = "<3<3<3<3<3<3<3"
    m = "-" * n
    M = []
    L = ""
    vidas = 7
    pontos = 0
    velocidade = 10
    colidiu = False
    ganhou = False
    escolha = choice([0,1,2])
    indice = choice([0,1])
    personagem.rect.y = yd
    personagem.pular = False
    livro.rect.x = largura
    pi.rect.x = largura
    integral.rect.x = largura
    e.rect.x = largura
    livrogg.rect.x = largura
    livro.escolha = escolha
    pi.escolha = escolha
    e.escolha = escolha
    integral.escolha = escolha
    livrogg.escolha = escolha
    livro.indice = indice
    pi.indice = indice
    e.indice = indice
    integral.indice = indice
    livrogg.indice = indice

class Samuel(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.som_pulo = pygame.mixer.Sound(os.path.join(diretorio_sons, "jump_sound.wav"))
        self.som_pulo.set_volume(1)
        self.imagens_samuel = [] 
        for i in range(4):
            img = sprite_sheet.subsurface((0,i * 74), (83,74))
            self.imagens_samuel.append(img)
        self.index_lista = 0
        self.image = self.imagens_samuel[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.y = yd
        self.rect.center = (x,y)
        self.pular = False

    def pulo(self):
        self.pular = True
        self.som_pulo.play()
    
    def update(self):
        if self.pular == True:
            self.rect.y -=velocidadeS
            if self.rect.y < yd - altura_pulo:
                self.pular = False
        else: 
            if self.rect.y != yd:
                self.rect.y +=velocidadeS

        if self.index_lista > 3:
            self.index_lista = 0
        self.index_lista +=0.35
        self.image = self.imagens_samuel[int(self.index_lista)]
        
class Nuvem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((0,5 * 74), (83,74))
        self.image = pygame.transform.scale(self.image, (83*1.5,74*1.5))
        self.rect = self.image.get_rect()
        self.rect.y = randrange(50,200,50)
        self.rect.x = randrange(30, 600, 90)

    def update(self):
          if self.rect.topright[0] < 0:
            self.rect.x = largura
            self.rect.y = randrange(50,200,50)
          self.rect.x -= velocidade 

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

class livros(pygame.sprite.Sprite):
    def __init__(self):
         pygame.sprite.Sprite.__init__(self)
         self.image = sprite_sheet.subsurface((0,4 * 74), (83,74))
         self.rect = self.image.get_rect()
         self.mask = pygame.mask.from_surface(self.image)
         self.escolha = escolha
         self.indice = indice
         self.rect.center = (largura,y)
         self.rect.x = largura
    
    def update(self):
        if self.indice == 0:
            if self.escolha == 0 or self.escolha == 1:
                 if self.rect.topright[0] < 0:
                    self.rect.x = largura
                 self.rect.x -= velocidade 

class Pi(pygame.sprite.Sprite):
    def __init__(self):
         pygame.sprite.Sprite.__init__(self)
         self.image = sprite_sheet.subsurface((0,7 * 74), (83,74))
         self.rect = self.image.get_rect()
         self.mask = pygame.mask.from_surface(self.image)
         self.escolha = escolha
         self.indice = indice
         self.rect.center = (largura,yv)
         self.rect.x = largura
    
    def update(self):
        if self.indice == 1: 
            if self.escolha == 0:
                 if self.rect.topright[0] < 0:
                    self.rect.x = largura
                 self.rect.x -= velocidade 

class E(pygame.sprite.Sprite):
    def __init__(self):
         pygame.sprite.Sprite.__init__(self)
         self.image = sprite_sheet.subsurface((0,6 * 74), (83,74))
         self.rect = self.image.get_rect()
         self.mask = pygame.mask.from_surface(self.image)
         self.escolha = escolha
         self.indice = indice
         self.rect.center = (largura,yv)
         self.rect.x = largura
    
    def update(self):
        if self.indice == 1: 
            if self.escolha == 1:
                 if self.rect.topright[0] < 0:
                    self.rect.x = largura
                 self.rect.x -= velocidade 

class Integral(pygame.sprite.Sprite):
    def __init__(self):
         pygame.sprite.Sprite.__init__(self)
         self.image = sprite_sheet.subsurface((0,8 * 74), (83,74))
         self.rect = self.image.get_rect()
         self.mask = pygame.mask.from_surface(self.image)
         self.escolha = escolha
         self.indice = indice
         self.rect.center = (largura,yv)
         self.rect.x = largura
    
    def update(self):
        if self.indice == 1: 
            if self.escolha == 2:
                 if self.rect.topright[0] < 0:
                    self.rect.x = largura
                 self.rect.x -= velocidade 

class livroGG(pygame.sprite.Sprite):
    def __init__(self):
         pygame.sprite.Sprite.__init__(self)
         self.image = sprite_sheet.subsurface((0,12 * 74), (83,74))
         self.rect = self.image.get_rect()
         self.mask = pygame.mask.from_surface(self.image)
         self.escolha = escolha
         self.indice = indice
         self.rect.center = (largura,y)
         self.rect.x = largura
    
    def update(self):
        if self.indice == 0:
            if self.escolha == 2:
                 if self.rect.topright[0] < 0:
                    self.rect.x = largura
                 self.rect.x -= velocidade 

class Professor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet_boss.subsurface((0,1 * 83), (73,83))
        self.image = pygame.transform.scale(self.image, (73*1.5,83*1.5))
        self.rect = self.image.get_rect()
        self.rect.center = (x + 450,y - 5)

todas_as_sprites = pygame.sprite.Group()

for i in range(largura*2//74+1):
    chao = Chao(i)
    todas_as_sprites.add(chao)

for i in range(3):
    nuvem = Nuvem()
    todas_as_sprites.add(nuvem)

personagem = Samuel()
livro = livros()
pi = Pi()
e = E()
integral = Integral()
livrogg = livroGG()
todas_as_sprites.add(personagem,livro, pi, e, integral, livrogg)

professor = Professor()
sprite_profs = pygame.sprite.Group()
sprite_profs.add(professor)

obstaculos = pygame.sprite.Group()
obstaculos.add(livro, pi, e, integral, livrogg)

while True:
    relogio.tick(30)
    tela.fill(azulCeu)
    pygame.draw.rect(tela, verdeGrama, (0,altura-27,largura,32))

    for evento in pygame.event.get():
       if evento.type == KEYDOWN:
          if evento.key == K_SPACE:
            if personagem.rect.y != yd:
                pass
            else:
                personagem.pulo()  
          if evento.key == K_r and (colidiu == True):  
              reiniciarJogo()
          if fim == True and evento.key == K_RETURN:
              proximo_nivel = True
               
       if ganhou == True:
           if evento.type == pygame.MOUSEBUTTONDOWN:
                text = ""
           elif evento.type == pygame.KEYDOWN and input_active:
                if evento.key == pygame.K_RETURN:
                    input_active = False
                elif evento.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += evento.unicode   

       if evento.type == QUIT:
          pygame.quit()
          exit()

    colisoes = pygame.sprite.spritecollide(personagem, obstaculos, False, pygame.sprite.collide_mask)
    
    todas_as_sprites.draw(tela)

    if pontos < 1000:
        if livro.rect.topright[0] <= 0 or pi.rect.topright[0] <= 0 or integral.rect.topright[0] <= 0 or e.rect.topright[0] <= 0 or livrogg.rect.topright[0] <= 0:
            escolha = choice([0,1,2])
            indice = choice([0,1])
            livro.rect.x = largura
            pi.rect.x = largura
            integral.rect.x = largura
            e.rect.x = largura
            livrogg.rect.x = largura
            livro.escolha = escolha
            pi.escolha = escolha
            e.escolha = escolha
            integral.escolha = escolha
            livrogg.escolha = escolha
            livro.indice = indice
            pi.indice = indice
            e.indice = indice
            integral.indice = indice
            livrogg.indice = indice
    else:
        if livro.rect.topright[0] <= 0 or pi.rect.topright[0] <= 0 or integral.rect.topright[0] <= 0 or e.rect.topright[0] <= 0 or livrogg.rect.topright[0] <= 0:
            indice = 2
            livro.indice = indice
            pi.indice = indice
            e.indice = indice
            integral.indice = indice
            livrogg.indice = indice

    if pontos > 1100:
        ganhou = True
      
    if colisoes and colidiu == False:
        som_morte.play()
        colidiu = True
   
    if colidiu == True:
        if pontos%100 == 0:
            pontos+=1
        gameOver = exibe_mensagem("GAME OVER", 40, preto)
        tela.blit(gameOver, (largura//2, altura//2))        
        mr = exibe_mensagem("Pressione r para reiniciar", 20, preto)
        tela.blit(mr, (largura//2, altura//2 + 60))

    elif colidiu == False and ganhou == False:
        pontos +=1
        p = "{}m".format(pontos)
        todas_as_sprites.update()
        texto_pontos = exibe_mensagem(p, 40, preto)

    if pontos%100 == 0:
        som_ponto.play()
        if velocidade >= 23:
            velocidade += 0
        else:
            velocidade += 1       

    if input_active == False:
        input_active = True
        acertou = 0
        for i in range(n):
            if z[i] == text:
              M[i] = z[i]
              m = ""
              for j in range(n):
                m = m + M[j] 
              acertou += 1
        if acertou == 0:
           vidas -= 1
           L = L + text + "-"
           vida = vida[:-2]
        text = ""   

    if vidas == 0:
        colidiu = True
        ganhou = False

    if m == z:
         ganhou = False
         fim = True
         mensagem = exibe_mensagem("Parabens!!", 40, preto)
         tela.blit(mensagem, (largura//2, altura//2))
         mr = exibe_mensagem("Voce ganhou = )", 20, preto)
         tela.blit(mr, (largura//2, altura//2 + 60))
    
    if ganhou == True:
        sprite_profs.draw(tela)
        fala = exibe_mensagem("Vamos ver se voce e bom de portugues", 15, preto)
        tela.blit(fala, (x + 240, y - 80))
        vidas_aparece = exibe_mensagem(vida, 15, preto)
        tela.blit(vidas_aparece, (largura//2, altura//2 - 40))
        ja_foi = exibe_mensagem(L, 15, preto)
        tela.blit(ja_foi, (largura//2 + 130, altura//2 - 40))
        palavra_secreta = exibe_mensagem(m, 20, preto)
        tela.blit(palavra_secreta, (largura//2, altura//2))
        text_surf = font.render(text, True, (preto))
        tela.blit(text_surf, (largura//2, altura//2 + 40))

    if proximo_nivel == True:
        break
    else:
        pass   

    tela.blit(texto_pontos, (500,30))
    nivel_aparece = exibe_mensagem("NIVEL 2", 30, preto)  
    tela.blit(nivel_aparece, (50,30))
    pygame.display.flip() 
    
