import matplotlib.pyplot as plt

class PlotManager:
    @staticmethod
    def grafico_barras(datos, campo):
        valores = [dato[campo] for dato in datos]
        etiquetas = [dato[0] for dato in datos]  # Asumiendo que el ID es el primer campo
        plt.bar(etiquetas, valores)
        plt.xlabel("Encuestados")
        plt.ylabel(campo)
        plt.title(f"Gráfico de barras - {campo}")
        plt.show()

    @staticmethod
    def grafico_pastel(datos, campo):
        valores = [dato[campo] for dato in datos]
        etiquetas = [dato[0] for dato in datos]
        plt.pie(valores, labels=etiquetas, autopct='%1.1f%%')
        plt.title(f"Gráfico de pastel - {campo}")
        plt.show()
