import json
import os
import sys
import pygame
from xml.dom import minidom

sys.path.append(os.getcwd() + "/bloque/clases/")
sys.path.append(os.getcwd()+ "/enemigos/clases/")
sys.path.append(os.getcwd() + "/bonus/")
sys.path.append(os.getcwd() + "/motor/")
from fabrica import Fabrica
from bloque_base import Bloque_base
from lava import Lava
from pinchos import Pinchos
from moneda import Moneda
import utilidades
from constantes import *

matriz_muros = [1,2,6,7,8,9,10,16,17,18,19,20,21,24,26,29,30,31,36,43]
matriz_enemigos = [11,14,22,23]
matriz_bonus = [13]
matriz_ambientales = [19,39]

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
    sprites = utilidades.crear_sprite(archivo_sabana,[ancho_recorte,alto_recorte],columnas_imagen,filas_imagen)
    return(sprites)

def cargar_mapa(matriz_mapa,dimensiones_mapa,ancho_recorte,alto_recorte,sprites,receptor):
    #print(len(sprites))
    con = 0
    for i in range(dimensiones_mapa[0]):
        for j in range(dimensiones_mapa[1]):
            if matriz_mapa[con] != 0:
                #print([matriz_mapa[con] - 1])# obtiene el sprite de la lista de sprites
                sprite_cuadro = sprites[matriz_mapa[con] - 1]
                pos_x = ancho_recorte * j
                pos_y = alto_recorte * i
                pos = [pos_x, pos_y]
                if matriz_mapa[con] in matriz_muros:
                    bloque = Bloque_base(pos, sprite_cuadro)
                    bloque.tipo = "muro"
                    receptor["bloques"].add(bloque)
                elif matriz_mapa[con] in matriz_bonus:
                    bono = Moneda(pos)
                    #bono.tipo = "bono"
                    receptor["bonos"].add(bono)
                
                elif matriz_mapa[con] in matriz_enemigos:
                    fabrica_enemigos = Fabrica()
                    codigo_enemigo = matriz_mapa[con]
                    enemigo = fabrica_enemigos.crear_enemigo(codigo_enemigo,pos)
                    receptor["enemigos"].add(enemigo)
                
                elif matriz_mapa[con] in matriz_ambientales:
                    
                    if matriz_mapa[con] == 39:
                        bloque = Pinchos(pos,sprite_cuadro)
                        receptor["bloques"].add(bloque)
                    elif matriz_mapa[con] == 19:
                        bloque = Lava(pos,sprite_cuadro)
                        receptor["bloques"].add(bloque)


                
            con += 1
