import os
import sys
import pygame as pg
sys.path.append(os.getcwd() + "/menu/")
from menu.menu import *

pg.init()

icoHistory = pg.sprite.Group()

IconoAceptar = pg.image.load("./menu/IconoAceptar.png")
aceptar = Icono([992,602], IconoAceptar))
icoHistory.add(aceptar)

IconoSiguiente = pg.image.load("./menu/IconoSiguiente.png")
siguiente = Icono([992,602], ))
icoHistory.add(siguiente)


dialogo1 = pg.image.load("./Historia/dialogo1.png")
dialogo2 = pg.image.load("./Historia/dialogo2.png")


def historia(ventana,estados,mouse,click,sonidos):
    ventana.fill(NEGRO)
    if estados["historia"]:
        if estados["dialogo1"]:
            ventana.blit(dialogo1, [0,0])
            if siguiente.rect.collidepoint(mouse):
                ventana.blit(IconoSiguiente,[992,602])
                if click[0] == 1:
                    sonidos.click()
                    estados["dialogo1"] = False
        elif estados["dialogo2"]:
            ventana.blit(dialogo2, [0,0])
            if aceptar.rect.collidepoint(mouse):
                ventana.blit(IconoSiguiente,[992,602])
                if click[0] == 1:
                    sonidos.click()
                    estados["dialogo2"] = False
        else:
            ventana.blit(dialogo3, [0,0])
            if aceptar.rect.collidepoint(mouse):
                ventana.blit(IconoAceptar,[992,602])
                if click[0] == 1:
                    sonidos.click()
                    estados["historia"] = False
                    estados.["nivel1"] = True