import sqlite3


class BaseDeDatos:
    def __init__(self) -> None:
        pass

    def crear_tabla(self):
        with sqlite3.connect("bd_puntajes.db") as conexion:
            try:
                sentencia = ''' create  table puntajes
                (
                id integer primary key autoincrement,
                usuario text,
                puntaje integer
                )
                '''
                conexion.execute(sentencia)
                print("Se creo la tabla personajes")
            except sqlite3.OperationalError:
                print("La tabla personajes ya existe")

    def insertar_puntajes(self, usuario, puntaje):
        with sqlite3.connect("bd_puntajes.db") as conexion:
            try:
                conexion.execute(
                    "insert into puntajes(usuario,puntaje) values (?,?)", (usuario, puntaje))
            except:
                print("error")

    def devolver_tabla_ordenada(self) -> list:
        tabla_ordenada = []
        with sqlite3.connect("bd_puntajes.db") as conexion:
            cursor = conexion.execute(
                "SELECT * FROM puntajes ORDER BY puntaje DESC")
            for fila in cursor:
                tabla_ordenada.append({
                    "usuario": fila[1],
                    "puntaje": fila[2]
                })
        return tabla_ordenada
