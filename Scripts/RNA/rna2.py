import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

# Cargar los datos desde archivos de entrenamiento y prueba (conjuntos originales)
train_data = pd.read_csv('train_data_mx.csv')
test_data = pd.read_csv('test_data_mx.csv')

# Obtener características y etiquetas de entrenamiento (conjuntos originales)
X_train = train_data.drop(['Etiq1', 'Etiq2'], axis=1).values
y_train = train_data[['Etiq1', 'Etiq2']].values

# Obtener características y etiquetas de prueba (conjuntos originales)
X_test = test_data.drop(['Etiq1', 'Etiq2'], axis=1).values
y_test = test_data[['Etiq1', 'Etiq2']].values

# Cargar los nuevos conjuntos de datos
train_data_arg = pd.read_csv('train_data_arg.csv')
train_data_cl = pd.read_csv('train_data_cl.csv')
train_data_it = pd.read_csv('train_data_it.csv')
test_data_arg = pd.read_csv('test_data_arg.csv')
test_data_cl = pd.read_csv('test_data_cl.csv')

# Obtener características y etiquetas de los nuevos conjuntos de entrenamiento
X_train_arg = train_data_arg.drop(['Etiq1', 'Etiq2'], axis=1).values
y_train_arg = train_data_arg[['Etiq1', 'Etiq2']].values

X_train_cl = train_data_cl.drop(['Etiq1', 'Etiq2'], axis=1).values
y_train_cl = train_data_cl[['Etiq1', 'Etiq2']].values

X_train_it = train_data_it.drop(['Etiq1', 'Etiq2'], axis=1).values
y_train_it = train_data_it[['Etiq1', 'Etiq2']].values

# Obtener características y etiquetas de los nuevos conjuntos de prueba
X_test_arg = test_data_arg.drop(['Etiq1', 'Etiq2'], axis=1).values
y_test_arg = test_data_arg[['Etiq1', 'Etiq2']].values

X_test_cl = test_data_cl.drop(['Etiq1', 'Etiq2'], axis=1).values
y_test_cl = test_data_cl[['Etiq1', 'Etiq2']].values

# Concatenar los datos de entrenamiento y prueba
X_train_combined = np.concatenate((X_train, X_train_arg, X_train_cl, X_train_it), axis=0)
y_train_combined = np.concatenate((y_train, y_train_arg, y_train_cl, y_train_it), axis=0)


X_test_combined = np.concatenate((X_test, X_test_arg, X_test_cl), axis=0)
y_test_combined = np.concatenate((y_test, y_test_arg, y_test_cl), axis=0)
# Crear un modelo de red neuronal para todos los conjuntos de datos
model = Sequential()
model.add(Dense(64, input_dim=X_train_combined.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(2, activation='sigmoid'))  # Ajustar el número de neuronas a 6

# Compilar el modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo
model.fit(X_train_combined, y_train_combined, epochs=10, batch_size=32, validation_data=(X_test_combined, y_test_combined))

# Evaluar el modelo en el conjunto de prueba
loss, accuracy = model.evaluate(X_test_combined, y_test_combined)
print("Loss:", loss)
print("Accuracy:", accuracy)

# Guardar el modelo entrenado
model.save('modelo_entrenado.keras')
