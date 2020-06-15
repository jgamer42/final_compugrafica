import menu.menu as menu
import motor.ambiente as amb
import motor.globales as globales
import motor.utilidades as util
import pygame as pg
from jugador.clases.jugador import Jugador
from motor.constantes import *
import motor.mapeo as mapa
from sonidos.sonidos import *

pg.init()

jugadores = pg.sprite.Group()
enemigos = pg.sprite.Group()
bloques = pg.sprite.Group()
bonus = pg.sprite.Group()

reloj = pg.time.Clock()
estados = {"jugando": True, "inicio": True, "nivel1": False, "nivel2": False, "creditos": False, "opciones": False, "historia": False,"opciones": False, "creditos": False}
game_over = False

grupoSprite = {"bloques":bloques,"bonos":bonus,"enemigos":enemigos}

if __name__ == "__main__":
    mapa.leer_mapa("mapa/mapaA1.json",grupoSprite)
    ventana = pg.display.set_mode([ANCHO,ALTO])
    icono_juego = pg.image.load('CapuchoMAN.png')
    pg.display.set_icon(icono_juego)
    pg.display.set_caption("CapuchoMAN")

    sonidos = Mezclador()
    while estados["jugando"]:

        while estados["inicio"] and estados["jugando"]:
            for evento in pg.event.get():
                #PARAMETRIZAR ESTO EN UNA FUNCION
                if evento.type == pg.QUIT:
                    estados["jugando"] = False
                    estados["inicio"] = False
                else:
                    sonidos.update(estados)
                    #ES MEJOR CREAR EL MENU COMO OBJETO Y NO COMO ESTATICO
                    estados["jugando"] = menu.inicio(ventana,estados,pg.mouse.get_pos(),pg.mouse.get_pressed(),sonidos,evento)
        #PARAMETRIZAR ESTO EN UN CONSTRUCTOR O UNA FUNCION
        jugador = Jugador([128 + 1,ALTO-128 - 1])
        jugadores.add(jugador)
        while estados["nivel1"] and estados["jugando"]:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    estados["jugando"] = False
                    estados["nivel1"] = False
                jugador.controles(pg.key.get_pressed())
            jugador.bloques = bloques
            elementos_dibujar = [jugadores,bloques,enemigos,bonus]
            amb.ciclo_juego(ventana,elementos_dibujar)
            sonidos.update(estados)
            game_over = jugador.game_over
            #ESTO NO PUEDE IR AHI :C
            if game_over:
                estados["nivel1"] = False
                estados["inicio"] = True
                game_over = False
                jugadores.remove(jugador)
            reloj.tick(FPS)
    pg.quit()
