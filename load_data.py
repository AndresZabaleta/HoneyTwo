import sqlite3
import pandas as pd

def load_environment_data():
    # Cargar datos desde el CSV con el delimitador correcto
    env_df = pd.read_csv('./data/ambiente.csv', sep=';')
    # Verifica los nombres de las columnas
    print(env_df.columns)
    # Conectar a la base de datos SQLite
    conn = sqlite3.connect('apicultores.db')
    # Cargar los datos en la tabla 'environment'
    env_df.to_sql('environment', conn, if_exists='replace', index=False)
    conn.close()

def load_colmenas_data():
    # Cargar datos desde el CSV con el delimitador correcto
    colmenas_df = pd.read_csv('./data/colmenas.csv', sep=',')
    # Verifica los nombres de las columnas
    print(colmenas_df.columns)
    # Conectar a la base de datos SQLite
    conn = sqlite3.connect('apicultores.db')
    # Cargar los datos en la tabla 'colmenas'
    colmenas_df.to_sql('colmenas', conn, if_exists='replace', index=False)
    conn.close()

if __name__ == '__main__':
    load_environment_data()
    load_colmenas_data()
