
🎯 README - Proyecto de Gestión de Encuestas de Consumo de Alcohol
🚀 Descripción del Proyecto
Este proyecto es una aplicación desarrollada con Python utilizando Tkinter para la interfaz gráfica de usuario (GUI) y MySQL para gestionar una base de datos relacionada con el consumo de alcohol y sus efectos sobre la salud. El sistema permite realizar operaciones CRUD sobre las encuestas de los pacientes, visualizar los resultados mediante gráficos, y exportar datos a Excel para su análisis.

Objetivos Principales:
Interfaz de Usuario (Tkinter): Permitir la visualización y manipulación de los datos relacionados con el consumo de alcohol y los indicadores de salud.
Conexión con MySQL: Establecer una conexión con una base de datos de MySQL para realizar operaciones CRUD.
Consultas y Ordenación: Permitir la consulta y ordenación de los resultados de las encuestas de los pacientes según diferentes criterios.
Visualización Gráfica: Mostrar los resultados de las consultas en gráficos de barras, pastel, y líneas.
Exportación a Excel (Opcional): Permitir exportar los resultados a un archivo Excel.
🛠️ Requisitos
Requisitos del Sistema:
Antes de ejecutar el proyecto, asegúrate de tener instalado lo siguiente:

Python 3.x: El proyecto está desarrollado en Python, por lo que necesitas tenerlo instalado.
Tkinter: Utilizado para crear la interfaz de usuario.
MySQL: Se necesita MySQL para gestionar la base de datos.
Librerías adicionales de Python:
mysql-connector-python para la conexión a MySQL.
matplotlib para la visualización de gráficos.
pandas para el manejo de datos y exportación a Excel.
Instalación de Dependencias:
🐍 Instalar Tkinter:
Tkinter debería estar incluido por defecto con tu instalación de Python, pero si no es así, puedes instalarlo ejecutando:

sudo apt-get install python3-tk

  🛢️ Instalar MySQL:
Descarga e instala MySQL Community Server desde aquí.
Crea la base de datos utilizando el script SQL proporcionado para generar la tabla de encuestas.
📦 Instalar Librerías de Python:
Para instalar las librerías necesarias, ejecuta el siguiente comando en tu terminal:

pip install mysql-connector-python matplotlib pandas

Conexión con MySQL:
Crea una base de datos llamada clinica (o el nombre que prefieras) en MySQL.
Ejecuta el siguiente script SQL para crear la tabla de encuestas:

CREATE TABLE encuestas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    edad INT,
    sexo VARCHAR(10),
    consumo_semanal INT,
    problemas_salud TEXT
);

Edita el archivo de configuración de la base de datos en tu proyecto para establecer la conexión:

import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",  # Cambia el usuario si es necesario
    password="password",  # Cambia la contraseña si es necesario
    database="clinica"
)

📝 Uso del Proyecto
1. Ejecutar la Aplicación:
Para iniciar la aplicación, simplemente ejecuta el archivo principal:

python main.py

Esto abrirá la ventana de la interfaz gráfica de usuario donde podrás interactuar con el sistema.

2. Operaciones CRUD:
Crear:
Agrega nuevas encuestas con los campos de edad, sexo, consumo semanal, y problemas de salud.
Los datos se guardarán automáticamente en la base de datos.
Leer:
Visualiza las encuestas existentes con un formato organizado en la interfaz.
Actualizar:
Modifica los registros de las encuestas de los pacientes (por ejemplo, cambiar el consumo de alcohol o los problemas de salud reportados).
Eliminar:
Elimina registros con un mensaje de confirmación para evitar eliminaciones accidentales.
3. Consultas y Filtros:
Ordenación: Puedes ordenar las encuestas por edad, sexo, consumo semanal, entre otros campos.
Filtros Condicionales: Filtra por criterios específicos como:
Encuestados con un alto consumo de alcohol.
Personas que han perdido el control de su consumo en más de 3 ocasiones.
4. Visualización de Gráficos:
Puedes visualizar los resultados de las consultas mediante gráficos interactivos. Algunos ejemplos son:

Gráfico de barras para mostrar el consumo promedio de alcohol por grupo de edad.
Gráfico de pastel para ver la distribución de los problemas de salud.
Gráfico de líneas para analizar la correlación entre consumo de alcohol y problemas de salud.
Para visualizar los gráficos, simplemente selecciona la consulta deseada y presiona el botón de "Ver Gráfico".

5. Exportación a Excel (Opcional):
El proyecto incluye una funcionalidad para exportar los resultados de las encuestas a un archivo Excel. Esto es útil para un análisis más profundo de los datos.

Para exportar los datos:

Realiza una consulta.
Haz clic en el botón "Exportar a Excel".
El archivo será guardado en tu directorio de trabajo.

import pandas as pd

def exportar_a_excel():
    query = "SELECT * FROM encuestas"
    cursor.execute(query)
    result = cursor.fetchall()
    
    # Convertir a DataFrame y exportar
    df = pd.DataFrame(result, columns=["ID", "Edad", "Sexo", "Consumo Semanal", "Problemas de Salud"])
    df.to_excel("encuestas.xlsx", index=False)


🧑‍💻 Contribuciones
Si deseas contribuir a este proyecto, siéntete libre de realizar un fork y hacer un pull request con tus cambios. Asegúrate de que el código siga las pautas de estilo y sea completamente funcional.

📜 Licencia
Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

🔧 Tecnologías Utilizadas
Python 3.x
Tkinter (para la interfaz gráfica)
MySQL (para la base de datos)
Matplotlib (para gráficos)
Pandas (para exportar a Excel)
🌐 Contactos
Si tienes alguna pregunta o sugerencia, no dudes en contactarme.

📧 Correo Electrónico: tu.email@example.com

⭐ Agradecimientos
Gracias por revisar este proyecto. ¡Espero que sea útil para ti!  
