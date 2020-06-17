import os
import sys

from disparar import Disparar
from esmad import Esmad
from observador_base import Observador_base
from perro import Perro
from zombi import Zombi

sys.path.append(os.getcwd()+"/enemigos/clases/")
sys.path.append(os.getcwd()+"/motor/")
class Fabrica():
    def __init__(self):
        print("fabrica lista")

    def crear_enemigo(self,codigo_enemigo,pos):
        if codigo_enemigo == 11:
            #enemigo = self.crear_tanqueta(pos)
            enemigo = self.crear_esmad(pos)
        elif codigo_enemigo == 14:
            enemigo = self.crear_policia_zombi(pos)
        elif codigo_enemigo == 22:
            enemigo = self.crear_esmad(pos)
        elif codigo_enemigo == 23:
            enemigo = self.crear_perro(pos)
        return enemigo
    def crear_esmad(self,pos):
        x = pos[0]
        y = pos[1]- 64
        enemigo = Esmad([x,y])
        comportamiento1 = Observador_base(enemigo,5)
        comportamiento2 = Disparar(enemigo,2)  
        return enemigo

    def crear_policia_zombi(self,pos):
        x = pos[0]
        y = pos[1]- 64
        enemigo = Zombi([x,y])
        return enemigo

    def crear_tanqueta(self,pos):
        enemigo = Esmad(pos)
        comportamiento1 = Observador_base(enemigo,5)
        comportamiento2 = Disparar(enemigo,10)
        return enemigo

    def crear_perro(self,pos):
        x = pos[0]
        y = pos[1]- 64
        enemigo = Perro([x,y])
        return enemigo
