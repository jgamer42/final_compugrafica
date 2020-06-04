import pygame
import sys
import os
from .constantes import *
from .globales import *


def ciclo_juego(ventana, elementos_dibujar):
    ventana.fill(NEGRO)
    for grupo_sprites in elementos_dibujar:
        grupo_sprites.update()
        grupo_sprites.draw(ventana)
    pygame.display.flip()
    reloj.tick(30)
