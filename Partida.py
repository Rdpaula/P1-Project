# coding: utf-8

import pygame
import random
from constantes import *
from mapas import *
from player import player
from Blocos import Bloco
from Bola import Bola

class Partida():
    """
        Classe que gerencia uma partida.
    """
    def __init__(self,mapa):
        # Variável para checar se a partida está ativa ainda
        self.estado = True 
        self.CLOCK = pygame.time.Clock()
        self.BLOCOS_GROUP = pygame.sprite.Group()
        self.JOGADOR_GROUP = pygame.sprite.GroupSingle()
        self.BOLA_GROUP = pygame.sprite.GroupSingle()
        
        # Inicializador do mapa
        if mapa==0:
            mapatemporario = self.gerador()
            for bloco in mapatemporario:
                self.BLOCOS_GROUP.add(bloco)
        else:
            for bloco in MAPAS[mapa]:
                self.BLOCOS_GROUP.add(bloco)
        
        self.jogador = player((DIRETORIO + "images/player.png"), 330, 500, 5)
        self.bola = Bola(LARGURA_TELA/2-TAMANHO_BOLA, ALTURA_TELA/2-TAMANHO_BOLA)
        self.JOGADOR_GROUP.add(self.jogador)
        self.BOLA_GROUP.add(self.bola)
    
    def gerador(self):
        """
            Gerador de mapa semi-randômico
        """
        mapa_gerado = []
        bloco=0
        for i in range(1,4): # Quantidade de linhas
            somalargura=2
            while somalargura < LARGURA_TELA:
                bloco+=1
                aux = random.randint(39,80) # Intervalo de largura dos blocos
                if somalargura + aux + 4 > LARGURA_TELA:
                    break

                if aux%7 == 0:   # Critério de atribuição de poder
                    mapa_gerado.append(Bloco(aux%5,somalargura,(30*i)+(3*(i-1)),aux,30,(aux%3)+1))
                else:
                    mapa_gerado.append(Bloco(aux%5,somalargura,(30*i)+(3*(i-1)),aux,30))
                somalargura += aux + 4

            somalargura += 4
            if LARGURA_TELA-somalargura-4 > 0:
                mapa_gerado.append(Bloco(aux%5,somalargura,(30*i)+(3*(i-1)),LARGURA_TELA-somalargura-4,30))
        
        return mapa_gerado

    def update_graphics(self, janela):
        """
            Método que gerencia os gráficos da partida
        """
        janela.fill(WHITE)
        self.JOGADOR_GROUP.draw(janela)
        self.BOLA_GROUP.draw(janela)
        self.BLOCOS_GROUP.draw(janela)
        pygame.display.update() # atualiza tela

    def block_colision(self, bola, bloco):
        """
            Tratamento de colisão de bola com bloco
        """
        bloco.perder_vida()
        if bloco.vida == -1:
            self.BLOCOS_GROUP.remove(bloco)

        if bola.rect.centerx < bloco.rect.left or bola.rect.centerx > bloco.rect.right:
            self.bola.change_direction_x()
        else:
            self.bola.change_direction_y()
        
    def check_block_colision(self):
        """
            Checa colisão entre bola e blocos
        """
        blocos_atingidos = pygame.sprite.spritecollide(self.bola,self.BLOCOS_GROUP,False)
        for bloco in blocos_atingidos:
            self.block_colision(self.bola, bloco)

    def check_player_colision(self):
        """
            Checa e trata colisão entre player e bola
        """
        colisao = pygame.sprite.spritecollide(self.bola, self.JOGADOR_GROUP, False)
        if len(colisao) > 0:
            if self.bola.rect.centerx < self.jogador.rect.left: # tocou na quina esquerda
                self.bola.change_direction_x()
                self.bola.rect.x -= 8 # margem para não bugar
            elif self.bola.rect.centerx > self.jogador.rect.right: # tocou na quina direita
                self.bola.change_direction_x()
                self.bola.rect.x += 8 # margem para não bugar
            self.bola.change_direction_y()

    def update(self, janela):
        """
            A cada tick da partida atualiza jogador, blocos e gráficos
        """
        self.check_player_colision()
        self.check_block_colision()
        self.JOGADOR_GROUP.update()
        self.BOLA_GROUP.update()
        self.BLOCOS_GROUP.update()
        self.update_graphics(janela)
        self.CLOCK.tick(60)
