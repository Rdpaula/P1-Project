import pygame
import pygame.gfxdraw
from constantes import *

class Bloco(pygame.sprite.Sprite):
    def __init__(self,vida,x,y,largura,altura,poder=0):
        pygame.sprite.Sprite.__init__(self)
        self.vida = vida
        self.image = pygame.Surface([largura,altura])
        self.image.fill(CORES_VIDA[self.vida])
        self.rect = self.image.get_rect()
        self.poder = poder
        self.rect.x = x
        self.rect.y = y

    def perder_vida(self):
        """
            Remove vida do bloco e atualiza cor
        """
        self.vida -= 1
        self.image.fill(CORES_VIDA[self.vida])
    
    def update (self):
        pass
