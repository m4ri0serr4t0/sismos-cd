import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('italia.csv')
#data2 = pd.read_csv('italia.csv')


columna = data['Magnitude']

plt.hist(columna, bins=10, color='green')
plt.xlabel('Magnitud del sismo')
plt.ylabel('Frecuencia')
plt.title('Histograma de Frecuencia Italia')

# Mostrar el histograma
plt.show()

