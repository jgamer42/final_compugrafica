
import math
import os
import sys
import pygame

sys.path.append(os.getcwd() + "/motor/")
import ambiente
import globales
from constantes import *
from utilidades import *

class Jugador(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.vidas = 3
        self.salud = 1000
        self.puntos = 0
        self.animacion = self.crear_animacion()
        self.frame = 0
        self.direccion = 0
        self.aux_animacion = 0
        self.image = self.animacion[self.aux_animacion][self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0
        self.estados = {"saltando": False, "corriendo": False}

    def update(self):
        self.frame = animar(self.frame, 28, self.direccion)
        self.image = self.animacion[self.aux_animacion][self.frame]
        self.rect.x += self.velx
        self.rect.y += self.vely
        self.comportamiento_limites()
        ambiente.gravedad(self)

    def comportamiento_limites(self):
        #limites derechos e izquierdos
        if self.rect.x <= 0 or self.rect.right >= ANCHO:
            self.velx = 0
            globales.velx_entorno = -10 * self.direccion
            if self.direccion == -1:
                self.rect.x = 0
            else:
                self.rect.right = ANCHO
        else:
            globales.velx_entorno = 0

    def controles(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_s:
                self.estados["corriendo"] = True
            if evento.key == pygame.K_d:
                self.direccion = 1
                self.aux_animacion = 0
                if self.estados["corriendo"]:
                    self.velx = 16
                else:
                    self.velx = 11
            if evento.key == pygame.K_a:
                self.direccion = -1
                self.aux_animacion = 1
                if self.estados["corriendo"]:
                    self.velx = -16
                else:
                    self.velx = -11
            if evento.key == pygame.K_SPACE:
                if not self.estados["saltando"]:
                    self.estados["saltando"] = True
                    self.vely = -50
                else:
                    self.estados["saltando"] = False
        if evento.type == pygame.KEYUP:
            if (evento.key == pygame.K_a) or (evento.key == pygame.K_d):
                self.velx = 0
            if evento.key == pygame.K_s:
                self.estados["corriendo"] = False

    def crear_animacion(self):
        animacion = []
        animacion.append(crear_sprite("./jugador/sprites/derecha.png", [64,92], 6, 5))
        animacion.append(crear_sprite("./jugador/sprites/izquierda.png", [64,92], 6, 5))
        return animacion
