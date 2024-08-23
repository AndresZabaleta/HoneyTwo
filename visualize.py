import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def plot_environment_data():
    conn = sqlite3.connect('apicultura.db')
    query = 'SELECT DateTime, T17, RH17, AT17, Tamb, RHamb, ATamb FROM environment'
    df = pd.read_sql_query(query, conn)
    conn.close()

    # Convertir la columna DateTime a formato datetime con el formato correcto
    df['DateTime'] = pd.to_datetime(df['DateTime'], format='%d.%m.%Y %H:%M')

    # Graficar la temperatura T17 y la humedad RH17
    plt.figure(figsize=(12, 6))
    plt.plot(df['DateTime'], df['T17'], label='Temperature T17')
    plt.plot(df['DateTime'], df['RH17'], label='Humidity RH17')
    plt.xlabel('DateTime')
    plt.ylabel('Values')
    plt.title('Temperature and Humidity over Time')
    plt.legend()
    plt.grid(True)
    plt.savefig('static/img/temperature_humidity.png')
    # plt.show()

def plot_colmenas_data():
    conn = sqlite3.connect('apicultura.db')
    query = 'SELECT year, totalprod FROM colmenas'
    df = pd.read_sql_query(query, conn)
    conn.close()

    # Graficar la producción total por año
    plt.figure(figsize=(10, 6))
    plt.bar(df['year'], df['totalprod'])
    plt.xlabel('Year')
    plt.ylabel('Total Production (pounds)')
    plt.title('Total Honey Production by Year')
    plt.grid(True)
    plt.savefig('static/img/total_production.png')
    # plt.show()

if __name__ == '__main__':
    plot_environment_data()
    plot_colmenas_data()

# import sqlite3

# def check_table_schema():
#     conn = sqlite3.connect('apicultura.db')
#     cursor = conn.cursor()
#     cursor.execute("PRAGMA table_info(colmenas);")
#     columns = cursor.fetchall()
#     conn.close()

#     for column in columns:
#         print(f"Column name: {column[1]}")

# if __name__ == '__main__':
#     check_table_schema()