import pygame as pg
from constantes import MOVIMIENTO_ENEMIGO
import random
from nave import Nave

# disparo_enemigo_basico = pg.image.load(
#     "galaxian/images/disparo_enemigo_basico.png")
# disparo_enemigo_basico = pg.transform.rotate(disparo_enemigo_basico, 90)


class NaveEnemiga(Nave):  # hija de la clase nave
    def __init__(self, vida, daño, velocidad, velocidad_tiro, imagen_nave, imagen_disparo, x, y, modificador_hitbox, moviendose, coordenada_x_final, coordenada_y_final) -> None:
        super().__init__(vida, daño, velocidad, velocidad_tiro,
                         imagen_nave, imagen_disparo, x, y, modificador_hitbox)
        self.moviendose = moviendose
        self.coordenada_x_final = coordenada_x_final
        self.coordenada_y_final = coordenada_y_final
        self.rectangulo_vida = pg.Rect(
            (self.x, self.y + self.imagen_nave.get_height() + 10), (self.imagen_nave.get_width(), 7))

        self.rectangulo_vida_rojo = pg.Rect(
            (self.x, self.y + self.imagen_nave.get_height() + 10), (self.imagen_nave.get_width(), 7))

        self.vida_inicial = vida

    def restar_vida(self, daño_recibido):  # se resta a la vida el daño recibido
        self.vida = self.vida - daño_recibido

    # si la nave no se esta moviendo se generan aleatoriamente unas nuevas coordenadas a donde se tieen que dirigir
    def generar_coordenadas(self, largo_ventana, ancho_ventana):
        if self.moviendose == False:
            self.coordenada_x_final = random.randint(
                700, ancho_ventana - self.imagen_nave.get_width())
            self.coordenada_y_final = random.randint(
                0, largo_ventana - self.imagen_nave.get_height())
            self.moviendose = True

    # se actualiza el la posicion del rectangulo de la vida de cada nave enemiga
    def actualizar_posicion_rectangulo(self):
        self.rectangulo_vida_rojo = pg.Rect(
            (self.x, self.y + self.imagen_nave.get_height() + 10), (self.imagen_nave.get_width(), 7))
        partes_imagen = self.imagen_nave.get_width() / self.vida_inicial
        self.rectangulo_vida = pg.Rect(
            (self.x, self.y + self.imagen_nave.get_height() + 10), (partes_imagen * self.vida, 7))

    # se dibujan los rectangulos de vida de nave enemiga
    def dibujar_rectangulo(self, pantalla):
        pg.draw.rect(pantalla, (255, 40, 23), self.rectangulo_vida_rojo)
        pg.draw.rect(pantalla, (0, 255, 27), self.rectangulo_vida)

    def mover(self, pantalla):  # si la nave se esta moviendo(no llego a su destino) se calcula a que direccion tiene que ir y se mueve una unidad de movimiento
        if self.moviendose == True:
            if self.x > self.coordenada_x_final:
                self.x = self.x - MOVIMIENTO_ENEMIGO
            if self.x < self.coordenada_x_final:
                self.x = self.x + MOVIMIENTO_ENEMIGO
            if self.y > self.coordenada_y_final:
                self.y = self.y - MOVIMIENTO_ENEMIGO
            if self.y < self.coordenada_y_final:
                self.y = self.y + MOVIMIENTO_ENEMIGO
            self.rect.x = self.x + 20
            self.rect.y = self.y
            self.actualizar_posicion_rectangulo()
            self.dibujar_rectangulo(pantalla)

    # se comprueba si se llego a menos de 10 pixeles del destino
    def comprobar_coordenada(self):
        if abs(self.coordenada_x_final - self.x) < 10 and abs(self.coordenada_y_final - self.y) < 10:
            self.moviendose = False

    # se actualiza el rectangulo de la vida del enemigo
    def actualizar_rectangulo_vida(self):
        partes_imagen = self.imagen_nave.get_width() / self.vida_inicial
        self.rectangulo_vida = pg.Rect(
            (self.x, self.y + self.imagen_nave.get_height() + 10), (partes_imagen * self.vida, 7))
