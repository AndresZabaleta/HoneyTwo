from flask import Flask, render_template, request

appi = Flask(__name__)

# Función para evaluar la salud de las colmenas
def evaluar_salud_colmena(salud):
    if salud.lower() in ['buena', 'excelente']:
        return "La salud de la colmena es óptima para reactivación."
    elif salud.lower() == 'regular':
        return "Es recomendable mejorar la salud de las colmenas antes de reactivarlas."
    else:
        return "No es recomendable reactivar las colmenas en su estado actual."

# Función para sugerir los mejores momentos de reactivación
def sugerir_momento_reactivacion(estacionalidad, demanda_polen):
    if estacionalidad.lower() in ['primavera', 'verano']:
        estacionalidad_factor = 'alta'
    elif estacionalidad.lower() == 'otoño':
        estacionalidad_factor = 'media'
    else:
        estacionalidad_factor = 'baja'

    if demanda_polen.lower() == 'alta':
        demanda_factor = 'alta'
    elif demanda_polen.lower() == 'media':
        demanda_factor = 'media'
    else:
        demanda_factor = 'baja'

    if estacionalidad_factor == 'alta' and demanda_factor == 'alta':
        return "Es un excelente momento para reactivar las colmenas."
    elif estacionalidad_factor == 'media' or demanda_factor == 'media':
        return "Es un momento aceptable para reactivar las colmenas, pero con precaución."
    else:
        return "No es un buen momento para reactivar las colmenas."

@appi.route('/recomendaciones', methods=['GET', 'POST'])
def recomendaciones():
    if request.method == 'POST':
        # Obtener los datos del formulario
        cantidad_colmenas = int(request.form['cantidad_colmenas'])
        ubicacion = request.form['ubicacion']
        estacionalidad = request.form['estacionalidad']
        salud_colmena = request.form['salud_colmena']
        demanda_polen = request.form['demanda_polen']

        # Evaluar la salud de las colmenas
        evaluacion_salud = evaluar_salud_colmena(salud_colmena)

        # Sugerir el mejor momento para reactivar
        if evaluacion_salud == "La salud de la colmena es óptima para reactivación.":
            recomendacion_reactivacion = sugerir_momento_reactivacion(estacionalidad, demanda_polen)
        else:
            recomendacion_reactivacion = "Mejore la salud de las colmenas antes de proceder con la reactivación."
    
        # Renderizar la plantilla con los resultados
        return render_template('recomendaciones.html', 
                               evaluacion_salud=evaluacion_salud, 
                               recomendacion_reactivacion=recomendacion_reactivacion)
    else:
        # Mostrar el formulario inicialmente sin resultados
        return render_template('recomendaciones.html')

if __name__ == '__main__':
    appi.run(debug=True)