import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

# Cargar los datos desde archivos de entrenamiento y prueba
train_data = pd.read_csv('train_data_mx.csv')
test_data = pd.read_csv('test_data_mx.csv')

# Obtener características y etiquetas de entrenamiento
X_train = train_data.drop('W', axis=1).values
y_train = train_data['W'].values

# Obtener características y etiquetas de prueba
X_test = test_data.drop('W', axis=1).values
y_test = test_data['W'].values

# Preprocesar los datos (opcional)
# Puedes aplicar técnicas de normalización, codificación one-hot, etc.

# Dividir los datos en conjuntos de entrenamiento y prueba
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un modelo de red neuronal
model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compilar el modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Evaluar el modelo en el conjunto de prueba
loss, accuracy = model.evaluate(X_test, y_test)
print("Loss:", loss)
print("Accuracy:", accuracy)

# Guardar el modelo entrenado
model.save('modelo_entrenado.keras')