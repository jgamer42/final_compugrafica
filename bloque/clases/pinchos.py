from bloque_base import Bloque_base


class Pinchos(Bloque_base):
    def __init__(self,pos,img=None):
        super().__init__(pos,img)
        self.tipo = "pinchos"
        self.daño = 130
