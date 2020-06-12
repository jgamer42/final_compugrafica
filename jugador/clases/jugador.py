
import math
import os
import sys

import ambiente
import globales
import pygame
from constantes import *
from utilidades import *

sys.path.append(os.getcwd() + "/motor/")



class Jugador(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.tipo = "jugador"
        self.vidas = 1
        self.salud = 1000
        self.puntos = 0
        self.animacion = self.crear_animacion()
        self.frame = 0
        self.direccion = 0
        self.aux_animacion = 0
        self.image = self.animacion[self.aux_animacion][self.frame]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0
        self.saltando = False
        self.bloques = None
        self.choque = False
        self.game_over = False

    def update(self):
        self.rect.x += self.velx
        ls_col = pygame.sprite.spritecollide(self,self.bloques,False,pygame.sprite.collide_mask)
        if len(ls_col) > 0:
            for b in ls_col:
                self.choque = True
                if self.velx > 0:
                    if self.rect.right > b.rect.left or self.rect.left > objeto.rect.left or self.rect.left > objeto.rect.right:
                        self.rect.right = b.rect.left
                        self.velx = 0
                elif self.velx < 0:
                    if self.rect.left < b.rect.right or self.rect.right < objeto.rect.right or self.rect.left < objeto.rect.left:
                        self.rect.left = b.rect.right
                        self.velx = 0
        else:
            self.choque = False

        self.rect.y += self.vely
        ls_col = pygame.sprite.spritecollide(self,self.bloques,False,pygame.sprite.collide_mask)
        if len(ls_col) > 0:
            for b in ls_col:
                if self.vely > 0:
                    if self.rect.bottom > b.rect.top:
                        self.saltando = False
                        self.rect.bottom = b.rect.top
                        self.vely = 0
                elif self.vely < 0:
                    if self.rect.top < b.rect.bottom:
                        self.rect.top = b.rect.bottom
                        self.vely = 0
        else:
            ambiente.gravedad(self)

        if self.rect.bottom > ALTO:
            self.vidas -= 1
            if self.vidas == 0:
                self.game_over = True

        self.comportamiento_limites()
        self.frame = animar(self.frame, 28, self.direccion)
        self.image = self.animacion[self.aux_animacion][self.frame]
        self.mask = pygame.mask.from_surface(self.image)


    def comportamiento_limites(self):
        if self.choque == True:
            globales.velx_entorno = 0
        else:
            if self.rect.x <= 0 or self.rect.right >= ANCHO:
                self.velx = 0
                globales.velx_entorno = -10 * self.direccion
                if self.rect.x < 0 :
                    self.rect.x = 0
                elif self.rect.right > ANCHO:
                    self.rect.right = ANCHO
            else:
                globales.velx_entorno = 0

    def controles(self,keys):
        if not keys[pygame.K_a] or not keys[pygame.K_d]:
                self.velx = 0
                self.direccion = 0
        if keys[pygame.K_a]:
            self.direccion = -1
            self.aux_animacion = 1
            if keys[pygame.K_LSHIFT]:
                    self.velx = -14
            else:
                self.velx = -8
        if keys[pygame.K_d]:
            self.direccion = 1
            self.aux_animacion = 0
            if keys[pygame.K_LSHIFT]:
                    self.velx = 14
            else:
                self.velx = 8
        if keys[pygame.K_SPACE]:
            if not self.saltando:
                self.vely = -50
                self.saltando = True

    def crear_animacion(self):
        animacion = []
        animacion.append(crear_sprite("./jugador/sprites/derecha.png", [41,60], 6, 5))
        animacion.append(crear_sprite("./jugador/sprites/izquierda.png", [41,60], 6, 5))
        return animacion
