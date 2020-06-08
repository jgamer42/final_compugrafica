import os
import sys
sys.path.append(os.getcwd() + "/motor/")
import globales
import pygame
from constantes import *

def ciclo_juego(ventana, elementos_dibujar):
    ventana.fill(NEGRO)
    ventana.blit(globales.fondos_mapas["mapaA1"],velocidad_fondo())
    for grupo_sprites in elementos_dibujar:
        grupo_sprites.update()
        grupo_sprites.draw(ventana)
    pygame.display.flip()
    globales.reloj.tick(30)

def velocidad_fondo():
    globales.x_fondo += globales.velx_entorno
    globales.y_fondo += globales.vely_entorno
    return [globales.x_fondo,globales.y_fondo]

def gravedad(objeto):
    if objeto.vely == 0:
        objeto.vely = GRAVEDAD
    else:
        objeto.vely += GRAVEDAD

def control_colision(jugador,lista_colision):
    pass