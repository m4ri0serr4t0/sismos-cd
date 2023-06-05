import pandas as pd
import matplotlib.pyplot as plt

from keras.utils import plot_model
from keras.models import Sequential
from keras.layers import Dense

# Cargar los conjuntos de entrenamiento y prueba desde archivos CSV
train_data = pd.read_csv('train_data_mx.csv')
test_data = pd.read_csv('test_data_mx.csv')


# Obtener características y etiquetas de entrenamiento
X_train = train_data.drop(['W', 'MaxPd'], axis=1).values
y_train = train_data[['W', 'MaxPd']].values

# Obtener características y etiquetas de prueba
X_test = test_data.drop(['W', 'MaxPd'], axis=1).values
y_test = test_data[['W', 'MaxPd']].values

# Crear un modelo de red neuronal
model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(2, activation='linear'))

# Generar el gráfico de la red
plot_model(model, to_file='red_neuronal.png', show_shapes=True, show_layer_names=True)

# Mostrar el gráfico en pantalla
image = plt.imread('red_neuronal.png')
fig, ax = plt.subplots()
ax.imshow(image)
ax.axis('off')
plt.show()
