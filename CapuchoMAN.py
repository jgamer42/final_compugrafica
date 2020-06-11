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
import pygame
from bloque.clases.bloque_base import Bloque_base
from enemigos.clases.enemigo_base import Enemigo_base
from enemigos.clases.observador import Observador
from jugador.clases.jugador import Jugador
from motor.constantes import *

jugador = Jugador([128 + 1,ALTO-128 - 1])
globales.jugadores.add(jugador)
enemigo = Enemigo_base([500,500])
globales.enemigos.add(enemigo)
alarma = Observador(enemigo)

if __name__ == "__main__":
    pygame.init()
    util.leer_mapa("mapa/mapaA1.json",globales.bloques)
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    icono_juego = pygame.image.load('CapuchoMAN.png')
    pygame.display.set_icon(icono_juego)
    pygame.display.set_caption("CapuchoMAN")

    while globales.en_juego:
        while globales.niveles["inicio"] and globales.en_juego:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    globales.en_juego = False
                globales.en_juego = menu.menu_inicio(ventana,globales.niveles)

        while  globales.niveles["nivel1"] and globales.en_juego:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    globales.en_juego = False
                jugador.controles()
            lista_colision = pygame.sprite.spritecollide(jugador,globales.bloques,False)
            jugador.lista_colision = lista_colision
            jugador.lista_bloques = globales.bloques
            elementos_dibujar = [globales.jugadores,globales.bloques,globales.enemigos]
            amb.ciclo_juego(ventana,elementos_dibujar)

    pygame.quit()
