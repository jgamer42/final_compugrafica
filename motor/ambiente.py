import os
import sys

import globales
import pygame
from constantes import *

sys.path.append(os.getcwd() + "/motor/")
fondos_mapas = {"mapaA1Fondo":pygame.image.load("mapa/mapaA1Fondo.png")}
balas_enemigos = None

def ciclo_juego(ventana,elementos_dibujar,gui):
    global fondos_mapas
    global balas_enemigos
    ventana.fill(NEGRO)
    ventana.blit(fondos_mapas["mapaA1Fondo"],velocidad_fondo())
    #print(balas_enemigos)
    #print(len(balas_enemigos))
    for grupo_sprites in elementos_dibujar:
        grupo_sprites.update()
        grupo_sprites.draw(ventana)
    gui.update()
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

def protector_memoria(elementos):
    for elemento in elementos:
        for e in elemento:
            if(e.rect.bottom <= 0) or (e.rect.top > ALTO):
                elemento.remove(e)
            if(e.rect.x <= 0) or (e.rect.x > ANCHO):
                elemento.remove(e)
