import os
import sys
sys.path.append(os.getcwd() + "/motor/")
import pygame as pg
from motor.constantes import *
from motor.utilidades import *





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
FondCreditos = pg.image.load("./menu/creditos.png")

IconoAceptar = pg.image.load("./menu/IconoAceptar.png")
aceptar = Icono([992,602], IconoAceptar)
iconos.add(aceptar)

IconoSonidoON = pg.image.load("./menu/iconoSonidoON.png")
IconoSonidoOFF = pg.image.load("./menu/iconoSonidoOFF.png")
sonido = Icono([506,559], IconoSonidoOFF)
iconos.add(sonido)


def inicio(ventana,estados,mouse,click,sonidos):
    if estados["opciones"]:
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
                estados["opciones"] = False
            else:
                ventana.blit(IconoAceptar,[992,602])
        elif sonido.rect.collidepoint(mouse):
            if sonidos.getMudo():
                if click[0] == 1:
                    #ventana.blit(IconoSonidoON,[506,559])
                    sonidos.click()
                    sonidos.mudo()
                else:
                    ventana.blit(IconoSonidoON,[506,559])
            else:
                if click[0] == 1:
                    #ventana.blit(IconoSonidoOFF,[506,559])
                    sonidos.click()
                    sonidos.mudo()
                else:
                    ventana.blit(IconoSonidoOFF,[506,559])
    elif estados["creditos"]:
        ventana.fill(NEGRO)
        ventana.blit(FondCreditos,[0,0])
        if aceptar.rect.collidepoint(mouse):
            ventana.blit(IconoAceptar,[992,602])
            if click[0] == 1:
                sonidos.click()
                estados["creditos"] = False

    else:
        ventana.fill(NEGRO)
        ventana.blit(fondo,[0,0])
        if jugar.rect.collidepoint(mouse):
            ventana.blit(IconoJugar,[917,297])
            if click[0] == 1:
                sonidos.click()
                estados["inicio"] = False
                estados["nivel1"] = True

        elif opciones.rect.collidepoint(mouse):
            ventana.blit(IconoOpciones,[917,389])
            if click[0] == 1:
                sonidos.click()
                estados["opciones"] = True
        elif creditos.rect.collidepoint(mouse):
            ventana.blit(IconoCreditos,[917,482])
            if click[0] == 1:
                sonidos.click()
                estados["creditos"] = True
        elif salir.rect.collidepoint(mouse):
            ventana.blit(IconoSalir,[917,575])
            if click[0] == 1:
                sonidos.click()
                estados["inicio"] = False
                return False
    pg.display.flip()
    return True

'''

    ventana.blit(history, [20,38])
    ventana.blit(history2, [645,38])
    ventana.blit(history3, [20,38])

    '''
