# coding: utf-8

import pygame
from constantes import *
from player import player

class Partida():
    """
        Classe que gerencia uma partida.
    """
    def __init__(self):
        # Variável para checar se a partida está ativa ainda
        self.estado = True 
        self.CLOCK = pygame.time.Clock()
        self.JOGADOR_GROUP = pygame.sprite.GroupSingle()
        self.BLOCOS_GROUP = pygame.sprite.Group()
        jogador = player((DIRETORIO + "images/player.png"), 330, 500, 5)
        self.JOGADOR_GROUP.add(jogador)

    def update_graphics(self, janela):
        """
            Método que gerencia os gráficos da partida
        """
        janela.fill(WHITE)
        self.JOGADOR_GROUP.draw(janela)
        self.BLOCOS_GROUP.draw(janela)
        pygame.display.update() # atualiza tela
    
    def update(self, janela):
        """
            A cada tick da partida atualiza jogador, blocos e gráficos
        """
        self.JOGADOR_GROUP.update()
        self.BLOCOS_GROUP.update()
        self.update_graphics(janela)
        self.CLOCK.tick(60)
