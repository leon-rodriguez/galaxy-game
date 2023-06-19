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
ESTADO_INICIAL = 1
ESTADO_JUGANDO = 2
ESTADO_FINAL = 3

nave_principal_imagen = pg.image.load(
    "galaxian/images/naves/personaje_principal.png")
nave_principal_imagen = pg.transform.rotate(nave_principal_imagen, -90)

disparo_principal_imagen = pg.image.load(
    "galaxian/images/disparos/disparo_personaje_principal.png")
disparo_principal_imagen = pg.transform.rotate(disparo_principal_imagen, -90)

# nave_enemiga = pg.image.load(
#     "galaxian/images/naves/enemigo_basico.png")
# nave_enemiga = pg.transform.rotate(nave_enemiga, 90)

# disparo_enemigo_imagen = pg.image.load(
#     "galaxian/images/disparos/disparo_enemigo_basico.png")
# disparo_enemigo_imagen = pg.transform.rotate(disparo_enemigo_imagen, 90)


def imagen_nave_enemiga(path):
    nave_enemiga = pg.image.load(
        path)
    nave_enemiga = pg.transform.rotate(nave_enemiga, 90)
    return nave_enemiga


def imagen_disparo_enemigo(path):
    disparo_enemigo = pg.image.load(
        path)
    disparo_enemigo = pg.transform.rotate(disparo_enemigo, -90)
    return disparo_enemigo


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
    "y": LARGO_VENTANA / 2,
    "modificador_h": -40,
    "vidas": 5
}

NAVES_E = [
    # ENEMIGO BASICO
    {
        "vida": 3,
        "daño": 10,
        "velocidad": 1,
        "velocidadTiro": 1100,
        "imagen": imagen_nave_enemiga("galaxian/images/naves/enemigo_basico.png"),
        "imagen_disparo": imagen_disparo_enemigo("galaxian/images/disparos/disparo_enemigo_basico.png"),
        "x": 900,
        "y": 700,
        "modificador_h": 20,
        "moviendose": True,
        "coordenada_x_final": 0,
        "coordenada_y_final": 0,
    },
    # NAVE 3
    {
        "vida": 4,
        "daño": 10,
        "velocidad": 1,
        "velocidadTiro": 1600,
        "imagen": imagen_nave_enemiga("galaxian/images/naves/nave3.png"),
        "imagen_disparo": imagen_disparo_enemigo("galaxian/images/disparos/disparo_nave3.png"),
        "x": 900,
        "y": 700,
        "modificador_h": 20,
        "moviendose": True,
        "coordenada_x_final": 0,
        "coordenada_y_final": 0,
    },
    # NAVE 4
    {
        "vida": 2,
        "daño": 10,
        "velocidad": 1,
        "velocidadTiro": 2500,
        "imagen": imagen_nave_enemiga("galaxian/images/naves/nave4.png"),
        "imagen_disparo": imagen_disparo_enemigo("galaxian/images/disparos/disparo_nave4.png"),
        "x": 900,
        "y": 700,
        "modificador_h": 20,
        "moviendose": True,
        "coordenada_x_final": 0,
        "coordenada_y_final": 0,
    },
    # NAVE 5
    {
        "vida": 4,
        "daño": 10,
        "velocidad": 1,
        "velocidadTiro": 2200,
        "imagen": imagen_nave_enemiga("galaxian/images/naves/nave5.png"),
        "imagen_disparo": imagen_disparo_enemigo("galaxian/images/disparos/disparo_nave5.png"),
        "x": 900,
        "y": 700,
        "modificador_h": 20,
        "moviendose": True,
        "coordenada_x_final": 0,
        "coordenada_y_final": 0,
    },
    # NAVE 7
    {
        "vida": 2,
        "daño": 10,
        "velocidad": 1,
        "velocidadTiro": 1000,
        "imagen": imagen_nave_enemiga("galaxian/images/naves/nave7.png"),
        "imagen_disparo": imagen_disparo_enemigo("galaxian/images/disparos/disparo_nave7.png"),
        "x": 900,
        "y": 700,
        "modificador_h": 20,
        "moviendose": True,
        "coordenada_x_final": 0,
        "coordenada_y_final": 0,
    },
    # NAVE 11
    {
        "vida": 6,
        "daño": 10,
        "velocidad": 1,
        "velocidadTiro": 4000,
        "imagen": imagen_nave_enemiga("galaxian/images/naves/nave11.png"),
        "imagen_disparo": imagen_disparo_enemigo("galaxian/images/disparos/disparo_nave11.png"),
        "x": 900,
        "y": 700,
        "modificador_h": 20,
        "moviendose": True,
        "coordenada_x_final": 0,
        "coordenada_y_final": 0,
    },
]
