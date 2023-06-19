import pygame as pg
from utilidades import *
from score import Score
from contadores import Contadores
from navePrincipal import NavePrincipal
from naveEnemiga import NaveEnemiga
from disapro import Disparo
from constantes import *


class Entorno:
    def __init__(self) -> None:
        self.fuente = pg.font.SysFont("Fixedsys Normal", 45)
        self.lista_disparos = []
        self.lista_enemigos = []
        self.personajePrincipal = setear_personaje(NavePrincipal)
        self.primer_enemigo = setear_personaje_enemigo(NaveEnemiga)
        self.segundo_enemigo = setear_personaje_enemigo(NaveEnemiga)
        self.tercer_enemigo = setear_personaje_enemigo(NaveEnemiga)
        self.puntaje = Score(self.fuente)
        self.contadores = Contadores(
            self.lista_disparos, self.personajePrincipal, self.lista_enemigos)
        self.background_x = 0
        self.texto_usuario = ""
        self.flag_estado_juego = ESTADO_INICIAL
        self.flag_correr = True
        self.sonido_boton_start = pg.mixer.Sound("galaxian/sounds/inicio.wav")
        self.sonido_muerte = pg.mixer.Sound("galaxian/sounds/muerte.wav")
        self.sonido_disparo = pg.mixer.Sound("galaxian/sounds/disparo.wav")
        self.sonido_disparo_recibido = pg.mixer.Sound(
            "galaxian/sounds/disparo_recibido.wav")

    def inicializar_juego(self):
        self.lista_enemigos.append(self.primer_enemigo)
        self.lista_enemigos.append(self.segundo_enemigo)
        self.lista_enemigos.append(self.tercer_enemigo)

    def resetear_juego(self):
        self.lista_disparos = []
        self.lista_enemigos = []
        self.personajePrincipal = setear_personaje(NavePrincipal)
        self.primer_enemigo = setear_personaje_enemigo(NaveEnemiga)
        self.segundo_enemigo = setear_personaje_enemigo(NaveEnemiga)
        self.tercer_enemigo = setear_personaje_enemigo(NaveEnemiga)
        self.puntaje = Score(self.fuente)
        self.contadores = Contadores(
            self.lista_disparos, self.personajePrincipal, self.lista_enemigos)
        self.background_x = 0
        self.flag_estado_juego = ESTADO_JUGANDO
        self.flag_correr = True
        self.inicializar_juego()

    def correr_inicio(self, pantalla):
        boton_start = pg.image.load("galaxian/images/boton_start.png")
        boton_start = pg.transform.scale(boton_start, (260, 120))
        rect_boton_start = pg.Rect(
            ANCHO_VENTANA / 2 - boton_start.get_width() / 2, 620, boton_start.get_width(), boton_start.get_height())

        lista_eventos = pg.event.get()
        for evento in lista_eventos:
            if evento.type == pg.QUIT:
                self.flag_correr = False
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_BACKSPACE:
                    self.texto_usuario = self.texto_usuario[0:-1]
                elif len(self.texto_usuario) < 13:
                    self.texto_usuario += evento.unicode
            if evento.type == pg.MOUSEBUTTONDOWN:
                if rect_boton_start.collidepoint(evento.pos) and len(self.texto_usuario) > 0:
                    self.sonido_boton_start.play()
                    self.flag_estado_juego = ESTADO_JUGANDO

        input_texto = pg.Rect((ANCHO_VENTANA / 2) - (240) / 2, 400, 240, 70)
        titulo_imagen = pg.image.load("galaxian/images/titulo.png")

        texto_a_mostrar = self.fuente.render(
            self.texto_usuario, True, (255, 255, 255))

        pg.draw.rect(pantalla, (0, 0, 0), input_texto)
        pg.draw.rect(pantalla, BLANCO, input_texto, 2)

        pantalla.blit(titulo_imagen, ((ANCHO_VENTANA / 2) -
                                      (titulo_imagen.get_width() / 2), 30))
        pantalla.blit(boton_start, ((ANCHO_VENTANA / 2) -
                                    (boton_start.get_width() / 2), 620))
        pantalla.blit(texto_a_mostrar,
                      (input_texto.x + 10, input_texto.y + 15))

    def correr_juego(self, pantalla, baseDeDatos, background):
        current_time = pg.time.get_ticks()
        # TODO pasar entorno a clase ciclos
        self.contadores.ciclos(current_time, self.puntaje, self.fuente)

        # pg.mixer.music.load(
        # "galaxian/sounds/musica_de_fondo.wav")
        # pg.mixer.music.play(1)

        lista_eventos = pg.event.get()
        for evento in lista_eventos:
            if evento.type == pg.QUIT:
                self.flag_correr = False
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_SPACE and self.contadores.poder_disparar == True:
                    self.sonido_disparo.play()
                    disparo = Disparo(self.personajePrincipal.x, self.personajePrincipal.y,
                                      False, self.personajePrincipal.imagen_disparo)
                    self.lista_disparos.append(disparo)
                    self.contadores.cooldown_disparos(
                        current_time, self.personajePrincipal.velocidad_tiro)

        manejar_movimiento_pantalla(background, pantalla, self.background_x)
        self.background_x -= 4

        manejar_moviimento_enemigos(self.lista_enemigos, pantalla)

        manejar_teclas(pg, self.personajePrincipal)

        manejar_disparos(pantalla, self, current_time)

        self.personajePrincipal.dibujar_corazones(pantalla)

        self.personajePrincipal.dibujar(pantalla)

        for item in self.lista_enemigos:
            item.dibujar(pantalla)

        # print(self.puntaje.puntuacion)
        self.puntaje.dibujar_texto(pantalla)

        if self.personajePrincipal.vidas == 0:
            self.sonido_muerte.play()
            # self.contadores.delay_para_musica(
            # current_time, self.sonido_muerte.get_length() * 1000)
            baseDeDatos.insertar_puntajes(
                self.texto_usuario, self.puntaje.puntuacion)
            # if self.contadores.seguir_ejecucion == True:
            self.flag_estado_juego = ESTADO_FINAL

    def correr_final(self, pantalla, baseDeDatos):
        # renderizar boton
        boton_start = pg.image.load("galaxian/images/boton_start.png")
        boton_start = pg.transform.scale(boton_start, (260, 120))
        rect_boton_start = pg.Rect(800, LARGO_VENTANA / 2 - boton_start.get_height() /
                                   2, boton_start.get_width(), boton_start.get_height())

        # capturar si se clickeo el boton de start o de cerrar juego
        lista_eventos = pg.event.get()
        for evento in lista_eventos:
            if evento.type == pg.QUIT:
                self.flag_correr = False
            if evento.type == pg.MOUSEBUTTONDOWN:
                if rect_boton_start.collidepoint(evento.pos):
                    self.sonido_boton_start.play()
                    print(self.sonido_boton_start.get_length())
                    self.resetear_juego()

        pantalla.fill((0, 0, 0))

        pantalla.blit(boton_start, (800, LARGO_VENTANA /
                                    2 - boton_start.get_height() / 2))
        actual_puntaje_texto = self.fuente.render(
            "TU PUNTAJE ES: {0}".format(self.puntaje.puntuacion), True, BLANCO)
        pantalla.blit(actual_puntaje_texto, (100, LARGO_VENTANA / 2 - actual_puntaje_texto.get_height() /
                                             2))

        x_tabla = MITAD_PANTALLA - (ANCHO_TABLA / 2)

        titulo_tabla = pg.Rect((x_tabla, 100), (ANCHO_TABLA, ALTO_FILA))

        tabla_ordenada = baseDeDatos.devolver_tabla_ordenada()

        y_texto_linea = 180
        if len(tabla_ordenada) > 10:
            titulo = self.fuente.render("TOP 10 PUNTAJES", True, BLANCO)
            pantalla.blit(titulo, ((ANCHO_VENTANA / 2) -
                                   (titulo.get_width() / 2), titulo_tabla.y))
            for i in range(10):
                texto_linea = "{0}: {1}".format(
                    tabla_ordenada[i]["usuario"], tabla_ordenada[i]["puntaje"])
                texto_linea_a_mostrar = self.fuente.render(
                    texto_linea, True, BLANCO)
                pantalla.blit(texto_linea_a_mostrar, ((ANCHO_VENTANA / 2) -
                                                      (texto_linea_a_mostrar.get_width() / 2), y_texto_linea))
                y_texto_linea += ALTO_FILA
        else:
            titulo = self.fuente.render("TOP PUNTAJES", True, BLANCO)
            pantalla.blit(titulo, ((ANCHO_VENTANA / 2) -
                                   (titulo.get_width() / 2), titulo_tabla.y))
            for i in range(len(tabla_ordenada)):
                texto_linea = "{0}: {1}".format(
                    tabla_ordenada[i]["usuario"], tabla_ordenada[i]["puntaje"])
                texto_linea_a_mostrar = self.fuente.render(
                    texto_linea, True, BLANCO)
                pantalla.blit(texto_linea_a_mostrar, ((ANCHO_VENTANA / 2) -
                                                      (texto_linea_a_mostrar.get_width() / 2), y_texto_linea))
                y_texto_linea += ALTO_FILA
