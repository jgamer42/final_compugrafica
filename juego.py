# importante leer, son las reglas de desarollo
# - para este progama se usara snake case (esto_es_un_ejemplo) para la notacion de variables
# - nombres de variables y archivos en español
# - el de tema de los parentesis y espacios esta automatizado, cuando hacen el push el los acomoda
# - a la hora de crear nuevas clase nombrar el archivo en minisculas y la clase con la primera en mayuscula
# - mantener coherencia entre plural y singular
# - tratar de no subir word, psd, fsd, o cualquier extension o archivo compilado
import pygame

from ambiente.constantes import *
from ambiente.globales import *
from bloque.clases import bloque_base
from enemigos.clases import enemigo_base
from jugador.clases.jugador import Jugador

en_juego = True
jugador = Jugador([0, 0])
jugadores.add(jugador)
if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO, ALTO])
    while en_juego:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                en_juego = False
        jugadores.update()
        ventana.fill(NEGRO)
        jugadores.draw(ventana)
        pygame.display.flip()
