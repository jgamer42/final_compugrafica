from bloque_base import Bloque_base


class Lava(Bloque_base):
    def __init__(self,pos,img=None):
        super().__init__(pos,img)
        self.tipo = "lava"
        self.daño = 250
