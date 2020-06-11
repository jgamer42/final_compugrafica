import os
import sys
sys.path.append(os.getcwd() + "/motor/")
import globales as glob
import pygame as pg
from motor.constantes import *


class Icono(pg.sprite.Sprite):
    def __init__(self,pos,icon):
        pg.sprite.Sprite.__init__(self)
        self.image = icon
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.click = False

fondo = pg.image.load("./menu/Inicio.png")
iconos = pg.sprite.Group()

IconoJugar = pg.image.load("./menu/IconoJugar.png")
jugar = Icono([917,297],IconoJugar)
iconos.add(jugar)

IconoOpciones = pg.image.load("./menu/IconoOpciones.png")
opciones = Icono([917,389],IconoOpciones)
iconos.add(opciones)

IconoCreditos = pg.image.load("./menu/IconoCreditos.png")
creditos = Icono([917,482],IconoCreditos)
iconos.add(creditos)

IconoSalir = pg.image.load("./menu/IconoSalir.png")
salir = Icono([917,575],IconoSalir)
iconos.add(salir)

def menu_inicio(ventana,niveles, mouse,click):
    ventana.fill(NEGRO)
    ventana.blit(fondo,[0,0])
    if jugar.rect.collidepoint(mouse):
        if click[0] == 1:
            ventana.blit(IconoJugar,[917,297])
            niveles["inicio"] = False
            niveles["nivel1"] = True
        else:
            ventana.blit(IconoJugar,[917,297])
    elif opciones.rect.collidepoint(mouse):
        if click[0] == 1:
            ventana.blit(IconoOpciones,[917,389])
            niveles["inicio"] = False
            niveles["opciones"] = True
        else:
            ventana.blit(IconoOpciones,[917,389])
    elif creditos.rect.collidepoint(mouse):
        if click[0] == 1:
            ventana.blit(IconoCreditos,[917,482])
            niveles["inicio"] = False
            niveles["creditos"] = True
        else:
            ventana.blit(IconoCreditos,[917,482])
    elif salir.rect.collidepoint(mouse):
        if click[0] == 1:
            ventana.blit(IconoSalir,[917,575])
            niveles["inicio"] = False
            return False
        else:
            ventana.blit(IconoSalir,[917,575])
    pg.display.flip()
    return True
