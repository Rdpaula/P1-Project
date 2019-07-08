# coding: utf-8

import pygame
import pygame.gfxdraw
from random import choice
from constantes import *

class Bola(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y, velocidade = 5):
        pygame.sprite.Sprite.__init__(self)
        self.__initialposition_position = (pos_x,pos_y)

        self.image = pygame.Surface([TAMANHO_BOLA, TAMANHO_BOLA], pygame.SRCALPHA)
        pygame.gfxdraw.aacircle(self.image, TAMANHO_BOLA/2, TAMANHO_BOLA/2, TAMANHO_BOLA/2-1, BLACK)
        pygame.gfxdraw.filled_circle(self.image, TAMANHO_BOLA/2, TAMANHO_BOLA/2, TAMANHO_BOLA/2-1, BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.velocidade = velocidade
        self.direction_x = choice([-1, 1])
        self.direction_y = -1

    def pos_initial(self):
        self.rect.x = self.__initialposition_position[0]
        self.rect.y = self.__initialposition_position[1]

    def change_direction_x(self):
        """
            Inverte a direção X
        """
        self.direction_x *= -1
    
    def change_direction_y(self):
        """
            Inverte a direção Y
        """
        self.direction_y *= -1

    def move(self):
        """
            Checa limites da tela e move a bola
        """
        self.rect.y += self.direction_y * self.velocidade
        self.rect.x += self.direction_x * self.velocidade
        loss = False
        if self.rect.y >= ALTURA_TELA - self.image.get_height():
            loss = True
            self.pos_initial()
            self.change_direction_y()
        elif self.rect.y <= 0:
            self.rect.y = 0
            self.change_direction_y()
        if self.rect.x <= 0:
            self.rect.x = 0
            self.change_direction_x()
        elif self.rect.x >= LARGURA_TELA - self.image.get_width():
            self.rect.x = LARGURA_TELA - self.image.get_width()
            self.change_direction_x()
        return loss
    def update(self, velocidade = 3):
        loss = False
        self.velocidade = velocidade
        loss = self.move()
        return loss