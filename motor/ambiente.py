import pygame
import sys
import os

sys.path.append(os.getcwd() + "/motor/")
import globales
from constantes import *

def ciclo_juego(ventana, elementos_dibujar):
    ventana.fill(NEGRO)
    ventana.blit(globales.fondos_mapas["mapaA1"],velocidad_fondo())
    for grupo_sprites in elementos_dibujar:
        grupo_sprites.update()
        grupo_sprites.draw(ventana)
    pygame.display.flip()
    globales.reloj.tick(30)

# TODO pulir la colision
def control_colision(lista_colision, jugador):
    for colision in lista_colision:
        if not jugador.estados["saltando"]:
            if jugador.vely != 0:
                jugador.vely = 0
                #jugador.rect.bottom = colision.rect.top

        if jugador.rect.bottom > ALTO:
            jugador.vely = 0
            jugador.estados["saltando"] = False
            jugador.rect.bottom = colision.rect.top
        '''
        if jugador.direccion == 1:
            if jugador.rect.right > colision.rect.left:
                jugador.rect.right = colision.rect.left
                jugador.velx = 0
        if jugador.direccion == -1:
            if jugador.rect.left < colision.rect.right:
                jugador.rect.left = colision.rect.right
                jugador.velx = 0
        '''

def velocidad_fondo():
    globales.x_fondo += globales.velx_entorno
    globales.y_fondo += globales.vely_entorno
    return [globales.x_fondo,globales.y_fondo]

def gravedad(objeto):
    if objeto.vely == 0:
        objeto.vely = GRAVEDAD
    else:
        objeto.vely += GRAVEDAD
