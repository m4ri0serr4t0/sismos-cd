import csv


def count_duplicate_rows(file_path):
    duplicates = 0
    unique_rows = set()

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Omitir la primera fila si contiene encabezados

        for row in reader:
            # Convierte la fila en una tupla para que sea hashable
            row_tuple = tuple(row)

            if row_tuple in unique_rows:
                duplicates += 1
            else:
                unique_rows.add(row_tuple)

    return duplicates


# Ruta del archivo CSV
file_path = 'D:\Mario\Documents\Ingeniería en Computación\Octavo Semestre\Ciencia de  Datos\Proyecto\Scripts\RNA2\Datasets\Italia.csv'

# Llamar a la función para contar filas duplicadas
duplicate_count = count_duplicate_rows(file_path)

# Imprimir el resultado
print("Número de filas duplicadas:", duplicate_count)