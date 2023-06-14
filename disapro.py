import pygame as pg
from constantes import MOVIMIENTO_PERSONAJE


# def getSuperficie(path, filas, columnas):
#     lista = []
#     superficie_imagen = pg.image.load(path)
#     fotograma_ancho = int(superficie_imagen.get_width() / columnas)
#     fotograma_alto = int(superficie_imagen.get_height() / filas)

#     for fila in range(filas):
#         for columna in range(columnas):
#             x = columna * fotograma_ancho
#             y = fila * fotograma_alto
#             # un pedazo del sprite
#             superficie_fotograma = superficie_imagen.subsurface(
#                 x, y, fotograma_ancho, fotograma_alto)
#             lista.append(superficie_fotograma)
#     return lista


class Disparo:
    def __init__(self, x_inicial, y_inicial, disparo_enemigo, imagen_recibida) -> None:
        self.velocidad = 1
        self.x = x_inicial
        self.y = y_inicial
        self.imagen = imagen_recibida
        self.visible = True
        self.rect = pg.Rect(
            self.x, self.y, imagen_recibida.get_width(), imagen_recibida.get_height())
        self.es_enemigo = disparo_enemigo

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, [self.x, self.y])

    def mover(self):
        if self.es_enemigo == True:
            self.x = self.x - MOVIMIENTO_PERSONAJE * self.velocidad
            self.rect.x = self.x
        else:
            self.x = self.x + MOVIMIENTO_PERSONAJE * self.velocidad
            self.rect.x = self.x

    def checkear_visibilidad(self, ancho_ventana):
        if self.x > ancho_ventana or self.x < 0:
            return False


class DisparoAmigo(Disparo):
    pass
