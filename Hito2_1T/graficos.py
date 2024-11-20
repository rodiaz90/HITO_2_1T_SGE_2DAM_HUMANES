import matplotlib.pyplot as plt
import pandas as pd
import squarify
import seaborn as sns
from tkinter import messagebox
from crud import CrudEncuestas  # Importar CrudEncuestas

class Graficos:
    @staticmethod
    def mostrar_grafico(tipo="barras"):
        encuestas = CrudEncuestas.leer_encuestas()  # Usar el método de CrudEncuestas
        if encuestas:
            df = pd.DataFrame(encuestas, columns=["ID Encuesta", "Edad", "Sexo", "Bebidas Semana",
                                                  "Cervezas Semana", "Bebidas Fin Semana",
                                                  "Bebidas Destiladas Semana", "Vinos Semana",
                                                  "Pérdidas Control", "Diversión",
                                                  "Problemas Digestivos", "Tensión Alta", "Dolor de Cabeza"])
            plt.close("all")
            plt.figure(figsize=(10, 6))

            if tipo == "barras":
                plt.bar(df["Edad"], df["Bebidas Semana"], color='blue')
                plt.xlabel("Edad")
                plt.ylabel("Bebidas Semana")
                plt.title("Consumo de Bebidas por Semana según la Edad")

            elif tipo == "pastel":
                df_grouped = df.groupby("Sexo")["Bebidas Destiladas Semana"].sum()
                plt.pie(df_grouped, labels=df_grouped.index, autopct='%1.1f%%', startangle=90)
                plt.title("Distribución de Bebidas Destiladas por Sexo")

            elif tipo == "lineas":
                # Filtrar los datos para hombres y mujeres
                df_hombres = df[df["Sexo"] == "Hombre"]
                df_mujeres = df[df["Sexo"] == "Mujer"]
                
                # Agrupar por Edad y calcular la media de Bebidas Semana para hombres y mujeres
                df_hombres_grouped = df_hombres.groupby("Edad")["Bebidas Semana"].mean().reset_index()
                df_mujeres_grouped = df_mujeres.groupby("Edad")["Bebidas Semana"].mean().reset_index()
                
                # Graficar la media de Bebidas Semana por Edad para hombres (en azul) y mujeres (en rojo)
                plt.plot(df_hombres_grouped["Edad"], df_hombres_grouped["Bebidas Semana"], marker='o', color='blue', label='Hombres')
                plt.plot(df_mujeres_grouped["Edad"], df_mujeres_grouped["Bebidas Semana"], marker='o', color='red', label='Mujeres')
                
                # Etiquetas y título
                plt.xlabel("Edad")  # Etiqueta en el eje X
                plt.ylabel("Media de Bebidas Semana")  # Etiqueta en el eje Y
                plt.title("Consumo Promedio de Bebidas por Semana según la Edad")  # Título de la gráfica
                plt.legend()  # Agregar leyenda para diferenciar las líneas


            elif tipo == "area":
                df_mujeres = df[df["Sexo"] == "Mujer"]
                plt.scatter(df_mujeres["Bebidas Semana"], df_mujeres["Cervezas Semana"], color="purple", alpha=0.6)
                plt.xlabel("Bebidas por Semana")
                plt.ylabel("Cervezas por Semana")
                plt.title("Comparación de Bebidas por Semana vs. Cervezas por Semana (Mujeres)")
                plt.grid(visible=True, linestyle="--", alpha=0.5)

            elif tipo == "treemap":
                df_grouped = df.groupby("Sexo")["Bebidas Destiladas Semana"].sum()
                squarify.plot(sizes=df_grouped, label=df_grouped.index, alpha=0.7)
                plt.title("Mapa de Árbol: Bebidas Destiladas por Sexo")
                plt.axis('off')

            elif tipo == "franja":
                plt.close('all')
                df_grouped = df.groupby("Sexo")[["Bebidas Semana", "Cervezas Semana"]].sum()
                df_grouped.plot(kind="barh", stacked=True)
                plt.xlabel("Consumo Total")
                plt.title("Parcelas en Franja: Consumo de Bebidas por Sexo")
                plt.show() 

            elif tipo == "enjambre":
                sns.swarmplot(data=df, x="Sexo", y="Bebidas Semana", hue="Sexo", palette="Set2")
                plt.title("Gráfico de Enjambre: Consumo de Bebidas por Sexo")
            plt.show()
        else:
            messagebox.showwarning("Gráfico", "No hay datos para mostrar en el gráfico.")
