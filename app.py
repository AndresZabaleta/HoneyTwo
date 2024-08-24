from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from io import BytesIO
import base64

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/formulario")
def formulario():
    conn = sqlite3.connect("apicultores.db")
    c = conn.cursor()
    c.execute("SELECT * FROM datos_apicultores")
    datos = c.fetchall()
    conn.close()
    return render_template("formulario.html", datos=datos)



@app.route("/submit_form", methods=["POST"])
def submit_form():
    # Obtener los datos del formulario
    fecha = request.form["fecha"]
    numcol = request.form["numcol"]
    ubicacion = request.form["ubicacion"]
    estacion = request.form["estacion"]
    estsalud = request.form["estsalud"]
    polen = request.form["polen"]
    temperatura = request.form["temperatura"]
    humedad = request.form["humedad"]

    # Conectar a la base de datos
    conn = sqlite3.connect("apicultores.db")
    cursor = conn.cursor()

    # Insertar los datos en la base de datos
    cursor.execute(
        """
        INSERT INTO datos_apicultores (fecha, numcol, ubicacion, estacion, estsalud, polen, temperatura, humedad)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
        (fecha, numcol, ubicacion, estacion, estsalud, polen, temperatura, humedad),
    )

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

    return redirect(url_for("formulario"))


###########################################################################################
# def obtener_mejor_momento_para_reactivacion():
#     # Conectar a la base de datos
#     conn = sqlite3.connect("apicultores.db")
#     cursor = conn.cursor()

#     # Consultar los datos relevantes
#     cursor.execute(
#         """
#         SELECT fecha, estacionalidad, estsalud, polen
#         FROM apicultores
#     """
#     )

#     resultados = cursor.fetchall()

#     sugerencias = []

#     for fila in resultados:
#         fecha, estacionalidad, estsalud, polen = fila

#         # Asignar puntuaciones
#         puntos_estacionalidad = asignar_puntuacion_estacionalidad(estacionalidad)
#         puntos_estsalud = asignar_puntuacion_estsalud(estsalud)
#         puntos_polen = asignar_puntuacion_polen(polen)

#         puntuacion_total = puntos_estacionalidad + puntos_estsalud + puntos_polen

#         if puntuacion_total >= 12:  # Umbral para sugerir reactivación
#             sugerencias.append((fecha, puntuacion_total))
#     conn.close()
#     return sugerencias


# def asignar_puntuacion_estacionalidad(estacionalidad):
#     # Asignar puntuaciones basadas en la estacionalidad
#     if estacionalidad.lower() in ["primavera"]:
#         return 5
#     elif estacionalidad.lower() in ["verano"]:
#         return 4
#     elif estacionalidad.lower() in ["otoño"]:
#         return 3
#     else:
#         return 2


# def asignar_puntuacion_estsalud(estsalud):
#     # Asignar puntuaciones basadas en la salud de las colmenas
#     if estsalud.lower() in ["excelente"]:
#         return 5
#     elif estsalud.lower() in ["buena"]:
#         return 4
#     elif estsalud.lower() in ["regular"]:
#         return 3
#     else:
#         return 2


# def asignar_puntuacion_polen(polen):
#     # Asignar puntuaciones basadas en la demanda del polen
#     if polen.lower() in ["alta"]:
#         return 5
#     elif polen.lower() in ["media"]:
#         return 3
#     else:
#         return 1
###########################################################################################

if __name__ == "__main__":
    app.run(debug=True)
