import pygame
import os 
from constantes import *
DIRETORIO = os.getcwd()

class player(pygame.sprite.Sprite):
    def __init__(self, sprite, pos_x, pos_y, velocidade=5):# initiating player
        pygame.sprite.Sprite.__init__(self)
        self.__initialposition_position = (pos_x,pos_y)
        self.image = pygame.image.load(DIRETORIO+"/images/player.png")
        self.image = pygame.transform.scale(self.image, (120, 15))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.velocidade = velocidade
        self.vidas = 3
        self.died = False

    def posicao_inicial(self): # definition of initial position
        self.rect.x = self.__initialposition_position[0]
        self.rect.y = self.__initialposition_position[1]

    def die(self):
        # self.som_losslife = pygame.mixer.Sound
        self.posicao_inicial() # Reset position
        self.vidas -= 1 # loss life
        if self.vidas == 0:
            self.died = True
        return self.died

    def move_left(self):
        """
            Checa limites e move jogador para a esquerda
        """
        if self.rect.x - self.velocidade >= 0:
            self.rect.x -= self.velocidade

    def move_right(self):
        """
            Checa limites e move jogador para a direita
        """
        if self.rect.x + self.velocidade <= LARGURA_TELA - self.image.get_width() + 3:
            self.rect.x += self.velocidade

    def update(self, velocidade = 5):# moving the player
        self.velocidade = velocidade 
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.move_left()
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.move_right()
