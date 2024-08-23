from flask import Flask, render_template, request, redirect, url_for
import sqlite3

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

if __name__ == '__main__':
    app.run(debug=True)
