
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
        self.estados = {"saltando": False, "corriendo": False,"cayendo":True}
        self.lista_colision = []

    def update(self):
        self.frame = animar(self.frame, 28, self.direccion)
        self.image = self.animacion[self.aux_animacion][self.frame]
        self.rect.x += self.velx
        self.rect.y += self.vely
        self.colision_y()
        self.comportamiento_limites()
        if self.estados["cayendo"]:
            ambiente.gravedad(self)
    
    def colision_y(self):
        for objeto in self.lista_colision:
            print("cayendo ",self.rect.bottom -132,",",objeto.rect.top)
            if self.estados["saltando"]:
                print("subiendo")
                self.rect.top = objeto.rect.bottom
                self.vely = 0
                self.estados["saltando"] = False
                #self.estados["cayendo"] = True
            else:
                if self.estados["cayendo"]:
                    print("entro")
                    self.rect.bottom = objeto.rect.top
                    self.vely = 0
                    self.estados["cayendo"]= False

    '''
    def colision_x(self,lista_colision):
        for colision in lista_colision:
            if self.velx > 0:
                if self.rect.right > colision.rect.left:
                    self.rect.right = colision.rect.left
                    self.velx = 0
            else:
                if self.rect.left < colision.rect.right:
                    self.rect.left = colision.rect.right
                    self.velx = 0
    '''


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
            if evento.key == pygame.K_LSHIFT:
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
                    self.estados["cayendo"] = True
                    self.vely = -50
                else:
                    self.estados["saltando"] = False
        if evento.type == pygame.KEYUP:
            if (evento.key == pygame.K_a) or (evento.key == pygame.K_d):
                self.velx = 0
                self.direccion = 0
            if evento.key == pygame.K_LSHIFT:
                self.estados["corriendo"] = False

    def crear_animacion(self):
        animacion = []
        animacion.append(crear_sprite("./jugador/sprites/derecha.png", [64,92], 6, 5))
        animacion.append(crear_sprite("./jugador/sprites/izquierda.png", [64,92], 6, 5))
        return animacion
