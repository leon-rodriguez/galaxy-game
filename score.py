import pygame as pg
from constantes import ANCHO_VENTANA


class Score:

    def __init__(self, fuente) -> None:
        self.puntuacion = 0
        self.puntuacion_x_segundo = 10
        self.puntuacion_x_enemigo = 50
        self.texto = "Score: {0}".format(self.puntuacion)
        self.texto_a_devolver = fuente.render(
            self.texto, True, (255, 255, 255))

    def sumar_bonus_tiempo(self):
        self.puntuacion = self.puntuacion + self.puntuacion_x_segundo

    def sumar_bonus_enemigo(self):
        self.puntuacion = self.puntuacion + self.puntuacion_x_enemigo

    def actualizar_texto(self, fuente):
        self.texto = "Score: {0}".format(self.puntuacion)
        self.texto_a_devolver = fuente.render(
            self.texto, True, (255, 255, 255))

    def dibujar_texto(self, pantalla):
        pantalla.blit(self.texto_a_devolver,
                      ((ANCHO_VENTANA / 2) - (self.texto_a_devolver.get_width() / 2), 10))

    def resetear_score(self, fuente):
        self.puntuacion = 0
        self.puntuacion_x_segundo = 10
        self.puntuacion_x_enemigo = 50
        self.texto = "Score: {0}".format(self.puntuacion)
        self.texto_a_devolver = fuente.render(
            self.texto, True, (255, 255, 255))
