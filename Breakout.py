# coding: utf-8

import pygame
from constantes import *

class Partida():
    """
        Classe que gerencia uma partida.
    """

    def __init__(self):
        # Variável para checar se a partida está ativa ainda
        self.estado = True 

    def update_graphics(self, janela):
        janela.fill(WHITE)

    def update(self, janela):
        """
            Atualiza cada tick da partida
        """
        self.update_graphics(janela)
        pygame.display.update() # atualiza tela

class Breakout():
    """
        Classe principal do jogo.
    """

    def __init__(self):
        self.JANELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        self.CLOCK = pygame.time.Clock()
        pygame.display.set_caption("Atari Breakout")

    def iniciar_jogo(self):
        """
            Inicia partida
        """
        self.run = True
        self.partida_ativa = Partida()

    def finalizar_jogo(self):
        """
            Finaliza Partida
        """
        self.run = False
        self.partida_ativa = None

    def checar_eventos(self):
        """
            Trata eventos de entrada e do estado da partida
        """
        if(not self.partida_ativa.estado):
            self.finalizar_jogo()


        for event in pygame.event.get():
            # Se o usuário clicou no X da janela
            if event.type == pygame.QUIT:
                self.run = False
                self.menu = False

            # Tecla pressionada
            if event.type == pygame.KEYDOWN:
                pass

    def main(self):
        """
            Loop principal do jogo
        """

        # Variáveis de loop para manter o jogo rodando
        self.menu = True

        while self.menu:
            # TODO MENU

            self.iniciar_jogo()

            while self.run:
                self.partida_ativa.update(self.JANELA)
                self.checar_eventos()

if __name__ == "__main__":
    pygame.init() # inicia módulos do pygame

    game = Breakout() # instancia a classe principal do jogo
    game.main()

    pygame.quit() # finaliza módulos pygame
