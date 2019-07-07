# coding: utf-8
import pygame
from constantes import *
from Blocos import Bloco
from player import player
from Partida import Partida
from mapas import *

class Breakout():
    """
        Classe principal do jogo.
    """
    def __init__(self):
        self.JANELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption("Atari Breakout")

    def iniciar_jogo(self):
        """
            Inicia partida
        """
        self.run = True
        self.partida_ativa = Partida(1)

    def clean(self, janela): # resets screen
        janela.fill(WHITE)

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
            # Se o usuário deseja fechar o programa
            if event.type == pygame.QUIT:
                self.run = False
                self.menu = False
            
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
                self.clean(self.JANELA)
                self.checar_eventos()
                self.partida_ativa.update(self.JANELA)

if __name__ == "__main__":
    pygame.init() # inicia módulos do pygame
    game = Breakout() # instancia a classe principal do jogo
    game.main()
    pygame.quit() # finaliza módulos pygame
