import os
import sys

import ambiente
import pygame as pg
from constantes import *
from utilidades import *

sys.path.append(os.getcwd() + "/motor/")


class GUI():
    def __init__(self,jugador,interfaz):
        self.interfaz = interfaz
        self.barra = pg.image.load("./gui/bar.png")
        self.numeros = crear_sprite("./gui/numeros.png",[14,19],10)
        self.vida = crear_sprite("./gui/vida.png",[33,28],3)
        self.posVidas = [[644,2],[681,2],[718,2]]
        self.jugador = jugador

    def update(self):
        self.interfaz.blit(self.barra,[0,0])
        self.drawPuntos()
        self.drawVida()
        self.drawTime()

    def drawPuntos(self):
        miles = self.jugador.puntos/1000
        centena = (self.jugador.puntos - ((int(self.jugador.puntos/1000))*1000))/100
        decena = (self.jugador.puntos % 100)/10
        unidad = decena % 10

        if int(miles) != 0:
            ventana.blit(self.numeros[int(miles)],[160,5])
        if int(centena) != 0 or miles > 0:
            ventana.blit(self.numeros[int(centena)],[177,5])
        if int(decena) != 0 or centena > 0 or miles > 0:
            ventana.blit(self.numeros[int(decena)],[194,5])

        self.interfaz.blit(self.numeros[int(unidad)],[211,5])
        pg.display.flip()

    def drawVida(self):
        if self.jugador.salud > 500 and self.jugador.vidas == 3:
            self.interfaz.blit(self.vida[0],self.posVidas[0])
            self.interfaz.blit(self.vida[0],self.posVidas[1])
            self.interfaz.blit(self.vida[0],self.posVidas[2])
        if self.jugador.salud <= 500 and self.jugador.vidas == 3:
            self.interfaz.blit(self.vida[0],self.posVidas[0])
            self.interfaz.blit(self.vida[0],self.posVidas[1])
            self.interfaz.blit(self.vida[1],self.posVidas[2])
        if self.jugador.salud > 500 and self.jugador.vidas == 2:
            self.interfaz.blit(self.vida[0],self.posVidas[0])
            self.interfaz.blit(self.vida[0],self.posVidas[1])
            self.interfaz.blit(self.vida[2],self.posVidas[2])
        if self.jugador.salud <= 500 and self.jugador.vidas == 2:
            self.interfaz.blit(self.vida[0],self.posVidas[0])
            self.interfaz.blit(self.vida[1],self.posVidas[1])
            self.interfaz.blit(self.vida[2],self.posVidas[2])
        if self.jugador.salud > 500 and self.jugador.vidas == 1:
            self.interfaz.blit(self.vida[0],self.posVidas[0])
            self.interfaz.blit(self.vida[2],self.posVidas[1])
            self.interfaz.blit(self.vida[2],self.posVidas[2])
        if self.jugador.salud <= 500 and self.jugador.vidas == 1:
            self.interfaz.blit(self.vida[1],self.posVidas[0])
            self.interfaz.blit(self.vida[2],self.posVidas[1])
            self.interfaz.blit(self.vida[2],self.posVidas[2])
        if self.jugador.vidas == 0:
            self.interfaz.blit(self.vida[2],self.posVidas[0])
            self.interfaz.blit(self.vida[2],self.posVidas[1])
            self.interfaz.blit(self.vida[2],self.posVidas[2])


    def drawTime(self):
        pass
