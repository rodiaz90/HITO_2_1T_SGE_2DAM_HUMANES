import tkinter as tk
from tkinter import ttk, messagebox

class App(tk.Tk):
    def __init__(self, db_manager):
        super().__init__()
        self.title("Gestión de Encuestas - Clínica de Salud")
        self.geometry("800x600")
        self.db_manager = db_manager

        # Widgets de la interfaz
        self.label_id = tk.Label(self, text="ID Encuesta:")
        self.label_id.pack()
        self.entry_id = tk.Entry(self)
        self.entry_id.pack()

        self.label_edad = tk.Label(self, text="Edad:")
        self.label_edad.pack()
        self.entry_edad = tk.Entry(self)
        self.entry_edad.pack()

        # Botones CRUD
        self.btn_agregar = tk.Button(self, text="Agregar Encuesta", command=self.agregar_encuesta)
        self.btn_agregar.pack()

        self.btn_leer = tk.Button(self, text="Leer Encuestas", command=self.leer_encuestas)
        self.btn_leer.pack()

        # Botón para gráficos
        self.btn_grafico_barras = tk.Button(self, text="Gráfico de Barras", command=self.grafico_barras)
        self.btn_grafico_barras.pack()

    def agregar_encuesta(self):
        try:
            datos = (
                int(self.entry_id.get()),
                int(self.entry_edad.get()),
                "M",  # Ejemplo de sexo
                5, 5, 5, 5, 5, 5, 'SI', 'NO', 'Normal', 'Normal'
            )
            self.db_manager.agregar_encuesta(datos)
            messagebox.showinfo("Éxito", "Encuesta agregada correctamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def leer_encuestas(self):
        encuestas = self.db_manager.leer_encuestas()
        for encuesta in encuestas:
            print(encuesta)  # Mostrar en consola o agregar a un widget

    def grafico_barras(self):
        datos = self.db_manager.leer_encuestas()
        # Aquí se llama al método correspondiente de PlotManager
        # Asegúrate de que el campo de edad sea el índice correcto
        from plot_manager import PlotManager
        PlotManager.grafico_barras(datos, 1)

    def run(self):
        self.mainloop()
