
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
    def __init__(self, pos, bloques, bonus):
        super().__init__()
        self.posInicial = pos
        self.grunt = pygame.mixer.Sound('./sonidos/grunt.ogg')
        self.tipo = "jugador"
        self.vidas = 3
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
        self.bloques = bloques
        self.bonus = bonus
        self.time = None
        
    def update(self):
        self.rect.x += self.velx
        self.colision_x()
        self.rect.y += self.vely
        self.colision_y()

        self.checkColisiones()
        self.comportamiento_limites()
        self.checkEstado()
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
                            print(colision.tipo)
                            self.grunt.play()
                            print(self.salud)
                elif self.vely < 0:
                    if self.rect.top < colision.rect.bottom:
                        self.rect.top = colision.rect.bottom
                        self.vely = 0
                        if colision.tipo == "pinchos" or colision.tipo == "lava" :
                            self.salud -= colision.daño
                            print(colision.tipo)
                            self.grunt.play()
                            print(self.salud)
        else:
            ambiente.gravedad(self)

        self.comportamiento_limites()
        self.frame = animar(self.frame, 28, self.direccion)
        self.image = self.animacion[self.aux_animacion][self.frame]
        self.mask = pygame.mask.from_surface(self.image)

    def checkEstado(self):
        if (self.rect.bottom > ALTO + 100) or (self.time == '0:00'):
            self.vidas -= 1
        elif self.salud <= 0:
            self.vidas -= 1
            self.salud = 1000
    def checkGameOver(self,gameOver,estados):
        if self.vidas == 0:
            gameOver = True
            estados["nivel1"] = False
            estados["inicio"] = True
            self.reiniciar()

    #Esto es la camara
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
        else:
            globales.velx_entorno = 0

    def moverCamara(self):
        #se debe evaluar si el fondo esta al limite
        if self.rect.right + 150 >= 7680 or self.rect.left - 150 <= 0:
            return False
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

    def sumarPuntos(self,puntos):
        self.puntos += puntos


    def restarVida(self,cantidad):
        jugador.vida -= cantidad

    def setTime(self,time):
        self.time = time

    def reiniciar(self):
        self.vidas = 3
        self.salud = 1000
        self.puntos = 0
        self.frame = 0
        self.direccion = 0
        self.aux_animacion = 0
        self.rect.x = self.posInicial[0]
        self.rect.y = self.posInicial[1]
        self.velx = 0
        self.vely = 0
        self.saltando = False

    def checkColisiones(self):
        ls_col = pygame.sprite.spritecollide(self,self.bonus,False,pygame.sprite.collide_mask)
        if len(ls_col) > 0:
            for bono in ls_col:
                self.sumarPuntos(bono.puntos)
                self.bonus.remove(bono)
