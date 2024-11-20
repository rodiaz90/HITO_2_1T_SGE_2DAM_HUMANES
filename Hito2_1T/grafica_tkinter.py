import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
from graficos import Graficos
from crud import CrudEncuestas

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CRUD Encuestas")
        self.geometry("1650x700")
        self.crear_pantalla_principal()

    def crear_pantalla_principal(self):
        """Crea la pantalla principal con los botones centrados y responsivos"""
        
        # Configurar el número de columnas y hacerlas expandibles
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        # Fila 1: los primeros 4 botones (centrados)
        self.boton_crear = tk.Button(self, text="Crear Encuesta", command=self.mostrar_crear)
        self.boton_crear.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        self.boton_leer = tk.Button(self, text="Leer Encuestas", command=self.mostrar_leer)
        self.boton_leer.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        
        self.boton_actualizar = tk.Button(self, text="Actualizar Encuesta", command=self.mostrar_actualizar)
        self.boton_actualizar.grid(row=0, column=2, padx=10, pady=10, sticky="ew")
        
        self.boton_borrar = tk.Button(self, text="Borrar Encuesta", command=self.mostrar_borrar)
        self.boton_borrar.grid(row=0, column=3, padx=10, pady=10, sticky="ew")

        # Fila 2: los botones de gráficos (centrados)
        self.boton_grafico_barras = tk.Button(self, text="Gráfico de Barras", command=lambda: Graficos.mostrar_grafico("barras"))
        self.boton_grafico_barras.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        
        self.boton_grafico_pastel = tk.Button(self, text="Gráfico de Pastel", command=lambda: Graficos.mostrar_grafico("pastel"))
        self.boton_grafico_pastel.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        
        self.boton_grafico_lineas = tk.Button(self, text="Gráfico de Líneas", command=lambda: Graficos.mostrar_grafico("lineas"))
        self.boton_grafico_lineas.grid(row=1, column=2, padx=10, pady=10, sticky="ew")
        
        self.boton_grafico_area = tk.Button(self, text="Gráfico de Área", command=lambda: Graficos.mostrar_grafico("area"))
        self.boton_grafico_area.grid(row=1, column=3, padx=10, pady=10, sticky="ew")

        # Fila 3: los últimos 4 botones (centrados en la misma forma)
        self.boton_grafico_treemap = tk.Button(self, text="Gráfico de Treemap", command=lambda: Graficos.mostrar_grafico("treemap"))
        self.boton_grafico_treemap.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.boton_grafico_franja = tk.Button(self, text="Gráfico de Franja", command=lambda: Graficos.mostrar_grafico("franja"))
        self.boton_grafico_franja.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.boton_grafico_enjambre = tk.Button(self, text="Gráfico de Enjambre", command=lambda: Graficos.mostrar_grafico("enjambre"))
        self.boton_grafico_enjambre.grid(row=2, column=2, padx=10, pady=10, sticky="ew")

        self.boton_exportar_excel = tk.Button(self, text="Exportar a Excel", command=self.exportar_excel)
        self.boton_exportar_excel.grid(row=2, column=3, padx=10, pady=10, sticky="ew")


        # Expandir las filas para que el diseño sea más responsivo
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
    
    def exportar_excel(self):
        """Exporta el contenido de la base de datos a un archivo Excel"""
        try:
            # Obtén los datos de la base de datos
            datos = CrudEncuestas.leer_encuestas()

            # Define los nombres de las columnas
            columnas = [
                "idEncuesta", "edad", "sexo", "bebidasSemana",
                "cervezasSemana", "bebidasFinSemana", "bebidasDestiladasSemana",
                "vinosSemana", "perdidasControl", "diversionDependenciaAlcohol",
                "problemasDigestivos", "tensionAlta", "dolorCabeza"
            ]

            # Crea un DataFrame a partir de los datos
            df = pd.DataFrame(datos, columns=columnas)

            # Exporta el DataFrame a un archivo Excel
            df.to_excel("encuestas_exportadas.xlsx", index=False, engine='openpyxl')

            # Muestra un mensaje de éxito
            messagebox.showinfo("Éxito", "Datos exportados correctamente a 'encuestas_exportadas.xlsx'")

        except Exception as e:
            # Maneja errores y muestra un mensaje al usuario
            messagebox.showerror("Error", f"Error al exportar los datos: {e}")


    def mostrar_crear(self):
        """Muestra la pantalla para crear una encuesta"""
        self.limpiar_ventana()

        self.titulo = tk.Label(self, text="Crear Encuesta")
        self.titulo.pack(pady=10)

        # Función de validación para solo permitir números
        def solo_numeros(P):
            if P == "" or P.isdigit():
                return True
            else:
                return False

        # Registrar validación para entradas numéricas
        validate_numeros = self.register(solo_numeros)

        # ID Encuesta (solo números)
        self.idEncuesta_label = tk.Label(self, text="ID Encuesta")
        self.idEncuesta_label.pack()
        self.idEncuesta_entry = tk.Entry(self, validate="key", validatecommand=(validate_numeros, "%P"))
        self.idEncuesta_entry.pack()

        # Edad (solo números)
        self.edad_label = tk.Label(self, text="Edad")
        self.edad_label.pack()
        self.edad_entry = tk.Entry(self, validate="key", validatecommand=(validate_numeros, "%P"))
        self.edad_entry.pack()

        # Sexo
        self.sexo_label = tk.Label(self, text="Sexo")
        self.sexo_label.pack()
        self.sexo_var = tk.StringVar(self)
        self.sexo_var.set("")  
        self.sexo_entry = ttk.OptionMenu(self, self.sexo_var, "", "Hombre", "Mujer")
        self.sexo_entry.pack()


        # Bebidas por Semana (solo números)
        self.bebidasSemana_label = tk.Label(self, text="Bebidas por Semana")
        self.bebidasSemana_label.pack()
        self.bebidasSemana_entry = tk.Entry(self, validate="key", validatecommand=(validate_numeros, "%P"))
        self.bebidasSemana_entry.pack()

        # Cervezas por Semana (solo números)
        self.cervezasSemana_label = tk.Label(self, text="Cervezas por Semana")
        self.cervezasSemana_label.pack()
        self.cervezasSemana_entry = tk.Entry(self, validate="key", validatecommand=(validate_numeros, "%P"))
        self.cervezasSemana_entry.pack()

        # Bebidas Fin de Semana (solo números)
        self.bebidasFinSemana_label = tk.Label(self, text="Bebidas Fin de Semana")
        self.bebidasFinSemana_label.pack()
        self.bebidasFinSemana_entry = tk.Entry(self, validate="key", validatecommand=(validate_numeros, "%P"))
        self.bebidasFinSemana_entry.pack()

        # Bebidas Destiladas por Semana (solo números)
        self.bebidasDestiladasSemana_label = tk.Label(self, text="Bebidas Destiladas por Semana")
        self.bebidasDestiladasSemana_label.pack()
        self.bebidasDestiladasSemana_entry = tk.Entry(self, validate="key", validatecommand=(validate_numeros, "%P"))
        self.bebidasDestiladasSemana_entry.pack()

        # Vinos por Semana (solo números)
        self.vinosSemana_label = tk.Label(self, text="Vinos por Semana")
        self.vinosSemana_label.pack()
        self.vinosSemana_entry = tk.Entry(self, validate="key", validatecommand=(validate_numeros, "%P"))
        self.vinosSemana_entry.pack()

        # Pérdidas de Control
        self.perdidasControl_label = tk.Label(self, text="Pérdidas de Control")
        self.perdidasControl_label.pack()
        self.perdidasControl_entry = tk.Entry(self, validate="key", validatecommand=(validate_numeros, "%P"))
        self.perdidasControl_entry.pack()

        # Diversión Dependencia Alcohol
        self.diversionDependenciaAlcohol_label = tk.Label(self, text="Diversión Dependencia Alcohol")
        self.diversionDependenciaAlcohol_label.pack()
        self.diversionDependenciaAlcohol_var = tk.StringVar(self)
        self.diversionDependenciaAlcohol_var.set("")  # Valor por defecto
        self.diversionDependenciaAlcohol_entry = ttk.OptionMenu(self, self.diversionDependenciaAlcohol_var, "", "Sí", "No")
        self.diversionDependenciaAlcohol_entry.pack()

        # Problemas Digestivos 
        self.problemasDigestivos_label = tk.Label(self, text="Problemas Digestivos")
        self.problemasDigestivos_label.pack()
        self.problemasDigestivos_var = tk.StringVar(self)
        self.problemasDigestivos_var.set("")  
        self.problemasDigestivos_entry = ttk.OptionMenu(self, self.problemasDigestivos_var, "", "Sí", "No")
        self.problemasDigestivos_entry.pack()

        # Tensión Alta 
        self.tensionAlta_label = tk.Label(self, text="Tensión Alta")
        self.tensionAlta_label.pack()
        self.tensionAlta_var = tk.StringVar(self)
        self.tensionAlta_var.set("")  
        self.tensionAlta_entry = ttk.OptionMenu(self, self.tensionAlta_var, "", "Sí", "No", "No lo se")
        self.tensionAlta_entry.pack()

        # Dolor de Cabeza 
        self.dolorCabeza_label = tk.Label(self, text="Dolor de Cabeza")
        self.dolorCabeza_label.pack()
        self.dolorCabeza_var = tk.StringVar(self)
        self.dolorCabeza_var.set("")  
        self.dolorCabeza_entry = ttk.OptionMenu(self, self.dolorCabeza_var, "","Nunca", "Alguna vez", "A menudo", "Muy a menudo")
        self.dolorCabeza_entry.pack()

        # Botón para guardar la encuesta
        self.boton_guardar = tk.Button(self, text="Guardar Encuesta", command=self.guardar_encuesta)
        self.boton_guardar.pack(pady=10)

        # Botón para volver a la pantalla principal
        self.boton_volver = tk.Button(self, text="Volver", command=self.volver_pantalla_principal)
        self.boton_volver.pack(pady=10)

    def guardar_encuesta(self):
        """Guarda la encuesta en la base de datos"""
        try:
            # Recoge los datos de los campos de entrada y los convierte al tipo adecuado
            encuesta = (
                int(self.idEncuesta_entry.get()),  # idEncuesta (int)
                int(self.edad_entry.get()),        # edad (int)
                self.sexo_var.get(),             # Sexo (varchar(7))
                int(self.bebidasSemana_entry.get()),  # BebidasSemana (int)
                int(self.cervezasSemana_entry.get()), # CervezasSemana (int)
                int(self.bebidasFinSemana_entry.get()), # BebidasFinSemana (int)
                int(self.bebidasDestiladasSemana_entry.get()), # BebidasDestiladasSemana (int)
                int(self.vinosSemana_entry.get()),  # VinosSemana (int)
                int(self.perdidasControl_entry.get()), # PerdidasControl (int)
                self.diversionDependenciaAlcohol_var.get(), # DiversionDependenciaAlcohol (char(2))
                self.problemasDigestivos_var.get(),  # ProblemasDigestivos (char(2))
                self.tensionAlta_var.get(),          # TensionAlta (char(12))
                self.dolorCabeza_var.get()           # DolorCabeza (char(12))
            )

            # Llama al método de CRUD para guardar la encuesta en la base de datos
            CrudEncuestas.crear_encuesta(encuesta)

            # Muestra un mensaje de éxito
            messagebox.showinfo("Éxito", "Encuesta guardada correctamente")

            # Vuelve a la pantalla principal (debes haber definido este método)
            self.volver_pantalla_principal()
        except Exception as e:
            # Maneja errores y muestra un mensaje al usuario
            messagebox.showerror("Error", f"Error al guardar la encuesta: {e}")

    def mostrar_leer(self):
        """Muestra la pantalla para leer encuestas"""
        self.limpiar_ventana()
        self.titulo = tk.Label(self, text="Leer Encuestas")
        self.titulo.pack(pady=10)

        # Crear el Treeview (tabla) para mostrar los resultados de las encuestas
        self.tree = ttk.Treeview(self, columns=("idEncuesta", "edad", "Sexo", "BebidasSemana", "CervezasSemana",
                                                 "BebidasFinSemana", "BebidasDestiladasSemana", "VinosSemana",
                                                 "PerdidasControl", "DiversionDependenciaAlcohol", "ProblemasDigestivos",
                                                 "TensionAlta", "DolorCabeza"), show="headings")
        
        # Definir las cabeceras de las columnas
        self.tree.heading("idEncuesta", text="idEncuesta", command=lambda: self.ordenar_columnas("idEncuesta"))
        self.tree.heading("edad", text="Edad", command=lambda: self.ordenar_columnas("edad"))
        self.tree.heading("Sexo", text="Sexo", command=lambda: self.ordenar_columnas("Sexo"))
        self.tree.heading("BebidasSemana", text="BebidasSemana", command=lambda: self.ordenar_columnas("BebidasSemana"))
        self.tree.heading("CervezasSemana", text="CervezasSemana", command=lambda: self.ordenar_columnas("CervezasSemana"))
        self.tree.heading("BebidasFinSemana", text="BebidasFinSemana", command=lambda: self.ordenar_columnas("BebidasFinSemana"))
        self.tree.heading("BebidasDestiladasSemana", text="BebidasDestiladasSemana", command=lambda: self.ordenar_columnas("BebidasDestiladasSemana"))
        self.tree.heading("VinosSemana", text="VinosSemana", command=lambda: self.ordenar_columnas("VinosSemana"))
        self.tree.heading("PerdidasControl", text="PerdidasControl", command=lambda: self.ordenar_columnas("PerdidasControl"))
        self.tree.heading("DiversionDependenciaAlcohol", text="DiversionDependenciaAlcohol", command=lambda: self.ordenar_columnas("DiversionDependenciaAlcohol"))
        self.tree.heading("ProblemasDigestivos", text="ProblemasDigestivos", command=lambda: self.ordenar_columnas("ProblemasDigestivos"))
        self.tree.heading("TensionAlta", text="TensionAlta", command=lambda: self.ordenar_columnas("TensionAlta"))
        self.tree.heading("DolorCabeza", text="DolorCabeza", command=lambda: self.ordenar_columnas("DolorCabeza"))

        # Configurar el ancho de las columnas (opcional)
        self.tree.column("idEncuesta", width=80)
        self.tree.column("edad", width=80)
        self.tree.column("Sexo", width=100)
        self.tree.column("BebidasSemana", width=100)
        self.tree.column("CervezasSemana", width=100)
        self.tree.column("BebidasFinSemana", width=100)
        self.tree.column("BebidasDestiladasSemana", width=150)
        self.tree.column("VinosSemana", width=100)
        self.tree.column("PerdidasControl", width=120)
        self.tree.column("DiversionDependenciaAlcohol", width=180)
        self.tree.column("ProblemasDigestivos", width=150)
        self.tree.column("TensionAlta", width=150)
        self.tree.column("DolorCabeza", width=150)

        # Mostrar los resultados en el Treeview
        encuestas = CrudEncuestas.leer_encuestas()
        for encuesta in encuestas:
            # Insertar cada encuesta en la tabla
            self.tree.insert("", tk.END, values=encuesta)

        # Empacar el Treeview en la ventana
        self.tree.pack(pady=10)

        # Crear un marco para las dos columnas de filtros
        frame_filtros = tk.Frame(self)
        frame_filtros.pack(pady=10)

        # Crear un marco para la primera columna de filtros
        columna1 = tk.Frame(frame_filtros)
        columna1.grid(row=0, column=0, padx=10)

        # Crear un marco para la segunda columna de filtros
        columna2 = tk.Frame(frame_filtros)
        columna2.grid(row=0, column=1, padx=10)

        def validar_numero(input_text):
            # Verifica si el texto ingresado es un número
            if input_text == "" or input_text.isdigit():
                return True
            else:
                return False

        # Crear una validación de entrada
        validacion = self.register(validar_numero)

        # Etiqueta para ID Encuesta
        self.filtro_label_idEncuesta = tk.Label(columna1, text="Filtrar por ID Encuesta:")
        self.filtro_label_idEncuesta.grid(row=0, column=0, pady=5)
        # Campo de entrada para ID Encuesta con validación para números
        self.filtro_idEncuesta = tk.Entry(columna1, validate="key", validatecommand=(validacion, "%P"))
        self.filtro_idEncuesta.grid(row=1, column=0, pady=5)

        # Etiqueta y campo de entrada para "Edad"
        self.filtro_label_edad = tk.Label(columna1, text="Filtrar por Edad:")
        self.filtro_label_edad.grid(row=2, column=0, pady=5)
        self.filtro_edad = tk.Entry(columna1, validate="key", validatecommand=(validacion, "%P"))
        self.filtro_edad.grid(row=3, column=0, pady=5)

        # Etiqueta y campo de entrada para "Bebidas Semana"
        self.filtro_label_bebidasSemana = tk.Label(columna1, text="Filtrar por Bebidas Semana:")
        self.filtro_label_bebidasSemana.grid(row=4, column=0, pady=5)
        self.filtro_bebidasSemana = tk.Entry(columna1, validate="key", validatecommand=(validacion, "%P"))
        self.filtro_bebidasSemana.grid(row=5, column=0, pady=5)

        # Etiqueta y campo de entrada para "Bebidas Destiladas Semana"
        self.filtro_label_bebidasDestiladasSemana = tk.Label(columna1, text="Filtrar por Bebidas Destiladas Semana:")
        self.filtro_label_bebidasDestiladasSemana.grid(row=6, column=0, pady=5)
        self.filtro_bebidasDestiladasSemana = tk.Entry(columna1, validate="key", validatecommand=(validacion, "%P"))
        self.filtro_bebidasDestiladasSemana.grid(row=7, column=0, pady=5)

        # Etiqueta y campo de entrada para "Perdidas Control"
        self.filtro_label_perdidasControl = tk.Label(columna1, text="Filtrar por Perdidas Control:")
        self.filtro_label_perdidasControl.grid(row=8, column=0, pady=5)
        self.filtro_perdidasControl = tk.Entry(columna1, validate="key", validatecommand=(validacion, "%P"))
        self.filtro_perdidasControl.grid(row=9, column=0, pady=5)

        # Filtros de búsqueda - Columna 2

        # Etiqueta para el filtro de Sexo
        self.filtro_label_sexo = tk.Label(columna2, text="Filtrar por Sexo:")
        self.filtro_label_sexo.grid(row=0, column=0, pady=5)

        # Variable para el selector
        self.sexo_var = tk.StringVar(columna2)
        self.sexo_var.set("")  # Valor inicial vacío

        # Selector (OptionMenu) para elegir entre "Hombre" o "Mujer"
        self.filtro_sexo = ttk.OptionMenu(columna2, self.sexo_var, "", "Hombre", "Mujer")
        self.filtro_sexo.grid(row=1, column=0, pady=5)


        # Etiqueta y campo de entrada para "Cervezas Semana"
        self.filtro_label_cervezasSemana = tk.Label(columna2, text="Filtrar por Cervezas Semana:")
        self.filtro_label_cervezasSemana.grid(row=2, column=0, pady=5)
        self.filtro_cervezasSemana = tk.Entry(columna2, validate="key", validatecommand=(validacion, "%P"))
        self.filtro_cervezasSemana.grid(row=3, column=0, pady=5)

        # Etiqueta y campo de entrada para "Bebidas Fin Semana"
        self.filtro_label_bebidasFinSemana = tk.Label(columna2, text="Filtrar por Bebidas Fin Semana:")
        self.filtro_label_bebidasFinSemana.grid(row=4, column=0, pady=5)
        self.filtro_bebidasFinSemana = tk.Entry(columna2, validate="key", validatecommand=(validacion, "%P"))
        self.filtro_bebidasFinSemana.grid(row=5, column=0, pady=5)

        # Etiqueta y campo de entrada para "Vinos Semana"
        self.filtro_label_vinosSemana = tk.Label(columna2, text="Filtrar por Vinos Semana:")
        self.filtro_label_vinosSemana.grid(row=6, column=0, pady=5)
        self.filtro_vinosSemana = tk.Entry(columna2, validate="key", validatecommand=(validacion, "%P"))
        self.filtro_vinosSemana.grid(row=7, column=0, pady=5)

        # Etiqueta para el filtro de Diversión/Dependencia Alcohol
        self.filtro_label_diversionDependenciaAlcohol = tk.Label(columna2, text="Filtrar por Diversión/Dependencia Alcohol:")
        self.filtro_label_diversionDependenciaAlcohol.grid(row=8, column=0, pady=5)
 
        self.diversionDependenciaAlcohol_var = tk.StringVar(columna2)
        self.diversionDependenciaAlcohol_var.set("") 
        self.filtro_diversionDependenciaAlcohol = ttk.OptionMenu(columna2, self.diversionDependenciaAlcohol_var, "", "Sí", "No")
        self.filtro_diversionDependenciaAlcohol.grid(row=9, column=0, pady=5)


        # Botón para aplicar los filtros
        self.boton_filtrar = tk.Button(self, text="Filtrar", command=self.aplicar_filtro)
        self.boton_filtrar.pack(pady=10)

        # Botón para volver
        self.boton_volver = tk.Button(self, text="Volver", command=self.volver_pantalla_principal)
        self.boton_volver.pack(pady=10)

    def ordenar_columnas(self, columna):
        """Ordena las filas del Treeview por la columna seleccionada"""
        # Obtener el índice de la columna
        items = [(self.tree.set(item, columna), item) for item in self.tree.get_children('')]
        items.sort()  # Ordenar por el valor de la columna
        for index, item in enumerate(items):
            self.tree.move(item[1], '', index)

    def aplicar_filtro(self):
        """Aplica el filtro basado en los valores ingresados en las entradas"""
        # Recoger los valores de los filtros
        filtro_idEncuesta = self.filtro_idEncuesta.get()
        filtro_edad = self.filtro_edad.get()
        filtro_sexo = self.sexo_var.get()
        filtro_bebidasSemana = self.filtro_bebidasSemana.get()
        filtro_cervezasSemana = self.filtro_cervezasSemana.get()
        filtro_bebidasFinSemana = self.filtro_bebidasFinSemana.get()
        filtro_bebidasDestiladasSemana = self.filtro_bebidasDestiladasSemana.get()
        filtro_vinosSemana = self.filtro_vinosSemana.get()
        filtro_perdidasControl = self.filtro_perdidasControl.get()
        filtro_diversionDependenciaAlcohol = self.diversionDependenciaAlcohol_var.get()

        encuestas = CrudEncuestas.leer_encuestas()
        self.tree.delete(*self.tree.get_children())  # Limpiar los registros actuales

        # Filtrar las encuestas
        for encuesta in encuestas:
            # Filtrar por cada campo
            if (filtro_idEncuesta in str(encuesta[0]) and
                filtro_edad in str(encuesta[1]) and
                filtro_sexo in str(encuesta[2]) and
                filtro_bebidasSemana in str(encuesta[3]) and
                filtro_cervezasSemana in str(encuesta[4]) and
                filtro_bebidasFinSemana in str(encuesta[5]) and
                filtro_bebidasDestiladasSemana in str(encuesta[6]) and
                filtro_vinosSemana in str(encuesta[7]) and
                filtro_perdidasControl in str(encuesta[8]) and
                filtro_diversionDependenciaAlcohol in str(encuesta[9])):
                self.tree.insert("", tk.END, values=encuesta)
            


    def limpiar_ventana(self):
        """Limpia la ventana actual (opcional, si es necesario)"""
        for widget in self.winfo_children():
            widget.destroy()

    def volver_pantalla_principal(self):
        """Vuelve a la pantalla principal (opcional, si es necesario)"""
        pass

    def mostrar_actualizar(self):
        """Muestra la pantalla para actualizar una encuesta"""
        self.limpiar_ventana()

        self.titulo = tk.Label(self, text="Actualizar Encuesta")
        self.titulo.pack(pady=10)

        # Función de validación para solo permitir números
        def solo_numeros(P):
            if P == "" or P.isdigit():
                return True
            else:
                return False

        # Registrar validación para entradas numéricas
        validate_numeros = self.register(solo_numeros)

        # ID Encuesta (solo números)
        self.idEncuesta_label = tk.Label(self, text="ID Encuesta")
        self.idEncuesta_label.pack()
        self.idEncuesta_entry = tk.Entry(self, validate="key", validatecommand=(validate_numeros, "%P"))
        self.idEncuesta_entry.pack()

        # Edad (solo números)
        self.edad_label = tk.Label(self, text="Edad")
        self.edad_label.pack()
        self.edad_entry = tk.Entry(self, validate="key", validatecommand=(validate_numeros, "%P"))
        self.edad_entry.pack()

        # Sexo
        self.sexo_label = tk.Label(self, text="Sexo")
        self.sexo_label.pack()
        self.sexo_var = tk.StringVar(self)
        self.sexo_var.set("")  
        self.sexo_entry = ttk.OptionMenu(self, self.sexo_var, "", "Hombre", "Mujer")
        self.sexo_entry.pack()

        # Bebidas por Semana (solo números)
        self.bebidasSemana_label = tk.Label(self, text="Bebidas por Semana")
        self.bebidasSemana_label.pack()
        self.bebidasSemana_entry = tk.Entry(self, validate="key", validatecommand=(validate_numeros, "%P"))
        self.bebidasSemana_entry.pack()

        # Cervezas por Semana (solo números)
        self.cervezasSemana_label = tk.Label(self, text="Cervezas por Semana")
        self.cervezasSemana_label.pack()
        self.cervezasSemana_entry = tk.Entry(self, validate="key", validatecommand=(validate_numeros, "%P"))
        self.cervezasSemana_entry.pack()

        # Bebidas Fin de Semana (solo números)
        self.bebidasFinSemana_label = tk.Label(self, text="Bebidas Fin de Semana")
        self.bebidasFinSemana_label.pack()
        self.bebidasFinSemana_entry = tk.Entry(self, validate="key", validatecommand=(validate_numeros, "%P"))
        self.bebidasFinSemana_entry.pack()

        # Bebidas Destiladas por Semana (solo números)
        self.bebidasDestiladasSemana_label = tk.Label(self, text="Bebidas Destiladas por Semana")
        self.bebidasDestiladasSemana_label.pack()
        self.bebidasDestiladasSemana_entry = tk.Entry(self, validate="key", validatecommand=(validate_numeros, "%P"))
        self.bebidasDestiladasSemana_entry.pack()

        # Vinos por Semana (solo números)
        self.vinosSemana_label = tk.Label(self, text="Vinos por Semana")
        self.vinosSemana_label.pack()
        self.vinosSemana_entry = tk.Entry(self, validate="key", validatecommand=(validate_numeros, "%P"))
        self.vinosSemana_entry.pack()

        # Pérdidas de Control
        self.perdidasControl_label = tk.Label(self, text="Pérdidas de Control")
        self.perdidasControl_label.pack()
        self.perdidasControl_entry = tk.Entry(self, validate="key", validatecommand=(validate_numeros, "%P"))
        self.perdidasControl_entry.pack()

        # Diversión Dependencia Alcohol
        self.diversionDependenciaAlcohol_label = tk.Label(self, text="Diversión Dependencia Alcohol")
        self.diversionDependenciaAlcohol_label.pack()
        self.diversionDependenciaAlcohol_var = tk.StringVar(self)
        self.diversionDependenciaAlcohol_var.set("")  # Valor por defecto
        self.diversionDependenciaAlcohol_entry = ttk.OptionMenu(self, self.diversionDependenciaAlcohol_var, "", "Sí", "No")
        self.diversionDependenciaAlcohol_entry.pack()

        # Problemas Digestivos 
        self.problemasDigestivos_label = tk.Label(self, text="Problemas Digestivos")
        self.problemasDigestivos_label.pack()
        self.problemasDigestivos_var = tk.StringVar(self)
        self.problemasDigestivos_var.set("")  
        self.problemasDigestivos_entry = ttk.OptionMenu(self, self.problemasDigestivos_var, "", "Sí", "No")
        self.problemasDigestivos_entry.pack()

        # Tensión Alta 
        self.tensionAlta_label = tk.Label(self, text="Tensión Alta")
        self.tensionAlta_label.pack()
        self.tensionAlta_var = tk.StringVar(self)
        self.tensionAlta_var.set("")  
        self.tensionAlta_entry = ttk.OptionMenu(self, self.tensionAlta_var, "", "Sí", "No", "No lo se")
        self.tensionAlta_entry.pack()

        # Dolor de Cabeza 
        self.dolorCabeza_label = tk.Label(self, text="Dolor de Cabeza")
        self.dolorCabeza_label.pack()
        self.dolorCabeza_var = tk.StringVar(self)
        self.dolorCabeza_var.set("")  
        self.dolorCabeza_entry = ttk.OptionMenu(self, self.dolorCabeza_var, "","Nunca", "Alguna vez", "A menudo", "Muy a menudo")
        self.dolorCabeza_entry.pack()

        # Añadir los demás campos de la encuesta
        self.boton_actualizar = tk.Button(self, text="Actualizar Encuesta", command=self.actualizar_encuesta)
        self.boton_actualizar.pack(pady=10)

        # Botón para volver a la pantalla principal
        self.boton_volver = tk.Button(self, text="Volver", command=self.volver_pantalla_principal)
        self.boton_volver.pack(pady=10)

    def actualizar_encuesta(self):
        """Actualiza la encuesta en la base de datos"""
        idEncuesta = int(self.idEncuesta_entry.get())
        nuevos_datos = (
            int(self.edad_entry.get()),         # edad (int)
            self.sexo_var.get(),             # Sexo (varchar(7))
            int(self.bebidasSemana_entry.get()),  # BebidasSemana (int)
            int(self.cervezasSemana_entry.get()), # CervezasSemana (int)
            int(self.bebidasFinSemana_entry.get()), # BebidasFinSemana (int)
            int(self.bebidasDestiladasSemana_entry.get()), # BebidasDestiladasSemana (int)
            int(self.vinosSemana_entry.get()),  # VinosSemana (int)
            int(self.perdidasControl_entry.get()), # PerdidasControl (int)
            self.diversionDependenciaAlcohol_var.get(), # DiversionDependenciaAlcohol (char(2))
            self.problemasDigestivos_var.get(),  # ProblemasDigestivos (char(2))
            self.tensionAlta_var.get(),          # TensionAlta (char(12))
            self.dolorCabeza_var.get()           # DolorCabeza (char(12))
        )
        CrudEncuestas.actualizar_encuesta(idEncuesta, nuevos_datos)
        messagebox.showinfo("Éxito el regitro", f"El registro con ID: {idEncuesta} ha diso actualiado")
        self.volver_pantalla_principal()

    def mostrar_borrar(self):
        """Muestra la pantalla para borrar una encuesta"""
        self.limpiar_ventana()
        self.titulo = tk.Label(self, text="Borrar Encuesta")
        self.titulo.pack(pady=10)

        self.idEncuesta_label = tk.Label(self, text="ID Encuesta")
        self.idEncuesta_label.pack()
        self.idEncuesta_entry = tk.Entry(self)
        self.idEncuesta_entry.pack()

        self.boton_borrar = tk.Button(self, text="Borrar Encuesta", command=self.borrar_encuesta)
        self.boton_borrar.pack(pady=10)

        # Botón para volver a la pantalla principal
        self.boton_volver = tk.Button(self, text="Volver", command=self.volver_pantalla_principal)
        self.boton_volver.pack(pady=10)

    def borrar_encuesta(self):
        """Borra la encuesta en la base de datos"""
        idEncuesta = int(self.idEncuesta_entry.get())
        CrudEncuestas.borrar_encuesta(idEncuesta)
        messagebox.showinfo("Éxito al borrar el registro", f"El registro con id: {idEncuesta} ha sido eliminado")
        self.volver_pantalla_principal()

    def limpiar_ventana(self):
        """Limpia la ventana actual antes de cargar una nueva pantalla"""
        for widget in self.winfo_children():
            widget.destroy()

    def volver_pantalla_principal(self):
        """Vuelve a la pantalla principal"""
        self.limpiar_ventana()
        self.crear_pantalla_principal()

