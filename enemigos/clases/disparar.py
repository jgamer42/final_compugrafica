import os
import sys

import ambiente
import pygame as pg
from balas.bala_base import Bala_base
from observador_base import Observador_base

sys.path.append(os.getcwd()+"/motor/")
sys.path.append(os.getcwd()+"/enemigos/clases/")

class Disparar(Observador_base):
    def __init__(self,sujeto,tiempo):
        super().__init__(sujeto,tiempo)
    
    def informar(self):
        super().informar()
    
    def comportamiento(self):
        bala = Bala_base(self.observado.rect.center,self.observado.direccion)
        cosa=["hola","bola"]
        ambiente.agregar_bala(cosa,"enemigo")
        print(ambiente.balas_enemigos)
