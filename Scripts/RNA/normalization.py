import pandas as pd
import csv
mexico = pd.read_csv("Mexico.csv")
chile = pd.read_csv("Chile.csv")


#Mexico

peso_personas_mx=mexico["W"].values #lee solo los valores sin indices
max_cargaAx_mx=mexico["MaxPd"].values

with open ('pesos_cargaAx_mx.csv', 'w', newline='') as file_mexico:
    writer_mexico = csv.writer(file_mexico)
    writer_mexico.writerow(["W", "MaxPd"])


    for i in range(len(peso_personas_mx)): #peso_personas_mx y max_cargaAx tienen la misma dimension
        valor_normalizado_peso_mx = (peso_personas_mx[i]-peso_personas_mx.min()) / (peso_personas_mx.max() - peso_personas_mx.min())
        valor_normalizado_carga_mx = (max_cargaAx_mx[i] - max_cargaAx_mx.min()) / (max_cargaAx_mx.max() - max_cargaAx_mx.min())
        writer_mexico.writerow([valor_normalizado_peso_mx, valor_normalizado_carga_mx])

peso_personas_cl= chile["W"].values  # lee solo los valores sin indices
max_cargaAx_cl = chile["MaxPd"].values
# print(peso_personas_mx)

#Chile
with open('pesos_cargaAx_cl.csv', 'w', newline='') as file_chile:
    writer_chile = csv.writer(file_chile)
    writer_chile.writerow(["W", "MaxPd"])

    for i in range(len(peso_personas_cl)):  # peso_personas_mx y max_cargaAx tienen la misma dimension
        valor_normalizado_peso_cl = (peso_personas_cl[i] - peso_personas_cl.min()) / (
                    peso_personas_cl.max() - peso_personas_cl.min())
        valor_normalizado_carga_cl = (max_cargaAx_cl[i] - max_cargaAx_cl.min()) / (max_cargaAx_cl.max() - max_cargaAx_cl.min())
        writer_chile.writerow([valor_normalizado_peso_cl, valor_normalizado_carga_cl])

#valor_normalizado = (valor_original - valor_minimo) / (valor_maximo - valor_minimo)
