import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
colmenas_df = pd.read_csv('./data/colmenas.csv', delimiter=',', index_col=0)
ambiente_df = pd.read_csv('./data/ambiente.csv', delimiter=';')

# Convertir 'DateTime' a tipo datetime
ambiente_df['DateTime'] = pd.to_datetime(ambiente_df['DateTime'], format='%d.%m.%Y %H:%M')

# Extraer año, mes, semana y día
ambiente_df['year'] = ambiente_df['DateTime'].dt.year
ambiente_df['month'] = ambiente_df['DateTime'].dt.month
ambiente_df['week'] = ambiente_df['DateTime'].dt.isocalendar().week
ambiente_df['day'] = ambiente_df['DateTime'].dt.day

# Promediar datos de ambiente por semana
weekly_ambient = ambiente_df.groupby(['year', 'week']).agg({
    'T17': 'mean',
    'RH17': 'mean',
    'AT17': 'mean',
    'Tamb': 'mean',
    'RHamb': 'mean',
    'ATamb': 'mean'
}).reset_index()

# Renombrar columnas para mayor claridad
weekly_ambient.rename(columns={
    'T17': 'temperature',
    'RH17': 'humidity',
    'AT17': 'apparent_temperature',
    'Tamb': 'ambient_temperature',
    'RHamb': 'ambient_humidity',
    'ATamb': 'ambient_apparent_temperature'
}, inplace=True)

# Limpiar el DataFrame de colmenas eliminando columnas innecesarias
colmenas_df = colmenas_df[['state', 'numcol', 'yieldpercol', 'totalprod', 'stocks', 'priceperlb', 'year']]

# Unir datos de ambiente con producción
merged_df = pd.merge(weekly_ambient, colmenas_df, on='year', how='left')

# Imprimir nombres de columnas para verificar
print("Columnas en merged_df:", merged_df.columns)

# Verificar si las columnas necesarias existen antes de calcular correlaciones
required_columns = ['temperature', 'humidity', 'priceperlb']
missing_columns = [col for col in required_columns if col not in merged_df.columns]

if not missing_columns:
    correlations = merged_df[required_columns].corr()
    print(correlations)
else:
    print("Las siguientes columnas faltan en el DataFrame:", missing_columns)

# Establecer rangos ideales (ejemplo, ajusta según tus datos)
ideal_temp_range = (20, 30)  # Ajusta según tus necesidades
ideal_humidity_range = (40, 60)  # Ajusta según tus necesidades

# Filtrar datos de ambiente por condiciones ideales
ideal_conditions = weekly_ambient[
    (weekly_ambient['temperature'] >= ideal_temp_range[0]) &
    (weekly_ambient['temperature'] <= ideal_temp_range[1]) &
    (weekly_ambient['humidity'] >= ideal_humidity_range[0]) &
    (weekly_ambient['humidity'] <= ideal_humidity_range[1])
]

# Asignar una puntuación basada en las condiciones ideales y la producción
if 'priceperlb' in merged_df.columns:
    ideal_conditions = ideal_conditions.merge(merged_df[['year', 'week', 'priceperlb']], on=['year', 'week'], how='left')
    ideal_conditions['score'] = (
        (ideal_conditions['temperature'] - ideal_temp_range[0]) / (ideal_temp_range[1] - ideal_temp_range[0]) +
        (ideal_conditions['humidity'] - ideal_humidity_range[0]) / (ideal_humidity_range[1] - ideal_humidity_range[0])
    ) / 2

    # Identificar las mejores semanas
    best_weeks = ideal_conditions.sort_values(by='score', ascending=False)

    # Gráfico de producción y condiciones ideales
    plt.figure(figsize=(12, 8))
    plt.plot(ideal_conditions['week'], ideal_conditions['priceperlb'], label='Producción de Polen', color='blue')
    plt.scatter(best_weeks['week'], best_weeks['priceperlb'], color='red', label='Mejores Semanas')

    plt.xlabel('Semana del Año')
    plt.ylabel('Producción de Polen')
    plt.title('Producción de Polen y Mejores Semanas para la Recolección')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('./static/img/mejores_semanas.png')
    plt.close()
else:
    print("La columna 'priceperlb' no está disponible en el DataFrame.")
