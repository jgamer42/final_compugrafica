import os
import sys

import globales as glob
import pygame as pg
from motor.constantes import *

sys.path.append(os.getcwd() + "/motor/")

fondo = pg.image.load("./menu/Inicio.png")
IconoJugar = pg.image.load("./menu/IconoJugar.png")
IconoOpciones = pg.image.load("./menu/IconoOpciones.png")
IconoCreditos = pg.image.load("./menu/IconoCreditos.png")
IconoSalir = pg.image.load("./menu/IconoSalir.png")


class Icono(pg.sprite.Sprite):
    def __init__(self,pos,icon):
        pg.sprite.Sprite.__init__(self)
        self.image = icon
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.click = False


iconos = pg.sprite.Group()
jugar = Icono([917,297],IconoJugar)
iconos.add(jugar)
opciones = Icono([917,389],IconoOpciones)
iconos.add(opciones)
creditos = Icono([917,482],IconoCreditos)
iconos.add(creditos)
salir = Icono([917,575],IconoSalir)
iconos.add(salir)
#print(glob.cosa)
def menu_inicio(ventana,niveles, mouse,click):
    ventana.fill(NEGRO)
    ventana.blit(fondo,[0,0])

    if jugar.rect.collidepoint(mouse):
        print("colisionando en jugar")
        if click[0] == 1:
            ventana.blit(IconoJugar,[917,297])
            niveles["inicio"] = False
            niveles["nivel1"] = True
        else:
            ventana.blit(IconoJugar,[917,297])
    elif opciones.rect.collidepoint(mouse):
        if click[0] == 1:
            print("opciones")
            ventana.blit(IconoOpciones,[917,389])
            niveles["inicio"] = False
            niveles["opciones"] = True
        else:
            ventana.blit(IconoOpciones,[917,389])
    elif creditos.rect.collidepoint(mouse):
        if click[0] == 1:
            print("creditos")
            ventana.blit(IconoCreditos,[917,482])
            niveles["inicio"] = False
            niveles["creditos"] = True
        else:
            ventana.blit(IconoCreditos,[917,482])
    elif salir.rect.collidepoint(mouse):
        if click[0] == 1:
            print("salir")
            ventana.blit(IconoSalir,[917,575])
            niveles["inicio"] = False
            return False
        else:
            ventana.blit(IconoSalir,[917,575])
    pg.display.flip()
    return True
