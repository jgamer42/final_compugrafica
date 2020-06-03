import pygame


def crear_sprite(sabana, size, frames, filas=1, opcion=None):
    """
    Funcion para recorte de sprites
    sabana: imagen con los graficos
    size: lista con ancho y alto [ancho,alto]
    frames: cantidad de columnas que tiene la sabana
    filas: filas de lasabana (default 1)
    opcion: optiene una matriz con el parametro "matriz" (default None)
    """
    animacion = []
    if filas == 1:
        for c in range(frames):
            cuadro = sabana.subsurface(size[0] * c, 0, size[0], size[1])
            animacion.append(cuadro)
    elif filas > 1 and opcion == "matriz":
        for f in range(filas):
            fila = []
            for c in range(frames):
                cuadro = sabana.subsurface(size[0] * c, size[1] * f, size[0],
                                           size[1])
                fila.append(cuadro)
            animacion.append(fila)
    elif filas > 1 and opcion == None:
        for f in range(filas):
            for c in range(frames):
                cuadro = sabana.subsurface(size[0] * c, size[1] * f, size[0],
                                           size[1])
                animacion.append(cuadro)
    return animacion


def next_frame(frame_actual, numero_frames):
    if frame_actual < (numero_frames - 1):
        frame_actual += 1
    else:
        frame_actual = 0
    return frame_actual
