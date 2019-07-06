import pygame
import os 
from constantes import *
DIRETORIO = os.getcwd()

class player(pygame.sprite.Sprite):
    def __init__(self, sprite, pos_x, pos_y, velocidade=1):# initiating player
        super(pygame.sprite.Sprite,self).__init__()
        self.__initialposition_position = (pos_x,pos_y)
        self.image = pygame.image.load(DIRETORIO+"/images/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.velocidade = velocidade
        self.vidas = 3
        self.screen = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA))
        self.left=False
        self.right=False
    def posicao_inicial(self): # definition of initial position
        self.rect.x = self.__initial_position[0]
        self.rect.y = self.__initial_position[1]

    def die(self):
        # self.som_losslife = pygame.mixer.Sound
        self.posicao_inicial() # Reset position
        self.vidas -= 1 # loss life

    def update(self, evento):# moving the player 

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                self.left = True
            elif evento.key == pygame.K_RIGHT:
                self.right = True
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                self.left = False
            elif evento.key == pygame.K_RIGHT:
                self.right = False 
        if self.right and self.rect.right < (LARGURA_TELA - self.velocidade):
                self.rect.x += self.velocidade
        elif self.left and self.rect.left > self.velocidade:
                self.rect.x -= self.velocidade
        self.screen.blit(self.image,(self.rect.x,self.rect.y)) 
        pygame.display.update()
    def update2(self): # moving the player without new event

        if self.right and self.rect.right < (LARGURA_TELA - self.velocidade):
                self.rect.x += self.velocidade
        elif self.left and self.rect.left > self.velocidade:
                self.rect.x -= self.velocidade
        self.screen.blit(self.image,(self.rect.x,self.rect.y)) 
        pygame.display.update()

    
    
