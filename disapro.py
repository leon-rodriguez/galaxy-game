import pygame as pg
from constantes import MOVIMIENTO_PERSONAJE


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
