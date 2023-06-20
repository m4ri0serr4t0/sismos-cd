import pandas as pd
import csv

mexico = pd.read_csv("Datasets\Mexico.csv")
chile = pd.read_csv("Datasets\Chile.csv")
italia = pd.read_csv("Datasets\Italia.csv")
Global = pd.read_csv("Datasets\Global.csv")

# Mexico
gf_mx = mexico["GF"].values
W_mx = mexico["W"].values  # lee solo los valores sin indices
maxpd_mx = mexico["MaxPd"].values
maxtd_mx = mexico["MaxTd"].values
maxpc_mx = mexico["MaxPc"].values

with open('normalized_data/mexico_normalizado.csv', 'w', newline='') as file_mexico:
    writer_mexico = csv.writer(file_mexico)
    writer_mexico.writerow(["Etiq1", "Etiq2", "Etiq3", "Etiq4", "Etiq5"])

    for i in range(len(W_mx)):  # W_mx y max_cargaAx tienen la misma dimension

        n_gf_mx = (gf_mx[i] - gf_mx.min()) / (gf_mx.max() - gf_mx.min())
        n_w_mx = (W_mx[i] - W_mx.min()) / (W_mx.max() - W_mx.min())
        n_pd_mx = (maxpd_mx[i] - maxpd_mx.min()) / (maxpd_mx.max() - maxpd_mx.min())
        n_td_mx = (maxtd_mx[i] - maxtd_mx.min()) / (maxtd_mx.max() - maxtd_mx.min())
        n_pc_mx = (maxpc_mx[i] - maxpc_mx.min()) / (maxpc_mx.max() - maxpc_mx.min())
        writer_mexico.writerow([n_gf_mx, n_w_mx, n_pd_mx, n_td_mx, n_pc_mx])


#Chile

gf_cl = chile["GF"].values
W_cl = chile["W"].values  # lee solo los valores sin indices
maxpd_cl = chile["MaxPd"].values
maxtd_cl = chile["MaxTd"].values
maxpc_cl = chile["MaxPc"].values

# print(W_mx)

# Chile
with open('normalized_data/Chile_normalizado', 'w', newline='') as file_chile:

    writer_chile = csv.writer(file_chile)
    writer_chile.writerow(["Etiq1", "Etiq2", "Etiq3", "Etiq4", "Etiq5"])

    for i in range(len(W_cl)):  # W_mx y max_cargaAx tienen la misma dimension

        n_gf_cl= (gf_cl[i] - gf_cl.min()) / (gf_cl.max() - gf_cl.min())
        n_w_cl= (W_cl[i] - W_cl.min()) / (W_cl.max() - W_cl.min())
        n_pd_cl= (maxpd_cl[i] - maxpd_cl.min()) / (maxpd_cl.max() - maxpd_cl.min())
        n_td_cl= (maxtd_cl[i] - maxtd_cl.min()) / (maxtd_cl.max() - maxtd_cl.min())
        n_pc_cl= (maxpc_cl[i] - maxpc_cl.min()) / (maxpc_cl.max() - maxpc_cl.min())
        writer_mexico.writerow([n_gf_cl, n_w_cl, n_pd_cl, n_td_cl, n_pc_cl])

#Italia

# valor_normalizado = (valor_original - valor_minimo) / (valor_maximo - valor_minimo)

latitud = italia["Latitude"].values  # lee solo los valores sin indices
# longitud= italia["Longitude"].values
magnitud = italia["Magnitude"].values

# italia
with open('normalized_data/Italia_normalizado.csv', 'w', newline='') as file_italia:
    writer_italia = csv.writer(file_italia)
    writer_italia.writerow(["Etiq1", "Etiq2"])

    for i in range(len(latitud)):
        valor_normalizado_latitud = (latitud[i] - latitud.min()) / (latitud.max() - latitud.min())
        # valor_normalizado_longitud = (longitud[i] - longitud.min()) / (longitud.max() - longitud.min())
        valor_normalizado_magnitud = (magnitud[i] - magnitud.min()) / (magnitud.max() - magnitud.min())

        writer_italia.writerow([valor_normalizado_latitud, valor_normalizado_magnitud])

magnitudd_total = Global["Magnitude"].values  # lee solo los valores sin indices
magnitudd_error = Global["errorMag"].values

# argentina
with open('normalized_data/magnitud_Arg.csv', 'w', newline='') as file_argentina:
    writer_global = csv.writer(file_argentina)
    writer_global.writerow(["Etiq1", "Etiq2"])

    for i in range(len(magnitudd_total)):
        valor_normalizado_magnitud = (magnitudd_total[i] - magnitudd_total.min()) / (
                magnitudd_total.max() - magnitudd_total.min())
        valor_normalizado_magnitud_error = (magnitudd_error[i] - magnitudd_error.min()) / (
                magnitudd_error.max() - magnitudd_error.min())
        writer_argentina.writerow([valor_normalizado_magnitud, valor_normalizado_magnitud_error])
