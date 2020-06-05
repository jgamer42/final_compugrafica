class Observador:
    def __init__(self,sujeto):
        self.observado = sujeto.agregar_observador(self)
    
    def informar(self):
        print("notificado")