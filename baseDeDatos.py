import sqlite3


class BaseDeDatos:  # clase que representa la base de datos
    def __init__(self) -> None:
        pass

    # este metodo crea la tabla puntajes con columnas de id, usuario y puntaje
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

    # este metodo inserta a la tabla el puntaje del usuario y su nombre
    def insertar_puntajes(self, usuario, puntaje):
        with sqlite3.connect("bd_puntajes.db") as conexion:
            try:
                conexion.execute(
                    "insert into puntajes(usuario,puntaje) values (?,?)", (usuario, puntaje))
            except:
                print("error")

    # este metodo retorna la tabla ordenada cuando se lo ejecuta
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
