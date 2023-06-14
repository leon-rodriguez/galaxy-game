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


# naves = getSuperficie("galaxian/images/sprites.png", 12, 2)
# principal = pg.transform.rotate(naves[2], -90)
# disparo_principal = pg.transform.rotate(naves[3], -90)

# print(principal.get_width())

nave_personaje_principal = pg.image.load(
    "galaxian/images/personaje_principal.png")
nave_personaje_principal = pg.transform.rotate(nave_personaje_principal, -90)

disparo_personaje_principal = pg.image.load(
    "galaxian/images/disparo_personaje_principal.png")
# naves = getSuperficie("galaxian/images/sprites.png", 12, 2)
disparo_personaje_principal = pg.transform.rotate(
    disparo_personaje_principal, -90)


class Personaje:
    def __init__(self) -> None:
        self.vida = 100
        self.daño = 10
        self.velocidad = 1
        self.velocidadTiro = 500
        self.imagen = nave_personaje_principal
        self.imagen_disparo = disparo_personaje_principal
        self.x = 0
        self.y = 0
        self.rect = pg.Rect(
            self.x, self.y, nave_personaje_principal.get_width(), nave_personaje_principal.get_height())

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, [self.x, self.y])

    def moverAriiba(self):
        if self.y > 0:
            self.y = self.y - MOVIMIENTO_PERSONAJE * self.velocidad
            self.rect.y = self.y

    def moverAbajo(self, largo_ventana):
        if self.y + self.imagen.get_height() < largo_ventana:
            self.y = self.y + MOVIMIENTO_PERSONAJE * self.velocidad
            self.rect.y = self.y
    # def disparar():
