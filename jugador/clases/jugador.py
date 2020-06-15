
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
        self.posInicial = pos
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
        self.game_over = False

    def update(self):
        self.rect.x += self.velx
        self.colision_x()
        self.rect.y += self.vely
        self.colision_y()
        self.checkGameOver()
        self.comportamiento_limites()
        self.frame = animar(self.frame, 28, self.direccion)
        self.image = self.animacion[self.aux_animacion][self.frame]
        self.mask = pygame.mask.from_surface(self.image)

    def colision_x(self):
        lista_colision = pygame.sprite.spritecollide(self,self.bloques,False,pygame.sprite.collide_mask)
        if len(lista_colision) > 0:
            for colision in lista_colision:
                self.choque = True
                if self.velx > 0:
                    if self.rect.right > colision.rect.left or self.rect.left > colision.rect.left or self.rect.left > colision.rect.right:
                        self.rect.right = colision.rect.left
                        self.velx = 0
                        if colision.tipo == "lava":
                            self.salud -= colision.daño
                elif self.velx < 0:
                    if self.rect.left < colision.rect.right or self.rect.right < colision.rect.right or self.rect.left < colision.rect.left:
                        self.rect.left = colision.rect.right
                        self.velx = 0
                        if colision.tipo == "lava":
                            self.salud -= colision.daño
        else:
            self.choque = False

    def colision_y(self):
        lista_colision = pygame.sprite.spritecollide(self,self.bloques,False,pygame.sprite.collide_mask)
        if len(lista_colision) > 0:
            for colision in lista_colision:
                if self.vely > 0:
                    if self.rect.bottom > colision.rect.top:
                        self.saltando = False
                        self.rect.bottom = colision.rect.top
                        self.vely = 0
                        if colision.tipo == "pinchos" or colision.tipo == "lava":
                            self.salud -= colision.daño
                elif self.vely < 0:
                    if self.rect.top < colision.rect.bottom:
                        self.rect.top = colision.rect.bottom
                        self.vely = 0
                        if colision.tipo == "pinchos" :
                            self.salud -= colision.daño
        else:
            ambiente.gravedad(self)


        if self.rect.bottom > ALTO:
            self.vidas -= 1
            if self.vidas == 0:
                self.game_over = True
                #self.reiniciar()

        self.comportamiento_limites()
        self.frame = animar(self.frame, 28, self.direccion)
        self.image = self.animacion[self.aux_animacion][self.frame]
        self.mask = pygame.mask.from_surface(self.image)

    def checkGameOver(self):
        if self.rect.bottom > ALTO:
            self.vidas -= 1
            if self.vidas == 0:
                self.game_over = True

    def checkSalud(self):
        pass

    def comportamiento_limites(self):
        if self.moverCamara():
            if self.choque == True:
                globales.velx_entorno = 0
            else:
                if self.rect.x <= 0 or self.rect.right >= ANCHO - 64 * 5:
                    self.velx = 0
                    globales.velx_entorno = -10 * self.direccion
                    if self.rect.x < 0 :
                        self.rect.x = 0
                    elif self.rect.right > ANCHO:
                        self.rect.right = ANCHO
                else:
                    globales.velx_entorno = 0

    def moverCamara(self):
        #se debe evaluar si el fondo esta al limite
        return True

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
                self.vely = -36
                self.saltando = True

    def crear_animacion(self):
        animacion = []
        animacion.append(crear_sprite("./jugador/sprites/derecha.png", [41,60], 6, 5))
        animacion.append(crear_sprite("./jugador/sprites/izquierda.png", [41,60], 6, 5))
        return animacion
