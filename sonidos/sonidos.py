import pygame as pg

pg.mixer.init()

class Mezclador():
    def __init__(self):
        self.playList = [pg.mixer.music.load("./sonidos/rock1.ogg"),
                        pg.mixer.music.load("./sonidos/rock2.ogg"),
                        pg.mixer.music.load("./sonidos/rock3.ogg")]
        self.musicMenu = pg.mixer.Sound("./sonidos/menu.ogg")
        self.sonidoClick = pg.mixer.Sound('./sonidos/Click.ogg')
        self.grunt = pg.mixer.Sound('./sonidos/grunt.ogg')
        self.flagMenu = True
        self.flagMudo = False
        self.conPlayList = 0

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

    def grunt(self):
        self.grunt.play()

    def musica(self,estados):
        if estados["nivel1"] or estados["nivel2"]:
            if not self.flagMudo:
                if pg.mixer.music.get_busy() == 0: #1 es sonando y 0 es sin sonido
                    self.playList[self.nextSong()]
                    pg.mixer.music.play()
        elif estados["inicio"]:
            pg.mixer.music.stop()

    def nextSong(self):
        if self.conPlayList < len(self.playList):
            self.conPlayList += 1
        else:
            self.conPlayList = 0
        return (self.conPlayList - 1)

    def mudo(self):
        if not self.flagMudo:
            self.flagMudo = True
            print("apagado")
        else:
            self.flagMudo = False
            print("encendido")

    def getMudo(self):
        return self.flagMudo
