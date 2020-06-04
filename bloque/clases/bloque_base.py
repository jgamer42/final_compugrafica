from constantes import *
import pygame
import sys
import os

sys.path.append(os.getcwd() + "/ambiente/")


class Bloque_base(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.image.fill(VERDE)
