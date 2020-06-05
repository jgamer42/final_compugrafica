import utilidades
from globales import *
from bloque_base import Bloque_base
import json
import pygame
import sys
import os

sys.path.append(os.getcwd() + "/bloque/clases/")
sys.path.append(os.getcwd() + "/motor/")
ANCHO = 1000
ALTO = 1000


if __name__ == "__main__":
    archivo = "mapa/nivel1.json"
    archivo2 = "mapa/info_mapa1.json"
    # lectura de la sabana asociada al json
    dimension_imagen = None
    filas_imagen = None
    columnas_imagen = None
    archivo_sabana = None
    ancho_recorte = None
    alto_recorte = None
    with open(archivo2, "r") as file:
        diccionario = json.load(file)
        dimension_imagen = [diccionario["imageheight"], diccionario["imagewidth"]]
        filas_imagen = int(diccionario["tilecount"] / diccionario["columns"])
        columnas_imagen = diccionario["columns"]
        archivo_sabana = diccionario["image"]
        ancho_recorte = diccionario["tilewidth"]
        alto_recorte = diccionario["tileheight"]
    file.close()
    # NOTE esto se hace para tener la ruta relativa, toca agregar manualmente la carpeta
    archivo_sabana = os.getcwd() + "/mapa/" + archivo_sabana
    sprites = utilidades.crear_sprite(
        archivo_sabana, [ancho_recorte, alto_recorte], columnas_imagen, filas_imagen
    )
    print(sprites)
    print(len(sprites))
    # lectura del json del mapa
    matriz_mapa = None
    dimensiones_mapa = None
    with open(archivo, "r") as file:
        diccionario = json.load(file)
        matriz_mapa = diccionario["layers"][1]["data"]
        dimensiones_mapa = [diccionario["height"], diccionario["layers"][1]["width"]]
    file.close()
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO, ALTO])
    con = 0

    # ciclo para leer el mapa
    for i in range(dimensiones_mapa[0]):
        for j in range(dimensiones_mapa[1]):
            print(matriz_mapa[con], end="")
            if matriz_mapa[con] == 7:
                # obtiene el sprite de la lista de sprites
                sprite_cuadro = sprites[matriz_mapa[con] - 1]
                pos_x = ancho_recorte * j
                pos_y = alto_recorte * i
                pos = [pos_x, pos_y]
                bloque = Bloque_base(pos, sprite_cuadro)
                bloques.add(bloque)
            con += 1
        print("\n")

    en_juego = True
    while en_juego:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                en_juego = False
        ventana.fill([0, 0, 0])
        bloques.draw(ventana)
        pygame.display.flip()
