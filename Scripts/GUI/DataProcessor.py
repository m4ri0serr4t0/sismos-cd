from tkinter import messagebox

import pandas as pd
from sklearn.preprocessing import MinMaxScaler


class DataPreprocessor:
    def __init__(self, df):
        self.df = df

    def preprocess(self):
        # Remove non-numeric columns and inform the user
        non_numeric_columns = []
        for column in self.df.columns:
            if not pd.api.types.is_numeric_dtype(self.df[column]):
                non_numeric_columns.append(column)
                del self.df[column]
        if non_numeric_columns:
            non_numeric_columns_str = ", ".join(non_numeric_columns)
            messagebox.showwarning("Advertencia",
                                   f"Las columnas no numéricas {non_numeric_columns_str} han sido eliminadas.")

        # Remove missing values
        self.df = self.df.dropna()

        # Remove duplicate rows
        self.df = self.df.drop_duplicates()

        # Normalize the data

        self.df = (self.df - self.df.mean()) / self.df.std()

        # Save the cleaned data in a new DataFrame
        cleaned_data = self.df.copy()

        return cleaned_data
