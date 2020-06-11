import os
import sys

import pygame
from constantes import *

sys.path.append(os.getcwd()+"/motor/")
sys.path.append(os.getcwd()+"/enemigos/")

class  Enemigo_base(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.lista_observadores = []
        self.estado = {
            "disparando":
                {
                    "bandera": False,
                    "tiempo": 50
                }
            }
        self.registro = 0
        self.image = pygame.Surface([50, 50])
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0

    def agregar_observador(self,observador):
        self.lista_observadores.append(observador)

    def update(self):
        if self.registro == self.estado["disparando"]["tiempo"]:
            self.registro = 0
            self.notificar()
        else:
            self.registro += 1

    def notificar(self):
        for observador in self.lista_observadores:
            observador.informar()


class Observador:
    def __init__(self,sujeto):
        self.observado = sujeto.agregar_observador(self)

    def informar(self):
        #print("notificado")
        pass
