from conexion import Conexion

class CrudEncuestas:
    @staticmethod
    def crear_encuesta(encuesta):
        try:
            con = Conexion.conectar()  # Establece la conexión a la base de datos
            cursor = con.cursor()  # Crea un cursor para ejecutar la consulta SQL
            query = """INSERT INTO ENCUESTA 
                    (idEncuesta, edad, Sexo, BebidasSemana, CervezasSemana, 
                    BebidasFinSemana, BebidasDestiladasSemana, VinosSemana, 
                    PerdidasControl, DiversionDependenciaAlcohol, ProblemasDigestivos, 
                    TensionAlta, DolorCabeza) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""  # Consulta SQL para insertar una nueva encuesta
            cursor.execute(query, encuesta)  # Ejecuta la consulta con los datos de la encuesta
            con.commit()  # Guarda los cambios en la base de datos
            print("Registro realizado con éxito")  # Confirma la operación
        except Exception as e:
            print("Error en crear encuesta:", e)  # Maneja errores en caso de fallos
        finally:
            Conexion.cerrar(con)  # Cierra la conexión a la base de datos

    @staticmethod
    def leer_encuestas(ordenar_por=None, filtros=None):
        try:
            con = Conexion.conectar()  # Establece la conexión a la base de datos
            cursor = con.cursor()  # Crea un cursor para ejecutar la consulta SQL
            query = "SELECT * FROM ENCUESTA"  # Consulta SQL básica para obtener todas las encuestas
            if filtros:  # Si se proporcionan filtros, los aplica a la consulta
                condiciones = " AND ".join(filtros)  # Une las condiciones de filtro con 'AND'
                query += f" WHERE {condiciones}"  # Añade la cláusula WHERE
            if ordenar_por:  # Si se especifica una columna para ordenar, la añade a la consulta
                query += f" ORDER BY {ordenar_por}"
            cursor.execute(query)  # Ejecuta la consulta
            encuestas = cursor.fetchall()  # Recupera todos los resultados
            return encuestas  # Devuelve los resultados
        except Exception as e:
            print("Error en lectura:", e)  # Maneja errores de lectura
            return []  # Devuelve una lista vacía en caso de error
        finally:
            Conexion.cerrar(con)  # Cierra la conexión a la base de datos

    @staticmethod
    def actualizar_encuesta(idEncuesta, nuevos_datos):
        try:
            con = Conexion.conectar()  # Establece la conexión a la base de datos
            cursor = con.cursor()  # Crea un cursor para ejecutar la consulta SQL
            query = """UPDATE ENCUESTA 
                       SET edad = %s, Sexo = %s, BebidasSemana = %s, CervezasSemana = %s, 
                       BebidasFinSemana = %s, BebidasDestiladasSemana = %s, VinosSemana = %s, 
                       PerdidasControl = %s, DiversionDependenciaAlcohol = %s, 
                       ProblemasDigestivos = %s, TensionAlta = %s, DolorCabeza = %s 
                       WHERE idEncuesta = %s"""  # Consulta SQL para actualizar una encuesta existente
            cursor.execute(query, (*nuevos_datos, idEncuesta))  # Ejecuta la consulta con los nuevos datos y el id de la encuesta
            con.commit()  # Guarda los cambios en la base de datos
            print("Actualización realizada con éxito")  # Confirma la operación
        except Exception as e:
            print("Error en actualización:", e)  # Maneja errores de actualización
        finally:
            Conexion.cerrar(con)  # Cierra la conexión a la base de datos

    @staticmethod
    def borrar_encuesta(idEncuesta):
        try:
            con = Conexion.conectar()  # Establece la conexión a la base de datos
            cursor = con.cursor()  # Crea un cursor para ejecutar la consulta SQL
            query = "DELETE FROM ENCUESTA WHERE idEncuesta = %s"  # Consulta SQL para eliminar una encuesta por su id
            cursor.execute(query, (idEncuesta,))  # Ejecuta la consulta con el id de la encuesta a eliminar
            con.commit()  # Guarda los cambios en la base de datos
            print("Encuesta eliminada con éxito")  # Confirma la operación
        except Exception as e:
            print("Error en borrar:", e)  # Maneja errores de eliminación
        finally:
            Conexion.cerrar(con)  # Cierra la conexión a la base de datos

