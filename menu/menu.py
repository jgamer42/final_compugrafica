import os
import sys

import pygame as pg
from motor.constantes import *
from motor.utilidades import *

sys.path.append(os.getcwd() + "/motor/")

pygame.init()

class Icono(pg.sprite.Sprite):
    def __init__(self,pos,icon):
        pg.sprite.Sprite.__init__(self)
        self.image = icon
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.click = False

#pg.mixer.init()
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

FondContr = pg.image.load("./menu/controles.png")

IconoAceptar = pg.image.load("./menu/IconoAceptar.png")
aceptar = Icono([992,602], IconoAceptar)
iconos.add(aceptar)

IconoSonidoON = pg.image.load("./menu/iconoSonidoON.png")
IconoSonidoOFF = pg.image.load("./menu/iconoSonidoOFF.png")
sonido = Icono([506,559], IconoSonidoOFF)
iconos.add(sonido)

def inicio(ventana,opInicio,estados,mouse,click,sonidos):
    if opInicio["opciones"]:
        ventana.fill(NEGRO)
        if sonidos.getMudo():
            ventana.blit(FondContr,[0,0])
            ventana.blit(IconoSonidoOFF,[506,559])
        else:
            ventana.blit(FondContr,[0,0])
        if aceptar.rect.collidepoint(mouse):
            if click[0] == 1:
                sonidos.click()
                ventana.blit(IconoAceptar,[992,602])
                opInicio["opciones"] = False
            else:
                ventana.blit(IconoAceptar,[992,602])
        elif sonido.rect.collidepoint(mouse):
            if sonidos.getMudo():
                if click[0] == 1:
                    ventana.blit(IconoSonidoON,[506,559])
                    sonidos.click()
                    sonidos.mudo()
                else:
                    ventana.blit(IconoSonidoON,[506,559])
            else:
                if click[0] == 1:
                    ventana.blit(IconoSonidoOFF,[506,559])
                    sonidos.click()
                    sonidos.mudo()
                else:
                    ventana.blit(IconoSonidoOFF,[506,559])
    elif opInicio["creditos"]:
        pass
    else:
        ventana.fill(NEGRO)
        ventana.blit(fondo,[0,0])
        if jugar.rect.collidepoint(mouse):
            if click[0] == 1:
                sonidos.click()
                ventana.blit(IconoJugar,[917,297])
                estados["inicio"] = False
                estados["nivel1"] = True
            else:
                ventana.blit(IconoJugar,[917,297])
        elif opciones.rect.collidepoint(mouse):
            if click[0] == 1:
                sonidos.click()
                ventana.blit(IconoOpciones,[917,389])
                opInicio["opciones"] = True
            else:
                ventana.blit(IconoOpciones,[917,389])
        elif creditos.rect.collidepoint(mouse):
            if click[0] == 1:
                sonidos.click()
                ventana.blit(IconoCreditos,[917,482])
                opInicio["creditos"] = True
            else:
                ventana.blit(IconoCreditos,[917,482])
        elif salir.rect.collidepoint(mouse):
            if click[0] == 1:
                sonidos.click()
                ventana.blit(IconoSalir,[917,575])
                estados["inicio"] = False
                return False
            else:
                ventana.blit(IconoSalir,[917,575])
    pg.display.flip()
    return True
