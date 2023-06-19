import pygame as pg

MOVIMIENTO_PERSONAJE = 8
MOVIMIENTO_ENEMIGO = 3
COLOR_PANTALLA = (255, 155, 155)
BLANCO = (255, 255, 255)
ANCHO_VENTANA = 1200
LARGO_VENTANA = 800
FPS = 60
ANCHO_TABLA = 500
ALTO_FILA = 60
MITAD_PANTALLA = ANCHO_VENTANA / 2

nave_principal_imagen = pg.image.load(
    "galaxian/images/personaje_principal.png")
nave_principal_imagen = pg.transform.rotate(nave_principal_imagen, -90)

disparo_principal_imagen = pg.image.load(
    "galaxian/images/disparo_personaje_principal.png")
disparo_principal_imagen = pg.transform.rotate(disparo_principal_imagen, -90)

nave_enemiga = pg.image.load(
    "galaxian/images/enemigo_basico.png")
nave_enemiga = pg.transform.rotate(nave_enemiga, 90)

disparo_enemigo_imagen = pg.image.load(
    "galaxian/images/disparo_enemigo_basico.png")
disparo_enemigo_imagen = pg.transform.rotate(disparo_enemigo_imagen, 90)


corazon = pg.image.load(
    "galaxian/images/corazon.png")
corazon = pg.transform.scale(corazon, (30, 30))

corazon_vacio = pg.image.load(
    "galaxian/images/corazon_vacio.png")
corazon_vacio = pg.transform.scale(corazon_vacio, (30, 30))


NAVE = {
    "vida": 100,
    "daño": 1,
    "velocidad": 1,
    "velocidadTiro": 400,
    "imagen": nave_principal_imagen,
    "imagen_disparo": disparo_principal_imagen,
    "imagen_corazon": corazon,
    "imagen_corazon_vacio": corazon_vacio,
    "x": 0,
    "y": 0,
    "modificador_h": -20,
    "vidas": 5
}

NAVE_E = {
    "vida": 3,
    "daño": 10,
    "velocidad": 1,
    "velocidadTiro": 500,
    "imagen": nave_enemiga,
    "imagen_disparo": disparo_enemigo_imagen,
    "x": 900,
    "y": 700,
    "modificador_h": 20,
    "moviendose": False,
    "coordenada_x_final": 0,
    "coordenada_y_final": 0,
}
