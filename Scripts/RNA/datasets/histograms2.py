import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('Mexico.csv')
data2 = pd.read_csv('Chile.csv')

w = data2['W']
Mpd = data2['MaxPd']

plt.hist2d(w, Mpd, bins=10, cmap='Oranges')
plt.xlabel('Peso de las personas')
plt.ylabel('Maxima carga axial')
plt.title('Histograma Chile')
plt.show()

