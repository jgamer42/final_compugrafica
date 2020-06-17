import os
import sys

import pygame as pg
from constantes import *

sys.path.append(os.getcwd()+"/motor/")
sys.path.append(os.getcwd()+"/enemigos/")

class Bala_base(pg.sprite.Sprite):
    def __init__(self, pos,direccion):
        super().__init__()
        self.image = pg.Surface([20, 20])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0
        self.direccion = direccion
        self.tipo = "bala base"
        self.daño = 50

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
