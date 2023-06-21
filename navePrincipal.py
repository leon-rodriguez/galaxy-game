from nave import Nave
from constantes import MOVIMIENTO_PERSONAJE
import pygame as pg


class NavePrincipal(Nave):  # clase hija de nave
    def __init__(self, vida, daño, velocidad, velocidad_tiro, imagen_nave, imagen_disparo, imagen_corazon, imagen_corazon_vacio, x, y, modificador_hitbox, vidas) -> None:
        super().__init__(vida, daño, velocidad, velocidad_tiro,
                         imagen_nave, imagen_disparo, x, y, modificador_hitbox)
        self.vidas = vidas
        self.imagen_corazon = imagen_corazon
        self.imagen_corazon_vacio = imagen_corazon_vacio
        self.vidas_inicial = self.vidas
        self.poder_recibir_disparos = True

    # cuando el usuario toca la tecla de arriba el personaje se mueve una unidad de movimiento
    def mover_arriba(self):
        if self.y > 0:
            self.y = self.y - MOVIMIENTO_PERSONAJE * self.velocidad
            self.rect.y = self.y

    # cuando el usuario toca la tecla de abajo el personaje se mueve una unidad de movimiento
    def mover_abajo(self, largo_ventana):
        if self.y + self.imagen_nave.get_height() < largo_ventana:
            self.y = self.y + MOVIMIENTO_PERSONAJE * self.velocidad
            self.rect.y = self.y

    def restar_vidas(self):  # cada vez que se recibe un impacto se resta una vida
        self.vidas -= 1

    # se dibujan los corazones que representan las vidas que uno tiene
    def dibujar_corazones(self, pantalla):
        posicion_x_corazon = 30
        for i in range(self.vidas):
            pantalla.blit(self.imagen_corazon, [posicion_x_corazon, 10])
            posicion_x_corazon += 40

        for i in range(self.vidas_inicial - self.vidas):
            pantalla.blit(self.imagen_corazon_vacio, [posicion_x_corazon, 10])
            posicion_x_corazon += 40
