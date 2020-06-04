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
