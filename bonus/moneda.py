import sys
import os
import pygame as pg
sys.path.append(os.getcwd() + "/motor/")
import utilidades as util
import globales
import pygame as pg
import utilidades as util

sys.path.append(os.getcwd() + "/motor/")
class Moneda(pg.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.frame = 0
        self.animacion = util.crear_sprite("./bonus/GoldenCoin.png",[64,64],7)
        self.image = self.animacion[self.frame]
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.puntos = 30

    def update(self):
        self.frame = util.animar(self.frame,7,1)
        self.image = self.animacion[self.frame]
        self.rect.x += globales.velx_entorno
        self.rect.y += globales.vely_entorno
