import os
import sys

from disparar import Disparar
from esmad import Esmad
from observador_base import Observador_base

sys.path.append(os.getcwd()+"/enemigos/clases/")
sys.path.append(os.getcwd()+"/motor/")



class Fabrica():
    def __init__(self):
        print("fabrica lista")

    def crear_enemigo(self,codigo_enemigo,receptor,pos):
        if codigo_enemigo == 1:
            self.crear_esmad(receptor,pos)

    def crear_esmad(self,receptor,pos):
        enemigo = Esmad(pos)
        comportamiento1 = Observador_base(enemigo,5)
        comportamiento2 = Disparar(enemigo,10)
        receptor.add(enemigo)
