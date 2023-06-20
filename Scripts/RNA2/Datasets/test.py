import numpy as np

# Cargar los datos del archivo CSV
data = np.genfromtxt('Mexico.csv', delimiter=',')

# Dividir los datos en características (X) y etiquetas (y)
X = data[:, 1:-1]  # Seleccionar todas las columnas excepto la primera y la última
y = data[:, -1]  # Seleccionar la última columna como etiquetas

# Normalizar las características (opcional pero recomendado)
X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

# Agregar un sesgo a las características
X = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)

# Inicializar los pesos aleatoriamente
np.random.seed(42)  # Fijar la semilla para reproducibilidad
num_features = X.shape[1]
weights = np.random.randn(num_features)

# Definir el número de épocas y la tasa de aprendizaje
epochs = 1000
learning_rate = 0.01

# Entrenamiento de la red neuronal con la regla Delta
for epoch in range(epochs):
    # Calcular la salida de la red neuronal
    output = np.dot(X, weights)

    # Calcular el error
    error = y - output

    # Actualizar los pesos utilizando la regla Delta
    weights += learning_rate * np.dot(X.T, error)

def imprimir_resultados(resultados):
    # Imprimir encabezados de la tabla
    print("{:<10s} {:<10s} {:<10s}".format("Columna 1", "Columna 2", "Columna 3"))
    print("-" * 30)

    # Imprimir los datos de cada fila
    for fila in resultados:
        columna1 = fila[0]
        columna2 = fila[1]
        columna3 = fila[2]
        print("{:<10s} {:<10s} {:<10s}".format(columna1, columna2, columna3))

# Ejemplo de datos de resultados
resultados = [
    ["Dato1", "Dato2", "Dato3"],
    ["Dato4", "Dato5", "Dato6"],
    ["Dato7", "Dato8", "Dato9"]
]

# Llamar a la función para imprimir los resultados
imprimir_resultados(resultados)