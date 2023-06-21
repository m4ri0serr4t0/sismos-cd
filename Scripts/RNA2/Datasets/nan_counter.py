import csv

def contar_datos_faltantes(archivo_csv):
    with open(archivo_csv, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        encabezado = next(lector_csv)  # Leer el encabezado del archivo CSV

        conteo = [0] * len(encabezado)  # Inicializar lista de conteo

        for fila in lector_csv:
            for i in range(len(fila)):
                if not fila[i]:  # Verificar si el dato está vacío
                    conteo[i] += 1  # Incrementar el contador correspondiente

        # Imprimir los resultados
        print('{:<15} {:<15}'.format('Columna', 'Datos faltantes'))
        print('-' * 30)
        for i in range(len(encabezado)):
            print('{:<15} {:<15}'.format(encabezado[i], conteo[i]))


# Ejemplo de uso
archivo_csv = 'D:\Mario\Documents\Ingeniería en Computación\Octavo Semestre\Ciencia de  Datos\Proyecto\Scripts\RNA2\DataSets\Grecia.csv'
contar_datos_faltantes(archivo_csv)
