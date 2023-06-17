import pandas as pd

class DataPreprocessor:
    def __init__(self, df):
        self.df = df

    def preprocess(self):
        # Elimina los valores faltantes
        self.df = self.df.dropna()

        # Corrige los valores incorrectos
        # self.df['edad'] = self.df['edad'].replace(-1, 0)  # Reemplaza los valores negativos con 0

        # Elimina los valores duplicados
        self.df = self.df.drop_duplicates()

        # Guarda los datos limpios en un nuevo DataFrame
        cleaned_data = self.df.copy()

        return cleaned_data
