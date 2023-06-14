import pygame as pg
# from personaje import getSuperficie
from personaje import Personaje
from disapro import Disparo
from enemigo import Enemigo
from constantes import *
from score import Score

x = 0
lista_disparos = []
lista_enemigos = []


pg.init()

pantalla = pg.display.set_mode((ANCHO_VENTANA, LARGO_VENTANA))
pg.display.set_caption("Mi primer juego")
clock = pg.time.Clock()

# naves = getSuperficie("galaxian/images/sprites.png", 12, 2)
# principal = pg.transform.rotate(naves[0], -90)


background = pg.image.load("galaxian/images/background.jpg").convert()
background = pg.transform.scale(background, (ANCHO_VENTANA, LARGO_VENTANA))

personajePrincipal = Personaje()
primer_enemigo = Enemigo(900, 400)
segundo_enemigo = Enemigo(900, 140)
puntaje = Score()

lista_enemigos.append(primer_enemigo)
lista_enemigos.append(segundo_enemigo)


timer_Segundos = pg.USEREVENT
pg.time.set_timer(timer_Segundos, 1000)
print("timer segundos es", timer_Segundos)

segundos = 1
medio_Segundos = 0.5
flag_correr = True
while flag_correr:

    current_time = pg.time.get_ticks()
    lista_eventos = pg.event.get()
    for evento in lista_eventos:
        if evento.type == pg.QUIT:
            flag_correr = False
        if evento.type == pg.USEREVENT:
            if evento.type == timer_Segundos:
                disparo = Disparo(personajePrincipal.x, personajePrincipal.y,
                                  False, personajePrincipal.imagen_disparo)
                lista_disparos.append(disparo)
                disparo_enemigo = Disparo(
                    lista_enemigos[0].x, lista_enemigos[0].y, True, lista_enemigos[0].imagen_disparo)
                lista_disparos.append(disparo_enemigo)
    """
    print("ticks ", current_time)
    if abs(current_time / 1000 - segundos) < 0.1:
        # disparo = Disparo(personajePrincipal.9, personajePrincipal.y,
        #                   False, personajePrincipal.imagen_disparo)
        # lista_disparos.append(disparo)

        disparo_enemigo = Disparo(lista_enemigos[0].x, lista_enemigos[0].y,
                                  True, lista_enemigos[0].imagen_disparo)
        lista_disparos.append(disparo_enemigo)
        # print("segundos ", segundos)
        segundos += 1

    if abs(current_time / 1000 - medio_Segundos) < 0.6 and abs(current_time / 1000 - medio_Segundos) > 0.4:
        print(abs(current_time / 1000 - medio_Segundos))
        disparo = Disparo(personajePrincipal.x, personajePrincipal.y,
                          False, personajePrincipal.imagen_disparo)
        lista_disparos.append(disparo)
        # disparo_enemigo = Disparo(lista_enemigos[0].x, lista_enemigos[0].y,
        #                           True, lista_enemigos[0].imagen_disparo)
        # lista_disparos.append(disparo_enemigo)
        # print("segundos ", segundos)
        medio_Segundos += 0.5
    """
    x_relativa = x % background.get_rect().width
    pantalla.blit(background, (x_relativa - background.get_rect().width, 0))
    if x_relativa < ANCHO_VENTANA:
        pantalla.blit(background, (x_relativa, 0))
    # x -= 10

    for item in lista_enemigos:
        item.generar_coordenadas(LARGO_VENTANA, ANCHO_VENTANA)
        item.mover()
        item.comprobar_coordenada()

    lista_teclas = pg.key.get_pressed()
    if True in lista_teclas:
        if lista_teclas[pg.K_UP]:
            personajePrincipal.moverAriiba()
            # personajePrincipal.velocidadTiro = 500
        if lista_teclas[pg.K_DOWN]:
            personajePrincipal.moverAbajo(LARGO_VENTANA)

    # pantalla.blit(background, [0, 0])
    print("lista disparos ", len(lista_disparos))
    for item in lista_disparos:
        item.mover()
        item.dibujar(pantalla)
        if item.checkear_visibilidad(ANCHO_VENTANA) == False:
            lista_disparos.remove(item)
        flag = True
        # for enemigo in lista_enemigos:
        #     if enemigo.comprobar_colision(item.rect, personajePrincipal.daño) and flag:
        #         lista_disparos.remove(item)
        #         flag = False
        #         if enemigo.vida < 1:
        #             lista_enemigos.remove(enemigo)
        #             lista_enemigos.append(Enemigo(900, 500))
        #             puntaje.sumar_bonus_enemigo()
        # la flag es para q no borre el disparo, itere de vuelta e intente # #borrarlo de vuelta y me de error :)
    personajePrincipal.dibujar(pantalla)
    for item in lista_enemigos:
        item.dibujar(pantalla)

    clock.tick(FPS)
    pg.display.flip()
    # print(puntaje.puntuacion)
pg.quit

"""
132.129032258 ancho la imagen enemiga
106 alto la imagen enemiga
57.4 a la derecha
65.56 a la izquierda
405.853658537 alto de los sprites en cuadraditos
33.8211382114 alto imagen en cuadrditos
277.333333333 alto imagen en pixels
73.8 pixeles desde arriba hacia la imagen
"""
