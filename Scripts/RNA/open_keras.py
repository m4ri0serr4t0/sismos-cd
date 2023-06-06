from keras.models import load_model
from keras.utils import plot_model
from PIL import Image
import matplotlib.pyplot as plt


import numpy as np

model = load_model('modelo_entrenado.keras')
model.summary()
# Generar el diagrama de la arquitectura del modelo sin los parámetros
plot_model(model, to_file='arquitectura_modelo.png', show_shapes=True, show_layer_names=False)

# Crear los subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Mostrar la imagen del diagrama de la arquitectura del modelo en ax1
image = plt.imread('arquitectura_modelo.png')
ax1.imshow(image)
ax1.axis('off')  # Desactivar los ejes

# Agregar una descripción o leyenda con los detalles de los parámetros en ax2
description = "Capa 1: 64 neuronas\nCapa 2: 32 neuronas\nCapa 3: 1 neurona"
ax2.text(0.1, 0.1, description, fontsize=12, color='black', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))
ax2.axis('off')  # Desactivar los ejes

plt.show()