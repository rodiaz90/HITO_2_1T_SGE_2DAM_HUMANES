from ui import App  # Importa la clase App desde ui.py
from db_manager import DBManager  # Importa la clase DBManager desde db_manager.py

def main():
    # Inicializar la conexión a la base de datos
    db_manager = DBManager()

    # Crear y ejecutar la aplicación Tkinter con la instancia de db_manager
    app = App(db_manager)
    app.run()

    # Cerrar la conexión a la base de datos al salir
    db_manager.cerrar_conexion()

if __name__ == "__main__":
    main()
