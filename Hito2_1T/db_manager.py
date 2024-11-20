import mysql.connector

class DBManager:
    def __init__(self):

        try:
            # Establecer la conexión
            conexion = mysql.connector.connect(
                host='localhost',
                user='tu_usuario',
                password='tu_contraseña',
                database='nombre_de_tu_base_de_datos'
            )
            print("Conexión exitosa.")
        except mysql.connector.Error as e:
            print("Error al conectar a la base de datos: ", e)


    def agregar_encuesta(self, datos):
        query = "INSERT INTO ENCUESTA (idEncuesta, edad, Sexo, BebidasSemana, CervezasSemana, BebidasFinSemana, BebidasDestiladasSemana, VinosSemana, PerdidasControl, DiversionDependenciaAlcohol, ProblemasDigestivos, TensionAlta, DolorCabeza) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query, datos)
        self.conexion.commit()

    def leer_encuestas(self):
        query = "SELECT * FROM ENCUESTA"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def actualizar_encuesta(self, idEncuesta, datos):
        query = "UPDATE ENCUESTA SET edad=%s, Sexo=%s, BebidasSemana=%s, CervezasSemana=%s, BebidasFinSemana=%s, BebidasDestiladasSemana=%s, VinosSemana=%s, PerdidasControl=%s, DiversionDependenciaAlcohol=%s, ProblemasDigestivos=%s, TensionAlta=%s, DolorCabeza=%s WHERE idEncuesta=%s"
        self.cursor.execute(query, datos + (idEncuesta,))
        self.conexion.commit()

    def eliminar_encuesta(self, idEncuesta):
        query = "DELETE FROM ENCUESTA WHERE idEncuesta=%s"
        self.cursor.execute(query, (idEncuesta,))
        self.conexion.commit()

    def consultar_ordenado(self, campo):
        query = f"SELECT * FROM ENCUESTA ORDER BY {campo}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def consultar_filtro(self, condicion):
        query = f"SELECT * FROM ENCUESTA WHERE {condicion}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()
