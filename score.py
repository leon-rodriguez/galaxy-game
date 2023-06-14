class Score:
    def __init__(self) -> None:
        self.puntuacion = 0
        self.puntuacion_x_segundo = 50
        self.puntuacion_x_enemigo = 10

    def sumar_bonus_tiempo(self):
        self.puntuacion = self.puntuacion + self.puntuacion_x_segundo

    def sumar_bonus_enemigo(self):
        self.puntuacion = self.puntuacion + self.puntuacion_x_enemigo
