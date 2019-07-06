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
        
        jogador = player((DIRETORIO + "images/player.png"), 330, 500, 5)
        self.bola = Bola(LARGURA_TELA/2-TAMANHO_BOLA, ALTURA_TELA/2-TAMANHO_BOLA)
        self.JOGADOR_GROUP.add(jogador)
        self.BOLA_GROUP.add(self.bola)
    
    def gerador(self):
        mapa_gerado = []
        bloco=0
        for i in range(1,4): # Quantidade de linhas
            somalargura=2
            while somalargura < LARGURA_TELA:
                bloco+=1
                aux = random.randint(39,80) # Intervalo de largura dos blocos

                if aux%7 == 0:   # Critério de atribuição de poder
                    mapa_gerado.append(Bloco(aux%5,somalargura,(30*i)+(3*(i-1)),aux,30,(aux%3)+1))
                else:
                    mapa_gerado.append(Bloco(aux%5,somalargura,(30*i)+(3*(i-1)),aux,30))
                somalargura += aux + 4

            somalargura = somalargura-aux+4
            if LARGURA_TELA-somalargura-4 > 0:  # Se ainda ficou um pedaço da linha sem bloco
                mapa_gerado.append(Bloco(aux%5,somalargura,(30*i)+3,LARGURA_TELA-somalargura-4,30))
        
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
        
        # Colisão entre bola e bloco
        blocos_atingidos = pygame.sprite.spritecollide(self.bola,self.BLOCOS_GROUP,False)
        for bloco in blocos_atingidos:
            self.bola.change_direction_y() # ***Tratar essa colisão depois***
            bloco.vida -= 1
            if bloco.vida == -1:
                self.BLOCOS_GROUP.remove(bloco)
            blocos_atingidos.remove(bloco)
    
    def update(self, janela):
        """
            A cada tick da partida atualiza jogador, blocos e gráficos
        """
        self.JOGADOR_GROUP.update()
        self.BOLA_GROUP.update()
        self.BLOCOS_GROUP.update()
        self.update_graphics(janela)
        self.CLOCK.tick(60)
