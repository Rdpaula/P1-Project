import pygame
import pygame.gfxdraw
from random import choice
from constantes import *

class Bola(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y, velocidade = 3):
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

    def change_direction_x(self):
        self.direction_x *= -1
    
    def change_direction_y(self):
        self.direction_y *= -1

    def move(self):
        self.rect.y += self.direction_y * self.velocidade
        self.rect.x += self.direction_x * self.velocidade

        if self.rect.y <= 0 or self.rect.y >= ALTURA_TELA - self.image.get_height():
            self.change_direction_y()
        if self.rect.x <= 0 or self.rect.x >= LARGURA_TELA - self.image.get_width():
            self.change_direction_x()

    def update(self):
        self.move()
