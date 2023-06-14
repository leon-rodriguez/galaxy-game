import pygame as pg
from constantes import MOVIMIENTO_PERSONAJE
import random
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
# imagen_primer_enemigo = naves[0]
# imagen_primer_enemigo_rect = pg.transform.scale(
# imagen_primer_enemigo, (100, 100))

nave_enemigo_basico = pg.image.load("galaxian/images/enemigo_basico.png")
nave_enemigo_basico = pg.transform.rotate(nave_enemigo_basico, 90)

disparo_enemigo_basico = pg.image.load(
    "galaxian/images/disparo_enemigo_basico.png")
disparo_enemigo_basico = pg.transform.rotate(disparo_enemigo_basico, 90)


class Enemigo:
    def __init__(self, x_inicial, y_inicial) -> None:
        self.vida = 50
        self.daño = 10
        self.velocidad = 1
        self.movimiento = 3
        self.velocidadTiro = 500
        self.imagen = nave_enemigo_basico
        self.imagen_disparo = disparo_enemigo_basico
        self.x = x_inicial
        self.y = y_inicial
        self.rect = pg.Rect(self.x + 20, self.y, nave_enemigo_basico.get_width(),
                            nave_enemigo_basico.get_height())
        self.moviendose = False
        self.coordenada_x_final = 0
        self.coordenada_y_final = 0

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, [self.x, self.y])

    def comprobar_colision(self, otro_rect, daño_personaje_principal) -> bool:
        if self.rect.colliderect(otro_rect):
            print("doblo y choclo")
            self.vida = self.vida - daño_personaje_principal
            return True

    def generar_coordenadas(self, largo_ventana, ancho_ventana):
        if self.moviendose == False:
            self.coordenada_x_final = random.randint(
                700, ancho_ventana - self.imagen.get_width())
            self.coordenada_y_final = random.randint(
                0, largo_ventana - self.imagen.get_height())
            self.moviendose = True
            # print("cordenada x", self.coordenada_x_final)
            # print("cordenada y", self.coordenada_y_final)

    def mover(self):
        # if self.y > 0 and self.y + self.imagen.get_height() < largo_ventana and self.x + self.imagen.get_height() < ancho_ventana:
        # coordenada_x_final = random.randint(800, ancho_ventana)
        # coordenada_y_final = random.randint(0, largo_ventana)
        if self.moviendose == True:
            # print("moviendose")
            if self.x > self.coordenada_x_final:
                self.x = self.x - self.movimiento
            if self.x < self.coordenada_x_final:
                self.x = self.x + self.movimiento
            if self.y > self.coordenada_y_final:
                self.y = self.y - self.movimiento
            if self.y < self.coordenada_y_final:
                self.y = self.y + self.movimiento
            self.rect.x = self.x + 20
            self.rect.y = self.y

    def comprobar_coordenada(self):
        if abs(self.coordenada_x_final - self.x) < 10 and abs(self.coordenada_y_final - self.y) < 10:
            self.moviendose = False
