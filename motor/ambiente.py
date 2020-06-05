import pygame
import sys
import os

sys.path.append(os.getcwd() + "/motor/")
from globales import *
from constantes import *


def ciclo_juego(ventana, elementos_dibujar):
    ventana.fill(ROJO)
    for grupo_sprites in elementos_dibujar:
        grupo_sprites.update()
        grupo_sprites.draw(ventana)
    pygame.display.flip()
    reloj.tick(30)
# TODO pulir la colision
def control_colision(lista_colision, jugador):
    for colision in lista_colision:
        if jugador.vely != 0:
            jugador.vely = 0


def gravedad(objeto):
    if objeto.vely == 0:
        objeto.vely = GRAVEDAD
    else:
        objeto.vely += GRAVEDAD
