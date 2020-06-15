import os
import sys

sys.path.append(os.getcwd()+"/motor/")
sys.path.append(os.getcwd()+"/enemigos/clases/")
import utilidades as util
from enemigo_base import Enemigo_base
class Zombi(Enemigo_base):
    def __init__(self,pos):
        super().__init__(pos)
        self.animacion = util.crear_sprite("./enemigos/sprites/policia_zombie.png",[128,128],9)
        self.frame = 0
        self.image = self.animacion[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.direccion = 1
        self.velx = 0
        self.tipo = "zombie"
    def update(self):
        super().update()

    def animar(self):
        self.frame = util.animar(self.frame,9,self.direccion)
        self.image = self.animacion[self.frame]
