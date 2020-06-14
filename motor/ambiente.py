import os
import sys

import globales
import pygame
from constantes import *

sys.path.append(os.getcwd() + "/motor/")
fondos_mapas = {"mapaA1":pygame.image.load("mapa/mapaA1.png")}
balas_enemigos = None

def ciclo_juego(ventana, elementos_dibujar):
    global fondos_mapas
    global balas_enemigos
    ventana.fill(NEGRO)
    ventana.blit(fondos_mapas["mapaA1"],velocidad_fondo())
    #print(balas_enemigos)
    #print(len(balas_enemigos))
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
    
def agregar_bala(objeto,fuente):
    global balas_enemigos
    if fuente == "jugador":
        pass
    elif fuente == "enemigo":
        balas_enemigos = objeto
        #balas_enemigos.add(objeto)
        #print(balas_enemigos)
        #balas_enemigos.append("hola")
    print(balas_enemigos)
