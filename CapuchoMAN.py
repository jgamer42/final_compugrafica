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

pg.init()
pg.mixer.init()

musicMenu = pg.mixer.Sound("./sonidos/menu.ogg")

musicJuego = pg.mixer.music.load("./sonidos/rock1.ogg")
pg.mixer.music.queue("./sonidos/rock2.ogg")
pg.mixer.music.queue("./sonidos/rock3.ogg")

pg.mixer.music.play()

jugadores = pg.sprite.Group()
enemigos = pg.sprite.Group()
bloques = pg.sprite.Group()


'''
pygame.mixer.music.set_endevent( )
hacer que la música envíe un evento cuando la reproducción se detenga
set_endevent () -> Ninguno
set_endevent (type) -> None
Esto hace que pygame señale (por medio de la cola de eventos) cuando la música termina de reproducirse. El argumento determina el tipo de evento que se pondrá en cola.

El evento se pondrá en cola cada vez que termine la música, no solo la primera vez. Para evitar que el evento se ponga en cola, llame a este método sin argumento.
'''




#jugador = Jugador([128 + 1,ALTO-128 - 1])
#jugadores.add(jugador)
enemigo = Enemigo_base([500,500])
enemigos.add(enemigo)

#alarma = Observador(enemigo)
reloj = pg.time.Clock()
jugar = True
niveles = {"inicio": True, "nivel1": False, "nivel2": False, "creditos": False, "opciones": False}
opInicio = {"opciones": False, "creditos": False}
game_over = False

if __name__ == "__main__":
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

        jugador = Jugador([128 + 1,ALTO-128 - 1])
        jugadores.add(jugador)
        while  niveles["nivel1"] and jugar:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    jugar = False
                jugador.controles(pg.key.get_pressed())
            jugador.bloques = bloques
            elementos_dibujar = [jugadores,bloques,enemigos]
            amb.ciclo_juego(ventana,elementos_dibujar)

            game_over = jugador.game_over
            if game_over:
                niveles["nivel1"] = False
                niveles["inicio"] = True
                game_over = False
                jugadores.remove(jugador)


            reloj.tick(30)
    pg.quit()
