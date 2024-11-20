import mysql.connector

class Conexion:
    @staticmethod
    def conectar():
        # Este método intenta conectar a la base de datos MySQL con las credenciales proporcionadas.
        # Si la conexión es exitosa, devuelve el objeto de conexión.
        try:
            return mysql.connector.connect(
                host="localhost",  # Dirección del servidor MySQL (localhost en este caso)
                user="root",       # Usuario para la conexión (root)
                password="campusfp",  # Contraseña del usuario
                database="ENCUESTAS",  # Nombre de la base de datos a la que se conecta
                auth_plugin='mysql_native_password'  # Plugin de autenticación para mi equipo, en casos normales BORRAR ESTA LÍNEA.
            )
        except Exception as e:
            # Si ocurre algún error al intentar conectar, se captura la excepción y se imprime el mensaje de error.
            print("Error de conexión:", e)
            return None  # Si no se puede conectar, retorna None.
    
    @staticmethod
    def cerrar(conexion):
        # Este método cierra la conexión a la base de datos si la conexión existe.
        if conexion:
            conexion.close()
