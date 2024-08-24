# PRODUCCION ANUAL DE MIEL####################################
# import pandas as pd
# import matplotlib.pyplot as plt

# # Cargar los datos de colmenas.csv
# colmenas_df = pd.read_csv('./data/colmenas.csv', delimiter=',')

# # Seleccionar las columnas relevantes
# colmenas_df = colmenas_df[['year', 'totalprod']]

# # Agrupar por año y sumar la producción total
# annual_production = colmenas_df.groupby('year').sum().reset_index()

# # Crear el gráfico
# plt.figure(figsize=(12, 6))
# plt.bar(annual_production['year'], annual_production['totalprod'], color='orange', alpha=0.7)

# # Añadir etiquetas y título
# plt.xlabel('Año')
# plt.ylabel('Producción Total de Polen (libras)')
# plt.title('Producción Anual de Polen')
# plt.xticks(annual_production['year'])  # Asegurar que todos los años aparezcan en el eje x

# # Guardar el gráfico como imagen
# plt.tight_layout()
# plt.savefig('./static/img/produccion_anual.png')
# plt.close()

# PRODUCCION POR ESTADO Y AÑO####################################
# import pandas as pd
# import matplotlib.pyplot as plt

# # Cargar los datos de colmenas.csv
# colmenas_df = pd.read_csv('./data/colmenas.csv', delimiter=',')

# # Seleccionar las columnas relevantes
# colmenas_df = colmenas_df[['year', 'state', 'totalprod']]

# # Agrupar por año y estado y sumar la producción total
# annual_state_production = colmenas_df.groupby(['year', 'state']).sum().reset_index()

# # Filtrar los estados que quieres mostrar (modifica esta lista según tus necesidades)
# states_to_show = ['North Dakota', 'South Dakota', 'California', 'Montana', 'Florida', 'Texas']

# # Filtrar los datos para mostrar solo los estados seleccionados
# filtered_production = annual_state_production[annual_state_production['state'].isin(states_to_show)]

# # Crear el gráfico
# plt.figure(figsize=(12, 8))
# for state in states_to_show:
#     state_data = filtered_production[filtered_production['state'] == state]
#     plt.plot(state_data['year'], state_data['totalprod'], label=state)

# # Añadir etiquetas y título
# plt.xlabel('Año')
# plt.ylabel('Producción Total de Polen (libras)')
# plt.title('Producción de Polen por Año y Estado')
# plt.legend(title='Estado')
# plt.xticks(annual_state_production['year'].unique())

# # Guardar el gráfico como imagen
# plt.tight_layout()
# plt.savefig('./static/img/produccion_por_estado_ano.png')
# plt.close()

# PRODUCCION ESTACIONAL####################################
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# # Cargar los datos de colmenas.csv
# colmenas_df = pd.read_csv('./data/colmenas.csv', delimiter=',')

# # Estimación de producción para 2024 basada en el último año disponible
# if 2024 not in colmenas_df['year'].values:
#     estimated_2024_prod = colmenas_df[colmenas_df['year'] == colmenas_df['year'].max()]['totalprod'].values[0]
# else:
#     estimated_2024_prod = colmenas_df[colmenas_df['year'] == 2024]['totalprod'].values[0]

# # Estacionalidad (proporciones aproximadas para cada mes basadas en patrones históricos)
# seasonal_weights = {
#     1: 0.05,  # Enero
#     2: 0.05,  # Febrero
#     3: 0.1,   # Marzo
#     4: 0.15,  # Abril
#     5: 0.2,   # Mayo
#     6: 0.2,   # Junio
#     7: 0.1,   # Julio
#     8: 0.05,  # Agosto
#     9: 0.05,  # Septiembre
#     10: 0.025, # Octubre
#     11: 0.025, # Noviembre
#     12: 0.05  # Diciembre
# }

# # Calcular la producción mensual basada en estacionalidad
# monthly_production = {month: estimated_2024_prod * weight for month, weight in seasonal_weights.items()}

# # Crear un DataFrame para los meses de 2024
# months = np.arange(1, 13)
# monthly_production_df = pd.DataFrame({
#     'month': months,
#     'monthly_prod': [monthly_production[m] for m in months]
# })

# # Graficar la producción mensual estacional para 2024
# plt.figure(figsize=(10, 6))
# plt.plot(monthly_production_df['month'], monthly_production_df['monthly_prod'], marker='o', color='b')

# # Añadir etiquetas y título
# plt.xlabel('Mes')
# plt.ylabel('Producción Estimada de Polen (libras)')
# plt.title('Previsión Mensual Estacional de Producción de Polen para 2024')
# plt.xticks(months, ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
# plt.grid(True)

# # Guardar el gráfico como imagen
# plt.tight_layout()
# plt.savefig('./static/img/prevision_estacional_produccion_2024.png')
# plt.close()

# # DEMANDA ESTACIONAL####################################
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# # Cargar los datos de colmenas.csv
# colmenas_df = pd.read_csv('./data/colmenas.csv', delimiter=',')

# # Estimación de producción para 2024 basada en el último año disponible
# if 2024 not in colmenas_df['year'].values:
#     estimated_2024_prod = colmenas_df[colmenas_df['year'] == colmenas_df['year'].max()]['totalprod'].values[0]
# else:
#     estimated_2024_prod = colmenas_df[colmenas_df['year'] == 2024]['totalprod'].values[0]

# # Estacionalidad (proporciones aproximadas para cada mes basadas en patrones históricos)
# seasonal_weights = {
#     1: 0.05,  # Enero
#     2: 0.05,  # Febrero
#     3: 0.1,   # Marzo
#     4: 0.15,  # Abril
#     5: 0.2,   # Mayo
#     6: 0.2,   # Junio
#     7: 0.1,   # Julio
#     8: 0.05,  # Agosto
#     9: 0.05,  # Septiembre
#     10: 0.025, # Octubre
#     11: 0.025, # Noviembre
#     12: 0.05  # Diciembre
# }

# # Calcular la producción mensual basada en estacionalidad
# monthly_production = {month: estimated_2024_prod * weight for month, weight in seasonal_weights.items()}

# # Definir demanda mensual (suponiendo que la demanda es mayor en meses de baja producción)
# demand_weights = {
#     1: 0.1,  # Enero
#     2: 0.1,  # Febrero
#     3: 0.15, # Marzo
#     4: 0.1,  # Abril
#     5: 0.05, # Mayo
#     6: 0.05, # Junio
#     7: 0.1,  # Julio
#     8: 0.15, # Agosto
#     9: 0.1,  # Septiembre
#     10: 0.05, # Octubre
#     11: 0.05, # Noviembre
#     12: 0.1  # Diciembre
# }

# # Calcular la demanda mensual basada en estacionalidad
# monthly_demand = {month: estimated_2024_prod * weight for month, weight in demand_weights.items()}

# # Crear un DataFrame para los meses de 2024
# months = np.arange(1, 13)
# monthly_data_df = pd.DataFrame({
#     'month': months,
#     'monthly_prod': [monthly_production[m] for m in months],
#     'monthly_demand': [monthly_demand[m] for m in months]
# })

# # Graficar la producción y demanda mensual para 2024
# plt.figure(figsize=(10, 6))
# plt.plot(monthly_data_df['month'], monthly_data_df['monthly_prod'], marker='o', color='b', label='Disponibilidad de Polen')
# plt.plot(monthly_data_df['month'], monthly_data_df['monthly_demand'], marker='o', color='r', linestyle='--', label='Demanda de Polen')

# # Añadir etiquetas y título
# plt.xlabel('Mes')
# plt.ylabel('Polen (libras)')
# plt.title('Disponibilidad y Demanda de Polen para 2024')
# plt.xticks(months, ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
# plt.legend()
# plt.grid(True)

# # Guardar el gráfico como imagen
# plt.tight_layout()
# plt.savefig('./static/img/disponibilidad_demanda_polen_2024.png')
# plt.close()

# # PRECIO VS DEMANDA####################################
# import pandas as pd
# import matplotlib.pyplot as plt

# # Cargar los datos de colmenas.csv
# colmenas_df = pd.read_csv('./data/colmenas.csv', delimiter=',')

# # Seleccionar las columnas relevantes
# colmenas_df = colmenas_df[['year', 'priceperlb', 'totalprod']]

# # Crear el gráfico
# plt.figure(figsize=(10, 6))
# plt.scatter(colmenas_df['priceperlb'], colmenas_df['totalprod'], color='blue')

# # Añadir etiquetas y título
# plt.xlabel('Precio por Libra ($)')
# plt.ylabel('Producción Total de Polen (libras)')
# plt.title('Relación entre Precio y Demanda de Polen')
# plt.grid(True)

# # Guardar el gráfico como imagen
# plt.tight_layout()
# plt.savefig('./static/img/precio_vs_demanda.png')
# plt.show()

# # PRECIO PROMEDIO POR MES####################################
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar los datos de colmenas.csv
colmenas_df = pd.read_csv('./data/colmenas.csv', delimiter=',')

# Revisar si hay valores nulos en la columna 'year'
print(f"Valores NaN en 'year': {colmenas_df['year'].isna().sum()}")

# Revisar si hay valores infinitos en la columna 'year'
print(f"Valores infinitos en 'year': {(colmenas_df['year'] == float('inf')).sum()}")

# Limpieza de datos: eliminar filas con valores nulos o infinitos en 'year'
colmenas_df = colmenas_df[~colmenas_df['year'].isna()]
colmenas_df = colmenas_df[colmenas_df['year'] != float('inf')]

# Convertir la columna 'year' a entero
colmenas_df['year'] = colmenas_df['year'].astype(int)

# Definir un patrón estacional (ejemplo ficticio)
# Estos factores se deben ajustar basándose en datos reales o expertos en apicultura.
seasonal_factors = {
    1: 0.7,   # Enero
    2: 0.7,   # Febrero
    3: 0.8,   # Marzo
    4: 1.0,   # Abril
    5: 1.2,   # Mayo
    6: 1.3,   # Junio
    7: 1.3,   # Julio
    8: 1.2,   # Agosto
    9: 1.0,   # Septiembre
    10: 0.9,  # Octubre
    11: 0.8,  # Noviembre
    12: 0.7   # Diciembre
}

# Crear un DataFrame con la distribución mensual basado en el patrón estacional
monthly_data_list = []
for _, row in colmenas_df.iterrows():
    # Crear un DataFrame para cada año con 12 meses
    monthly_data = pd.DataFrame({
        'year': row['year'],
        'month': range(1, 13),
        'price_per_lb': row['priceperlb'] * np.array([seasonal_factors[m] for m in range(1, 13)])
    })
    monthly_data_list.append(monthly_data)

# Unir todos los DataFrames en uno solo
monthly_df = pd.concat(monthly_data_list, ignore_index=True)

# Calcular el precio promedio por mes y año
monthly_price_avg = monthly_df.groupby(['year', 'month']).mean().reset_index()

# Crear el gráfico del precio promedio por mes
plt.figure(figsize=(12, 8))
for year in monthly_price_avg['year'].unique():
    year_data = monthly_price_avg[monthly_price_avg['year'] == year]
    plt.plot(year_data['month'], year_data['price_per_lb'], label=f'Año {year}')

plt.xlabel('Mes')
plt.ylabel('Precio Promedio por Libra (dólares)')
plt.title('Precio Promedio de Polen por Mes')
plt.legend(title='Año')
plt.grid(True)

# Guardar el gráfico como imagen
plt.tight_layout()
plt.savefig('./static/img/precio_promedio_por_mes_estacional.png')
plt.close()
