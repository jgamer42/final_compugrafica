import menu.menu as menu
import motor.ambiente as amb
import motor.globales as globales
import motor.utilidades as util
import pygame as pg
from enemigos.clases.esmad import Esmad
from enemigos.clases.observador_base import Observador_base
from jugador.clases.jugador import Jugador
from motor.constantes import *
from sonidos.sonidos import *

pg.init()

jugadores = pg.sprite.Group()
enemigos = pg.sprite.Group()
bloques = pg.sprite.Group()

jugador = Jugador([128 + 1,ALTO-128 - 1])
jugadores.add(jugador)
enemigo = Esmad([500,500])
o = Observador_base(enemigo,5)

enemigos.add(enemigo)


reloj = pg.time.Clock()
estados = {"jugando": True, "inicio": True, "nivel1": False, "nivel2": False, "creditos": False, "opciones": False}
opInicio = {"opciones": False, "creditos": False}
game_over = False

if __name__ == "__main__":
    util.leer_mapa("mapa/mapaA1.json",bloques)
    ventana = pg.display.set_mode([ANCHO,ALTO])
    icono_juego = pg.image.load('CapuchoMAN.png')
    pg.display.set_icon(icono_juego)
    pg.display.set_caption("CapuchoMAN")

    sonidos = Mezclador()

    while estados["jugando"]:
        while estados["inicio"] and estados["jugando"]:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    estados["jugando"] = False
                    estados["inicio"] = False
                else:
                    sonidos.update(estados)
                    estados["jugando"] = menu.inicio(ventana,opInicio,estados,pg.mouse.get_pos(),pg.mouse.get_pressed(),sonidos)

        jugador = Jugador([128 + 1,ALTO-128 - 1])
        jugadores.add(jugador)
        while estados["nivel1"] and estados["jugando"]:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    estados["jugando"] = False
                    estados["nivel1"] = False
                jugador.controles(pg.key.get_pressed())
            jugador.bloques = bloques
            elementos_dibujar = [jugadores,bloques,enemigos]
            amb.ciclo_juego(ventana,elementos_dibujar)
            onidos.update(estados)
            game_over = jugador.game_over
            if game_over:
                niveles["nivel1"] = False
                niveles["inicio"] = True
                game_over = False
                jugadores.remove(jugador)
            reloj.tick(FPS)
    pg.quit()
