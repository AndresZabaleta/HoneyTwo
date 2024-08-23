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
    return render_template('formulario.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    fecha = request.form['fecha']
    numcol = request.form['numcol']
    ubicacion = request.form['ubicacion']
    temperatura = request.form['temperatura']
    humedad = request.form['humedad']

    # Guardar datos en la base de datos
    conn = sqlite3.connect('apicultura.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO datos_apicultor (fecha, numcol, ubicacion, temperatura, humedad)
        VALUES (?, ?, ?, ?, ?)
    ''', (fecha, numcol, ubicacion, temperatura, humedad))
    conn.commit()
    conn.close()

    return redirect(url_for('datos'))

@app.route('/datos')
def datos():
    conn = sqlite3.connect('apicultura.db')
    c = conn.cursor()
    c.execute('SELECT * FROM datos_apicultor')
    datos = c.fetchall()
    conn.close()
    return render_template('datos.html', datos=datos)

# Ruta para mostrar los gráficos
@app.route('/graficos')
def graficos():
    # Cargar los datos de los CSVs
    ambiente = pd.read_csv('./data/ambiente.csv')
    colmenas = pd.read_csv('./data/colmenas.csv')

    # Preprocesamiento y normalización de fechas
    ambiente['DateTime'] = pd.to_datetime(ambiente['DateTime'], format='%d.%m.%Y %H:%M')
    colmenas['year'] = pd.to_datetime(colmenas['year'], format='%Y')

    # Agrupación de datos por períodos (meses o semanas)
    ambiente['Month'] = ambiente['DateTime'].dt.month
    colmenas['Month'] = colmenas['year'].dt.month

    # Unión de ambas bases de datos
    df_merged = pd.merge(ambiente, colmenas, how='inner', on='Month')

    # Análisis de Correlación para identificar periodos óptimos de recolección
    corr = df_merged.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')

    # Guardar gráfico en memoria
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    heatmap_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()

    # Gráfico de disponibilidad de polen durante el año
    df_monthly = df_merged.groupby('Month')['totalprod'].sum().reset_index()
    plt.figure(figsize=(10, 6))
    plt.bar(df_monthly['Month'], df_monthly['totalprod'], color='gold')
    plt.title('Disponibilidad de Polen Durante el Año')
    plt.xlabel('Mes')
    plt.ylabel('Total de Producción (Libras)')

    # Guardar gráfico en memoria
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    bargraph_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()

    # Renderizar la plantilla y pasar las URLs de las imágenes
    return render_template('graficos.html', heatmap_url=heatmap_url, bargraph_url=bargraph_url)


if __name__ == '__main__':
    app.run(debug=True)
