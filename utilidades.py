from constantes import *
from naveEnemiga import NaveEnemiga
from random import randint


def setear_personaje(NavePrincipal):  # instancia la clase navePrincipal y la retorna
    personajePrincipal = NavePrincipal(NAVE["vida"], NAVE["daño"], NAVE["velocidad"],
                                       NAVE["velocidadTiro"], NAVE["imagen"], NAVE["imagen_disparo"], NAVE["imagen_corazon"], NAVE["imagen_corazon_vacio"], NAVE["x"], NAVE["y"], NAVE["modificador_h"], NAVE["vidas"])
    return personajePrincipal


# instancia la clase enemiga con el enemigo 4, que es el primero que aparece
def setear_personaje_enemigo(NaveEnemiga):
    coordenada_x = ANCHO_VENTANA + NAVES_E[4]["imagen"].get_width() + 20
    coordenada_y = randint(0, LARGO_VENTANA -
                           NAVES_E[4]["imagen"].get_height())
    enemigo = NaveEnemiga(NAVES_E[4]["vida"], NAVES_E[4]["daño"], NAVES_E[4]["velocidad"],
                          NAVES_E[4]["velocidadTiro"], NAVES_E[4]["imagen"], NAVES_E[4]["imagen_disparo"], coordenada_x, coordenada_y, NAVE["modificador_h"], NAVES_E[4]["moviendose"], ANCHO_VENTANA - NAVES_E[4]["imagen"].get_height(),  coordenada_y)
    return enemigo


# esta funcion se encarga de mover y dibujar los disparos ademas de comprobar la colision de cada uno con enemigos y personaje principal
def manejar_disparos(pantalla, entorno, tiempo_actual):
    for item in entorno.lista_disparos:
        item.mover()
        item.dibujar(pantalla)
        if item.checkear_visibilidad(ANCHO_VENTANA) == False:
            entorno.lista_disparos.remove(item)
        flag = True
        for enemigo in entorno.lista_enemigos:

            if enemigo.comprobar_colision(item.rect) and flag and item.es_enemigo == False:
                try:
                    entorno.lista_disparos.remove(item)
                except ValueError:
                    print("ahi fallo")
                enemigo.restar_vida(entorno.personajePrincipal.daño)
                enemigo.actualizar_rectangulo_vida()
                flag = False
                if enemigo.vida < 1:
                    entorno.lista_enemigos.remove(enemigo)
                    nuevo_enemigo = randint(0, len(NAVES_E) - 1)
                    coordenada_x = ANCHO_VENTANA + \
                        NAVES_E[nuevo_enemigo]["imagen"].get_width() + 20
                    coordenada_y = randint(0, LARGO_VENTANA -
                                           NAVES_E[nuevo_enemigo]["imagen"].get_height())
                    nueva_nave_enemiga = NaveEnemiga(NAVES_E[nuevo_enemigo]["vida"], NAVES_E[nuevo_enemigo]["daño"], NAVES_E[nuevo_enemigo]["velocidad"],
                                                     NAVES_E[nuevo_enemigo]["velocidadTiro"], NAVES_E[nuevo_enemigo]["imagen"], NAVES_E[nuevo_enemigo]["imagen_disparo"], coordenada_x, coordenada_y, NAVE["modificador_h"], NAVES_E[nuevo_enemigo]["moviendose"], ANCHO_VENTANA - NAVES_E[nuevo_enemigo]["imagen"].get_height(),  coordenada_y)
                    entorno.lista_enemigos.append(nueva_nave_enemiga)
                    entorno.puntaje.sumar_bonus_enemigo()
                    entorno.puntaje.actualizar_texto(entorno.fuente)

        if entorno.personajePrincipal.comprobar_colision(item.rect) and item.es_enemigo == True and entorno.contadores.poder_recibir_disparos == True:
            entorno.contadores.no_recibir_disparos(tiempo_actual, 2000)
            if entorno.personajePrincipal.vidas > 1:
                entorno.sonido_disparo_recibido.play()
            entorno.personajePrincipal.restar_vidas()
            try:
                entorno.lista_disparos.remove(item)
            except ValueError:
                print("ahi fallo")


# esta funcion usa los metodos de naveEnemiga para m,anejar los movimientos de los enemigos
def manejar_moviimento_enemigos(lista_enemigos: list, pantalla):
    for item in lista_enemigos:
        item.generar_coordenadas(LARGO_VENTANA, ANCHO_VENTANA)
        item.mover(pantalla)
        item.comprobar_coordenada()


# se comprueba si el usuario toca tecla de arriba o abajo
def manejar_teclas(pg, personajePrincipal):
    lista_teclas = pg.key.get_pressed()
    if True in lista_teclas:
        if lista_teclas[pg.K_UP]:
            personajePrincipal.mover_arriba()
        if lista_teclas[pg.K_DOWN]:
            personajePrincipal.mover_abajo(LARGO_VENTANA)


# se maneja el movimiento de pantalla
def manejar_movimiento_pantalla(background, pantalla, x):
    x_relativa = x % background.get_rect().width
    pantalla.blit(background, (x_relativa - background.get_rect().width, 0))
    if x_relativa < ANCHO_VENTANA:
        pantalla.blit(background, (x_relativa, 0))
