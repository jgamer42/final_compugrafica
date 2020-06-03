import math
import os
import sys

import pygame
from constantes import *
from utilidades import *

sys.path.append(os.getcwd() + "/ambiente/")


class Jugador(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.vidas = 3
        self.salud = 1000
        self.puntos = 0
        self.speed = False
        self.salto = False

        self.animacion = self.crear_animacion()
        self.frame = 0
        self.direccion = 0
        self.image = self.animacion[self.direccion][self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.velx = 0
        self.vely = 0

    def update(self):
        self.frame = next_frame(self.frame, 28)
        self.animar()
        self.rect.x += self.velx
        self.rect.y += self.vely
        self.gravedad(0.3)
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO
            self.vely = 0

    def gravedad(self, g=0.5):
        if self.vely == 0:
            self.vely = g
            self.salto = False
        else:
            self.vely += g

    def controles(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_s:
                self.speed = True
            if evento.key == pygame.K_d:
                if self.speed:
                    self.velx = 8
                    self.vely = 0
                else:
                    self.velx = 3
                    self.vely = 0
            if evento.key == pygame.K_a:
                if self.speed:
                    self.velx = -8
                    self.vely = 0
                else:
                    self.velx = -3
                    self.vely = 0
            if (evento.key == pygame.K_SPACE) and (self.salto == False):
                self.salto = True
                self.vely = -14
        if evento.type == pygame.KEYUP:
            if (evento.key == pygame.K_a) or (evento.key == pygame.K_d):
                self.velx = 0
            if evento.key == pygame.K_s:
                self.speed = False

    def animar(self):
        if self.velx > 0:
            self.direccion = 0
        elif self.velx < 0:
            self.direccion = 1

        pos_x = self.rect.x
        pos_y = self.rect.y
        self.image = self.animacion[self.direccion][self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def crear_animacion(self):
        animacion = []
        sabana_derecha = pygame.image.load("./jugador/sprites/derecha.png")
        sabana_izquierda = pygame.image.load("./jugador/sprites/izquierda.png")
        animacion.append(crear_sprite(sabana_derecha, [128, 184], 6, 5))
        animacion.append(crear_sprite(sabana_izquierda, [128, 184], 6, 5))
        return animacion
