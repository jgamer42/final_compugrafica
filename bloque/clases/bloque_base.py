import globales
import ambiente
from constantes import *
import pygame
import sys
import os

sys.path.append(os.getcwd() + "/motor/")


class Bloque_base(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0
        self.image.fill(VERDE)

    def update(self):
        self.vely = globales.vely_entorno
        self.velx = globales.velx_entorno
        self.rect.x += self.velx
        self.rect.y += self.vely
