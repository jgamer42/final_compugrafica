import os
import sys

import globales
import pygame
from constantes import *

sys.path.append(os.getcwd()+"/motor/")
sys.path.append(os.getcwd()+"/enemigos/")



class  Enemigo_base(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.lista_observadores = []
        self.image = pygame.Surface([50, 50])
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0
        self.direccion = 1

    def agregar_observador(self,observador):
        self.lista_observadores.append(observador)

    def update(self):
        if self.en_camara():
            self.rect.x += self.velx*self.direccion
            self.rect.y += self.vely*self.direccion
            self.animar()
            self.notificar()
        else:
            self.rect.x += globales.velx_entorno
            self.rect.y += globales.vely_entorno

    def notificar(self):
        for observador in self.lista_observadores:
            observador.informar()

    def en_camara(self):
        if self.rect.right > 64*2 and self.rect.right < ANCHO-64*2:
            return True
        else:
            return False

    def animar(self):
        pass
