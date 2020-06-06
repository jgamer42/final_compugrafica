import pygame

# aqui se van a poner todas las variables que necesitan ser
# accesibles desde cualquier elemento del programa

# SPRITE GROUPS
jugadores = pygame.sprite.Group()
enemigos = pygame.sprite.Group()
bloques = pygame.sprite.Group()
# CICLO DE JUEGO
en_juego = True
reloj = pygame.time.Clock()
niveles = {"inicio": True, "nivel1": True, "nivel2": True, "creditos": True}

# configuracion ambiente
velx_entorno = 0
vely_entorno = 0
x_fondo = 0
y_fondo = 0

#fondos niveles
fondos_mapas = {"mapaA1":pygame.image.load("mapa/mapaA1.png")}
