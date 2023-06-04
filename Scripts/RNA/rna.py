import pandas as pd
import numpy as np

# Cargar los datos desde un archivo CSV
mexico = pd.read_csv('pesos_cargaAx_mx.csv')

# Obtener características (X) y etiquetas (y)
X = mexico.values
columnas = mexico.columns

# Obtener los nombres de las columnas
etiquetas = columnas.tolist()

# Obtener los índices de los datos
indices = np.arange(len(X))

# Fijar una semilla aleatoria
np.random.seed(42)

# Barajar los índices aleatoriamente
np.random.shuffle(indices)

# Calcular el tamaño de los conjuntos de entrenamiento y prueba
train_size = int(0.8 * len(indices))
test_size = len(indices) - train_size

# Dividir los datos en conjuntos de entrenamiento y prueba
train_indices = indices[:train_size]
test_indices = indices[train_size:]

# Obtener las muestras de los conjuntos de entrenamiento y prueba
X_train = X[train_indices]
y_train = [etiquetas[i] for i in train_indices if i < len(etiquetas)]
X_test = X[test_indices]
y_test = [etiquetas[i] for i in test_indices if i < len(etiquetas)]

# Imprimir las dimensiones de los conjuntos de entrenamiento y prueba
print("Dimensiones del conjunto de entrenamiento:")
print("Características (X_train):", X_train.shape)
print("Etiquetas (y_train):", len(y_train))

print("\nDimensiones del conjunto de prueba:")
print("Características (X_test):", X_test.shape)
print("Etiquetas (y_test):", len(y_test))

print(X_train)
print(X_test)