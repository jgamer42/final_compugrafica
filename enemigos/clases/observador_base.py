import os
import sys

import constantes

sys.path.append(os.getcwd()+"/motor/")
class Observador_base():
    def __init__(self,sujeto,tiempo_disparo):
        self.alarma = tiempo_disparo
        self.con = 0
        self.seg = 0
        self.bandera = 1
        self.observado = sujeto.agregar_observador(self)

    def informar(self):
        self.seg = self.con // constantes.FPS
        if self.seg % self.alarma == 0 and self.bandera == 1:
            self.comportamiento()
        #controla que solo se dispare una vez por segundo 
        if self.bandera != constantes.FPS:
            self.bandera += 1
        else:
            self.bandera = 1
        self.con += 1
        
    def comportamiento(self):
        pass
