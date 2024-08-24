import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('apicultores.db')
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS datos_apicultores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        numcol INTEGER,
        ubicacion TEXT,
        estacion TEXT,
        estsalud TEXT,
        polen TEXT,
        temperatura REAL,
        humedad REAL
    )
''')

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

# import os

# # Ruta al archivo de la base de datos
# db_path = 'apicultores.db'

# # Comprobar si el archivo de la base de datos existe
# if os.path.exists(db_path):
#     os.remove(db_path)
#     print(f"Base de datos '{db_path}' eliminada.")
# else:
#     print(f"No se encontró la base de datos '{db_path}'.")

# import sqlite3

# # Conectar a la base de datos
# conn = sqlite3.connect('apicultores.db')
# cursor = conn.cursor()

# # Eliminar todos los registros de la tabla
# cursor.execute("DELETE FROM datos_apicultores")

# # Guardar los cambios y cerrar la conexión
# conn.commit()
# conn.close()

# print("Todos los registros han sido eliminados.")