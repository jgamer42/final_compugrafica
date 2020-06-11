import os
import sys
sys.path.append(os.getcwd() + "/motor/")
import globales
import pygame
from constantes import *

fondos_mapas = {"mapaA1":pygame.image.load("mapa/mapaA1.png")}

def ciclo_juego(ventana, elementos_dibujar):
    global fondos_mapas
    ventana.fill(NEGRO)
    ventana.blit(fondos_mapas["mapaA1"],velocidad_fondo())
    for grupo_sprites in elementos_dibujar:
        grupo_sprites.update()
        grupo_sprites.draw(ventana)
    pygame.display.flip()

def velocidad_fondo():
    globales.x_fondo += globales.velx_entorno
    globales.y_fondo += globales.vely_entorno
    return [globales.x_fondo,globales.y_fondo]

def gravedad(objeto):
    if objeto.vely == 0:
        objeto.vely = GRAVEDAD
    else:
        objeto.vely += GRAVEDAD

