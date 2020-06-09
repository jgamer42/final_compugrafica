import os
import sys

import ambiente
import globales
import pygame
from constantes import *

sys.path.append(os.getcwd() + "/motor/")

class Bloque_base(pygame.sprite.Sprite):
    def __init__(self, pos, img=None):
        super().__init__()
        if img == None:
            self.image = pygame.Surface([50, 50])
            self.image.fill(VERDE)
        else:
            self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0

    def update(self):
        self.vely = globales.vely_entorno
        self.velx = globales.velx_entorno
        self.rect.x += self.velx
        self.rect.y += self.vely
