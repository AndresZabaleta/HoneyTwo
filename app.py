from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario')
def formulario():
    conn = sqlite3.connect('apicultores.db')
    c = conn.cursor()
    c.execute('SELECT * FROM datos_apicultores')
    datos = c.fetchall()
    conn.close()
    return render_template('formulario.html', datos=datos)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Obtener los datos del formulario
    fecha = request.form['fecha']
    numcol = request.form['numcol']
    ubicacion = request.form['ubicacion']
    estacion = request.form['estacion']
    estsalud = request.form['estsalud']
    polen = request.form['polen']
    temperatura = request.form['temperatura']
    humedad = request.form['humedad']

    # Conectar a la base de datos
    conn = sqlite3.connect('apicultores.db')
    cursor = conn.cursor()

    # Insertar los datos en la base de datos
    cursor.execute("""
        INSERT INTO datos_apicultores (fecha, numcol, ubicacion, estacion, estsalud, polen, temperatura, humedad)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (fecha, numcol, ubicacion, estacion, estsalud, polen, temperatura, humedad))

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

    return redirect(url_for('formulario'))

if __name__ == '__main__':
    app.run(debug=True)
