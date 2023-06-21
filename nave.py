import pygame as pg


class Nave:  # esta clase nave es la clase padre que hace heredar a sus dos hijos los tres metodos declarados y las propiedades
    def __init__(self, vida, daño, velocidad, velocidad_tiro, imagen, imagen_disparo, x, y, modificador_hitbox) -> None:
        self.vida = vida
        self.daño = daño
        self.velocidad = velocidad
        self.velocidad_tiro = velocidad_tiro
        self.imagen_nave = imagen
        self.imagen_disparo = imagen_disparo
        self.x = x
        self.y = y
        self.rect = pg.Rect(self.x + modificador_hitbox, self.y,
                            self.imagen_nave.get_width(), self.imagen_nave.get_height())

    def dibujar(self, pantalla):  # dibuja la nave en la pantalla
        pantalla.blit(self.imagen_nave, [self.x, self.y])

    # comprueba la colision de la nave con otro objeto, si es verdadero retorna true
    def comprobar_colision(self, otro_rect) -> bool:
        if self.rect.colliderect(otro_rect):
            return True
