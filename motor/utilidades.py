import pygame


def crear_sprite(dir_sabana, dimensiones, cuadros, filas=1, opcion=None):
    """
    Funcion para recorte de sprites
    sabana: imagen con los graficos
    size: lista con ancho y alto [ancho,alto]
    frames: cantidad de columnas que tiene la sabana
    filas: filas de lasabana (default 1)
    opcion: optiene una matriz con el parametro "matriz" (default None)
    """

    sabana = pygame.image.load(dir_sabana)

    ancho_cuadros = dimensiones[0]
    alto_cuadros = dimensiones[1]
    animacion = []
    # Recorta como fila
    if filas == 1:
        for cuadro in range(cuadros):
            cuadro = sabana.subsurface(
                ancho_cuadros * cuadro, 0, ancho_cuadros, alto_cuadros
            )
            animacion.append(cuadro)
    # recorta como matricez
    elif filas > 1 and opcion == "matriz":
        for f in range(filas):
            fila = []
            for cuadro in range(cuadros):
                cuadro = sabana.subsurface(
                    ancho_cuadros * cuadro,
                    alto_cuadros * f,
                    ancho_cuadros,
                    alto_cuadros,
                )
                fila.append(cuadro)
            animacion.append(fila)
    # recorta una sabana matriz como una fila
    elif filas > 1 and opcion == None:
        for fila in range(filas):
            for cuadro in range(cuadros):
                cuadro = sabana.subsurface(
                    ancho_cuadros * cuadro,
                    alto_cuadros * fila,
                    ancho_cuadros,
                    alto_cuadros,
                )
                animacion.append(cuadro)
    return animacion


def animar(frame_actual, numero_frames):
    if frame_actual < (numero_frames - 1):
        frame_actual += 1
    else:
        frame_actual = 0
    return frame_actual
