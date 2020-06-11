import json
import os
import sys
from xml.dom import minidom
sys.path.append(os.getcwd() + "/bloque/clases/")
sys.path.append(os.getcwd() + "/motor/")
import pygame
from bloque_base import Bloque_base
from constantes import *


def crear_sprite(dir_sabana, dimensiones, columnas, filas=1, opcion=None):
    """
    Funcion para recorte de sprites
    sabana: imagen con los graficos
    dimensiones: lista con ancho y alto [ancho,alto] del recorte
    columnas: cantidad de columnas que tiene la sabana
    filas: filas de la sabana (default 1)
    opcion: optiene una matriz con el parametro "matriz" (default None)
    """
    sabana = pygame.image.load(dir_sabana)
    ancho_cuadros = dimensiones[0]
    alto_cuadros = dimensiones[1]
    animacion = []
    # Recorta como fila
    if filas == 1:
        for cuadro in range(columnas):
            cuadro = sabana.subsurface(ancho_cuadros * cuadro, 0, ancho_cuadros, alto_cuadros)
            animacion.append(cuadro)
    # recorta como matricez
    elif filas > 1 and opcion == "matriz":
        for f in range(filas):
            fila = []
            for cuadro in range(columnas):
                cuadro = sabana.subsurface(ancho_cuadros * cuadro,alto_cuadros * f,ancho_cuadros,alto_cuadros)
                fila.append(cuadro)
            animacion.append(fila)
    # recorta una sabana matriz como una fila
    elif filas > 1 and opcion == None:
        for fila in range(filas):
            for cuadro in range(columnas):
                cuadro = sabana.subsurface(ancho_cuadros * cuadro,alto_cuadros * fila,ancho_cuadros,alto_cuadros)
                animacion.append(cuadro)
    return animacion

def animar(frame_actual, numero_frames,direccion):
    if direccion == 0:
        return frame_actual
    elif direccion == 1:
        if frame_actual < (numero_frames - 1):
            frame_actual += 1
        else:
            frame_actual = 0
        return frame_actual
    elif direccion == -1:
        if frame_actual > 0:
            frame_actual -= 1
        else:
            frame_actual = (numero_frames - 1)
        return frame_actual

def leer_mapa(dir_mapa,receptor):
    matriz_mapa = None
    dimensiones_mapa = None
    info_imagen = None
    ancho_recorte = None
    alto_recorte = None
    with open(dir_mapa, "r") as file:
        diccionario = json.load(file)
        matriz_mapa = diccionario["layers"][0]["data"]
        dimensiones_mapa = [diccionario["height"], diccionario["layers"][0]["width"]]
        info_imagen = diccionario["tilesets"][0]["source"]
        ancho_recorte = diccionario["tileheight"]
        alto_recorte = diccionario["tilewidth"]
    file.close()
    sprites = leer_config_imagen(info_imagen)
    cargar_mapa(matriz_mapa,dimensiones_mapa,ancho_recorte,alto_recorte,sprites,receptor)

def leer_config_imagen(dir_xml):
    dir_xml = "./mapa/"+dir_xml
    archivo = minidom.parse(dir_xml)
    info_mapa = archivo.getElementsByTagName("tileset")
    filas_imagen = int(int(info_mapa[0].attributes["tilecount"].value)/int(info_mapa[0].attributes["columns"].value))
    columnas_imagen = int(info_mapa[0].attributes["columns"].value)
    ancho_recorte = int(info_mapa[0].attributes["tilewidth"].value)
    alto_recorte = int(info_mapa[0].attributes["tileheight"].value)
    info_imagen = archivo.getElementsByTagName("image")
    archivo_sabana = info_imagen[0].attributes["source"].value
    archivo_sabana = "./mapa/" + archivo_sabana
    sprites = crear_sprite(archivo_sabana,[ancho_recorte,alto_recorte],columnas_imagen,filas_imagen)
    return(sprites)

def cargar_mapa(matriz_mapa,dimensiones_mapa,ancho_recorte,alto_recorte,sprites,receptor):
    con = 0
    for i in range(dimensiones_mapa[0]):
        for j in range(dimensiones_mapa[1]):
            if matriz_mapa[con] != 0:
                # obtiene el sprite de la lista de sprites
                sprite_cuadro = sprites[matriz_mapa[con] - 1]
                pos_x = ancho_recorte * j
                pos_y = alto_recorte * i
                pos = [pos_x, pos_y]
                bloque = Bloque_base(pos, sprite_cuadro)
                receptor.add(bloque)
            con += 1


def tiposBloques():
    pass
