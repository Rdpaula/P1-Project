# coding: utf-8
import pygame
from player import *
from constantes import *
import os
DIRETORIO = os.getcwd()

class Partida():
    """
        Classe que gerencia uma partida.
    """
    def __init__(self):
        # Variável para checar se a partida está ativa ainda
        self.estado = True 
        self.CLOCK = pygame.time.Clock()
        self.CLOCK.tick(60)

    def update_graphics(self, janela, evento):
        janela.fill(WHITE)
        player.jogador.update(evento)
    
    def update(self, janela, evento):
        """
            Atualiza cada tick da partida
        """
        self.update_graphics(janela, evento)
        pygame.display.update() # atualiza tela

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
        player.jogador = player((DIRETORIO + "images/player.png"),330,500)        
        self.run = True
        self.partida_ativa = Partida()

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
            # Se o usuário clicou no X da janela
            if event.type == pygame.QUIT:
                self.run = False
                self.menu = False
            self.partida_ativa.update(self.JANELA,event)
            
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
                self.checar_eventos()
                self.clean(self.JANELA)
                player.jogador.update2()

if __name__ == "__main__":
    pygame.init() # inicia módulos do pygame
    game = Breakout() # instancia a classe principal do jogo
    game.main()
    pygame.quit() # finaliza módulos pygame
