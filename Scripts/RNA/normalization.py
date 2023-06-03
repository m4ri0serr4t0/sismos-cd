import pandas as pd
import csv
mexico = pd.read_csv("Mexico.csv")
chile = pd.read_csv("Chile.csv")
italia = pd.read_csv("italy_earthquakes_from_2016-08-24_to_2016-11-30.csv")
argentina = pd.read_csv("argentina.csv")

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

magnitud_totalI= italia["Magnitude"].values  # lee solo los valores sin indices
magnitud_error = italia["magError"].values

#italia
with open('magnitud.csv', 'w', newline='') as file_italia:
    writer_italia = csv.writer(file_italia)
    writer_italia.writerow(["Magnitude", "magError"])

    for i in range(len(magnitud_totalI)):
        valor_normalizado_magnitud = (magnitud_totalI[i] - magnitud_totalI.min()) / (
                    magnitud_totalI.max() - magnitud_totalI.min())
        valor_normalizado_magnitud_error = (magnitud_error[i] - magnitud_error.min()) / (magnitud_error.max() - magnitud_error.min())
        writer_italia.writerow([valor_normalizado_magnitud, valor_normalizado_magnitud_error])

magnitudd_total=argentina["Magnitude"].values  # lee solo los valores sin indices
magnitudd_error = argentina["errorMag"].values

#argentina
with open('magnitud_Arg.csv', 'w', newline='') as file_argentina:
    writer_argentina = csv.writer(file_argentina)
    writer_argentina.writerow(["Magnitude", "errorMag"])

    for i in range(len(magnitudd_total)):
        valor_normalizado_magnitud = (magnitudd_total[i] - magnitudd_total.min()) / (
                    magnitudd_total.max() - magnitudd_total.min())
        valor_normalizado_magnitud_error = (magnitudd_error[i] - magnitudd_error.min()) / (magnitudd_error.max() - magnitudd_error.min())
        writer_argentina.writerow([valor_normalizado_magnitud, valor_normalizado_magnitud_error])
