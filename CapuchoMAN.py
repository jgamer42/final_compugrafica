# importante leer, son las reglas de desarollo
# - para este progama se usara snake case (esto_es_un_ejemplo) para la notacion de variables
# - nombres de variables y archivos en español
# - el de tema de los parentesis y espacios esta automatizado, cuando hacen el push el los acomoda
# - a la hora de crear nuevas clase nombrar el archivo en minisculas y la clase con la primera en mayuscula
# - mantener coherencia entre plural y singular
# - tratar de no subir word, psd, fsd, o cualquier extension o archivo compilado
import pygame

from motor.constantes import *
from motor.globales import *
import motor.ambiente as amb
import motor.utilidades as util
from bloque.clases.bloque_base import Bloque_base
from jugador.clases.jugador import Jugador
from enemigos.clases.enemigo_base import Enemigo_base
from enemigos.clases.observador import Observador

jugador = Jugador([151,0])
jugadores.add(jugador)
enemigo = Enemigo_base([500,500])
enemigos.add(enemigo)
alarma = Observador(enemigo)

if __name__ == "__main__":
    pygame.init()
    util.leer_mapa("mapa/mapaA1.json",bloques)
    ventana = pygame.display.set_mode([ANCHO,ALTO])

    while en_juego:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                en_juego = False
            jugador.controles(evento)
        lista_colision = pygame.sprite.spritecollide(jugador,bloques, False)
        elementos_dibujar = [bloques,enemigos,jugadores]
        amb.control_colision(lista_colision, jugador)
        amb.ciclo_juego(ventana, elementos_dibujar)
