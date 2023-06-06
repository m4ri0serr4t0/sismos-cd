import pandas as pd
import random
# Leer el archivo CSV
data = pd.read_csv('argentina.csv')

# Definir el rango deseado
rango_min = 2.0
rango_max = 3.2


# Modificar los valores de la columna dentro del rango
data.loc[(data['Magnitude'] >= rango_min) & (data['Magnitude'] <= rango_max), 'Magnitude'] = data.apply(lambda row: random.uniform(2, 3.2) if rango_min <= row['Magnitude'] <= rango_max else row['Magnitude'], axis=1)

# Guardar los cambios en un nuevo archivo CSV
data.to_csv('argentina2.csv', index=False)