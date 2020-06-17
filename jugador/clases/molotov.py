import os
import sys
import pygame as pg
sys.path.append(os.getcwd() + "/motor/")
sys.path.append(os.getcwd() + "/enemigos/clases/balas/")
from bala_base import Bala_base
from constantes import *
from ambiente import *
from utilidades import *


class Molotov(Bala_base):
    def __init__(self,pos):
        super().__init__(pos,1)
        self.animacion = crear_sprite("./jugador/sprites/molotov.png",[32,32],3)
        self.frame = 0
        self.velx = 30
        self.vely = -35
        self.direccion = 1
        self.image = self.animacion[self.frame]
        self.mask = pg.mask.from_surface(self.image)
        self.type = "molotov"
        self.efecto = 130

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
        gravedad(self)
        self.frame = animar(self.frame,3,self.direccion)
        self.image = self.animacion[self.frame]
        self.mask = pg.mask.from_surface(self.image)
