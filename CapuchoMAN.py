import menu.menu as menu
import motor.ambiente as amb
import motor.globales as globales
import motor.mapeo as mapa
import motor.utilidades as util
import pygame as pg
from gui.gui import *
from jugador.clases.jugador import Jugador
from motor.constantes import *
from sonidos.sonidos import *
from gui.gui import *

pg.init()

jugadores = pg.sprite.Group()
enemigos = pg.sprite.Group()
bloques = pg.sprite.Group()
bonus = pg.sprite.Group()

reloj = pg.time.Clock()
estados = {"jugando": True, "inicio": True, "nivel1": False, "nivel2": False, "creditos": False, "opciones": False, "historia": False,"opciones": False, "creditos": False}
gameOver = False

grupoSprite = {"bloques":bloques,"bonos":bonus,"enemigos":enemigos}

if __name__ == "__main__":
    mapa.leer_mapa("mapa/mapaA1.json",grupoSprite)
    ventana = pg.display.set_mode([ANCHO,ALTO])
    icono_juego = pg.image.load('CapuchoMAN.png')
    pg.display.set_icon(icono_juego)
    pg.display.set_caption("CapuchoMAN")

    jugador = Jugador([128 + 1,ALTO-128 - 1],bloques,bonus)
    jugadores.add(jugador)
    gui = GUI(jugador,ventana)

    sonidos = Mezclador()


    while estados["jugando"]:

        while estados["inicio"] and estados["jugando"]:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    estados["jugando"] = False
                    estados["inicio"] = False
                else:
                    sonidos.update(estados)
                    estados["jugando"] = menu.inicio(ventana,estados,pg.mouse.get_pos(),pg.mouse.get_pressed(),sonidos)

        while estados["nivel1"] and estados["jugando"]:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    estados["jugando"] = False
                    estados["nivel1"] = False
                jugador.controles(pg.key.get_pressed())
            elementos_dibujar = [jugadores,bloques,enemigos,bonus]
            amb.ciclo_juego(ventana,elementos_dibujar,gui)
            jugador.checkGameOver(gameOver,estados)
            gui.checkEstado(gameOver)
            sonidos.update(estados)
            reloj.tick(FPS)

    print(globales.vely_entorno)
    print(globales.x_fondo)

    pg.quit()
