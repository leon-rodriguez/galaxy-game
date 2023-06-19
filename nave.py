import pygame as pg
from constantes import MOVIMIENTO_PERSONAJE

# nave_personaje_principal = pg.image.load(
#     "galaxian/images/personaje_principal.png")
# nave_personaje_principal = pg.transform.rotate(nave_personaje_principal, -90)

# disparo_personaje_principal = pg.image.load(
#     "galaxian/images/disparos/disparo_personaje_principal.png")
# # naves = getSuperficie("galaxian/images/sprites.png", 12, 2)
# disparo_personaje_principal = pg.transform.rotate(
#     disparo_personaje_principal, -90)


class Nave:
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

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen_nave, [self.x, self.y])

    def comprobar_colision(self, otro_rect) -> bool:
        if self.rect.colliderect(otro_rect):
            return True

    def restar_vida(self, daño_recibido):
        self.vida = self.vida - daño_recibido
