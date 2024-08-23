import sqlite3
import pandas as pd

def analyze_patterns():
    conn = sqlite3.connect('apicultura.db')
    query = '''
    SELECT DateTime, totalprod
    FROM environment
    JOIN colmenas ON strftime('%Y', DateTime) = colmenas.year
    '''
    df = pd.read_sql_query(query, conn)
    conn.close()

    # Convertir la columna DateTime a formato datetime
    df['DateTime'] = pd.to_datetime(df['DateTime'], format='%d/%m/%Y %H:%M')

    # Agrupar por semana y calcular la producción total promedio
    df.set_index('DateTime', inplace=True)
    weekly_data = df.resample('W').mean()

    # Identificar las semanas con mayor producción
    best_weeks = weekly_data['totalprod'].sort_values(ascending=False)
    print("Top weeks for honey production:")
    print(best_weeks.head())

if __name__ == '__main__':
    analyze_patterns()
