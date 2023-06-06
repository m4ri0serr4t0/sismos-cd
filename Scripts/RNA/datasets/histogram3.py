import pandas as pd
import matplotlib.pyplot as plt

# Leer los archivos CSV
data1 = pd.read_csv('italia.csv')
data2 = pd.read_csv('argentina2.csv')

# Extraer la columna de interés de cada conjunto de datos
columna1 = data1['Magnitude']
columna2 = data2['Magnitude']

# Crear el histograma de comparación
plt.hist(columna1, bins=10, alpha=0.5, label='Sismos Italia')
plt.hist(columna2, bins=10, alpha=0.5, label='Sismos Argentina')

# Agregar etiquetas y título al histograma
plt.xlabel('Magnitud del sismo')
plt.ylabel('Frecuencia')
plt.title('Histograma de Comparación')

# Agregar una leyenda para distinguir los conjuntos de datos
plt.legend()

# Mostrar el histograma
plt.show()
