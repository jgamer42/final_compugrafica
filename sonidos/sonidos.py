import pygame as pg

pg.mixer.init()


'''
pygame.mixer.music.set_endevent( )
hacer que la música envíe un evento cuando la reproducción se detenga
set_endevent () -> Ninguno
set_endevent (type) -> None
Esto hace que pygame señale (por medio de la cola de eventos) cuando la música termina de reproducirse. El argumento determina el tipo de evento que se pondrá en cola.

El evento se pondrá en cola cada vez que termine la música, no solo la primera vez. Para evitar que el evento se ponga en cola, llame a este método sin argumento.
'''


class Mezclador():
    def __init__(self):
        self.playList = [pg.mixer.music.load("./sonidos/rock1.ogg"),
                        pg.mixer.music.load("./sonidos/rock2.ogg"),
                        pg.mixer.music.load("./sonidos/rock3.ogg")]
        self.musicMenu = pg.mixer.Sound("./sonidos/menu.ogg")
        self.sonidoClick = pg.mixer.Sound('./sonidos/Click.ogg')
        self.flagMenu = True
        self.flagMudo = False
        self.conPlayList = -1

    def update(self,estados):
        self.menu(estados)
        self.musica(estados)

    def menu(self,estados):
        if self.flagMudo:
            self.musicMenu.stop()
            self.flagMenu = True
        elif estados["inicio"] and not self.flagMudo and self.flagMenu:
            self.musicMenu.play(-1)
            self.flagMenu = False
        elif not estados["inicio"]:# and not self.flagMenu:
            self.musicMenu.stop()
            self.flagMenu = True

    def click(self):
        self.sonidoClick.play()

    def musica(self,estados):
        if estados["nivel1"] or estados["nivel2"]:
            if not self.flagMudo:
                if pg.mixer.music.get_busy() == 0: #1 es sonando y 0 es sin sonido
                    self.playList[self.nextSong()]
                    pg.mixer.music.play()
        elif estados["inicio"]:
            pg.mixer.music.stop()

    def nextSong(self):
        if self.conPlayList < 3:
            self.conPlayList += 1
        else:
            self.conPlayList = 0
        return self.conPlayList

    def mudo(self):
        if not self.flagMudo:
            self.flagMudo = True
            print("apagado")
        else:
            self.flagMudo = False
            print("encendido")

    def getMudo(self):
        return self.flagMudo
