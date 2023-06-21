import pandas as pd

# Importar datos desde un archivo CSV
data = pd.read_csv('D:\Mario\Documents\Ingeniería en Computación\Octavo Semestre\Ciencia de  Datos\Proyecto\Scripts\RNA2\Datasets\Grecia.csv')
# Obtener el tamaño del conjunto de datos
print(data.shape)

# Visualizar las primeras filas del conjunto de datos
print(data.head())
# Obtener estadísticas descriptivas básicas
print(data.describe())