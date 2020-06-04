import ambiente
import globales
from constantes import *
from utilidades import *
import math
import os
import sys
import pygame

sys.path.append(os.getcwd() + "/motor/")


class Jugador(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.vidas = 3
        self.salud = 1000
        self.puntos = 0
        self.animacion = self.crear_animacion()
        self.frame = 0
        self.direccion = 1
        self.aux_animacion = 0
        self.image = self.animacion[self.aux_animacion][self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0
        self.estados = {"saltando": False, "corriendo": False}

    def update(self):
        self.frame = animar(self.frame, 28)
        self.image = self.animacion[self.aux_animacion][self.frame]
        self.rect.x += self.velx
        self.rect.y += self.vely
        ambiente.gravedad(self)
        self.comportamiento_limites()

    def comportamiento_limites(self):
        if self.rect.bottom > ALTO:
            self.estados["saltando"] = False
            self.rect.bottom = ALTO
            self.vely = 0

        if self.rect.x <= 0 or self.rect.right >= ANCHO:
            self.velx = 0
            globales.velx_entorno = 10 * self.direccion
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
                    self.velx = 8
                else:
                    self.velx = 3
            if evento.key == pygame.K_a:
                self.direccion = -1
                self.aux_animacion = 1
                if self.estados["corriendo"]:
                    self.velx = -8
                else:
                    self.velx = -3
            if evento.key == pygame.K_SPACE:
                if not self.estados["saltando"]:
                    self.estados["saltando"] = True
                    self.vely = -50
        if evento.type == pygame.KEYUP:
            if (evento.key == pygame.K_a) or (evento.key == pygame.K_d):
                self.velx = 0
            if evento.key == pygame.K_s:
                self.estados["corriendo"] = False

    def crear_animacion(self):
        animacion = []
        sabana_derecha = pygame.image.load("./jugador/sprites/derecha.png")
        sabana_izquierda = pygame.image.load("./jugador/sprites/izquierda.png")
        animacion.append(crear_sprite(sabana_derecha, [128, 184], 6, 5))
        animacion.append(crear_sprite(sabana_izquierda, [128, 184], 6, 5))
        return animacion
