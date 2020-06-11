# importante leer, son las reglas de desarollo
# - para este progama se usara snake case (esto_es_un_ejemplo) para la notacion de variables
# - nombres de variables y archivos en español
# - el de tema de los parentesis y espacios esta automatizado, cuando hacen el push el los acomoda
# - a la hora de crear nuevas clase nombrar el archivo en minisculas y la clase con la primera en mayuscula
# - mantener coherencia entre plural y singular
# - tratar de no subir word, psd, fsd, o cualquier extension o archivo compilado

import menu.menu as menu
import motor.ambiente as amb
import motor.globales as globales
import motor.utilidades as util
import pygame as pg
from bloque.clases.bloque_base import Bloque_base
from enemigos.clases.enemigo_base import Enemigo_base
#from enemigos.clases.observador import Observador
from jugador.clases.jugador import Jugador
from motor.constantes import *

jugadores = pg.sprite.Group()
enemigos = pg.sprite.Group()
bloques = pg.sprite.Group()



jugador = Jugador([128 + 1,ALTO-128 - 1])
jugadores.add(jugador)
enemigo = Enemigo_base([500,500])
enemigos.add(enemigo)

#alarma = Observador(enemigo)
reloj = pg.time.Clock()
jugar = True
niveles = {"inicio": True, "nivel1": False, "nivel2": False, "creditos": False, "opciones": False}
opInicio = {"opciones": False, "creditos": False}
game_over = False
if __name__ == "__main__":
    pg.init()
    util.leer_mapa("mapa/mapaA1.json",bloques)
    ventana = pg.display.set_mode([ANCHO,ALTO])
    icono_juego = pg.image.load('CapuchoMAN.png')
    pg.display.set_icon(icono_juego)
    pg.display.set_caption("CapuchoMAN")

    while jugar:
        while niveles["inicio"] and jugar:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    jugar = False
                    niveles["inicio"] = False
                else:
                    jugar = menu.menu_inicio(ventana,opInicio,niveles,pg.mouse.get_pos(),pg.mouse.get_pressed())

        while  niveles["nivel1"] and jugar:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    jugar = False
                jugador.controles(pg.key.get_pressed())
            jugador.bloques = bloques
            elementos_dibujar = [jugadores,bloques,enemigos]
            amb.ciclo_juego(ventana,elementos_dibujar)
            reloj.tick(30)
    pg.quit()
