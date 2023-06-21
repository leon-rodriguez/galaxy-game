from constantes import ANCHO_VENTANA, BLANCO


class Score:  # clase con la que se maneja el puntaje que se va guardndo

    def __init__(self, fuente) -> None:
        self.puntuacion = 0
        self.puntuacion_x_segundo = 10
        self.puntuacion_x_enemigo = 50
        self.texto = "Puntaje: {0}".format(self.puntuacion)
        self.texto_a_devolver = fuente.render(
            self.texto, True, BLANCO)

    def sumar_bonus_tiempo(self):  # se suma la puntuacion por segundo
        self.puntuacion = self.puntuacion + self.puntuacion_x_segundo

    def sumar_bonus_enemigo(self):  # se suma la puntuacion por enemigo
        self.puntuacion = self.puntuacion + self.puntuacion_x_enemigo

    # se actualiza el texto a mostrar en la pantalla
    def actualizar_texto(self, fuente):
        self.texto = "Puntaje: {0}".format(self.puntuacion)
        self.texto_a_devolver = fuente.render(
            self.texto, True, BLANCO)

    def dibujar_texto(self, pantalla):  # se dibuja el texto a mostrar
        pantalla.blit(self.texto_a_devolver,
                      ((ANCHO_VENTANA / 2) - (self.texto_a_devolver.get_width() / 2), 10))

    def resetear_score(self, fuente):  # se resetean los valores
        self.puntuacion = 0
        self.texto = "Puntaje: {0}".format(self.puntuacion)
        self.texto_a_devolver = fuente.render(
            self.texto, True, BLANCO)
