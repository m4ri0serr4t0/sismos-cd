import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter import messagebox
import matplotlib
from Scripts.GUI.DataProcessor import DataPreprocessor
from Scripts.GUI.Normalizator import Normalizator

matplotlib.use('TkAgg')
import pandas as pd
from tkinter import ttk
from PIL import ImageTk, Image
import webbrowser
from matplotlib import pyplot as plt
from ResultsWindow import resultWindow
from Scripts.GUI.ColumnSelectionWindow import ColumnSelectionWindow
import numpy as np

def showEmptyFileWarning():
    messagebox.showwarning("Advertencia", "Selecciona un archivo")


def openLink():
    webbrowser.open('https://www.linkedin.com/in/jos%C3%A9-mario-mart%C3%ADnez-serrato-1465b0213/')


class mainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Data Processor")
        self.geometry("500x400")

        self.menu_bar = tk.Menu(self)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Abrir Archivo", command=self.open_file)
        self.file_menu.add_command(label="Guardar Archivo", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.quit)

        self.visualization_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.visualization_menu.add_command(label="Disperssion Plot", command=self.displayPlot)

        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="Contacto", command=openLink)

        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)
        self.menu_bar.add_cascade(label="Visualizacion", menu=self.visualization_menu)
        self.menu_bar.add_cascade(label="Ayuda", menu=self.help_menu)

        self.config(menu=self.menu_bar)

        self.imageFrame = ttk.Frame(self, width=300, height=300)
        self.imageFrame.grid(row=5, column=2, columnspan=3, padx=10, pady=20)

        self.labelBienvenida = ttk.Label(self, text="Welcome to MyJ Data Processor")
        self.labelSelect = ttk.Label(self, text="Select a File to Begin")

        self.labelBienvenida.grid(row=7, column=3, columnspan=5, padx=10, pady=5)
        self.labelSelect.grid(row=8, column=3, columnspan=5, padx=10, pady=5)

        self.imageMyJ = ImageTk.PhotoImage(Image.open("myj.jpg"))
        self.imageLabel = ttk.Label(self.imageFrame, image=self.imageMyJ)
        self.imageLabel.pack()

        self.buttons_frame = ttk.Frame(self)
        self.buttons_frame.grid(row=0, column=4, rowspan=2, padx=10, pady=20, sticky='nsew')
        self.buttons_frame.grid_remove()  # Ocultar el Frame inicialmente

        self.button1 = ttk.Button(self.buttons_frame, text="Preprocesado", command=self.preprocess)
        self.button1.pack(pady=5)

        self.button2 = ttk.Button(self.buttons_frame, text="Validacion Cruzada", command=resultWindow)
        self.button2.pack(pady=5)

        self.button3 = ttk.Button(self.buttons_frame, text="Normalizar Datos")
        self.button3.pack(pady=5)

        self.button4 = ttk.Button(self.buttons_frame, text="Algoritmo")
        self.button4.pack(pady=5)

        self.buttonReset = ttk.Button(self.buttons_frame, text="Eliminar cambios", command=self.reset_file)
        self.buttonReset.pack(pady=10)

        self.original_df = None

        self.headers = []  # Headers del archivo csv
        self.trv = None  # Treeview widget para mostrar los datos

    def run(self):
        self.mainloop()

    def open_file(self):
        global archivo
        archivo = askopenfile(mode='r', filetypes=[('csv File', '*.csv')])  # Abriendo el archivo desde un file explorer
        if archivo is None:  # Si el usuario no selecciona algún archivo
            showEmptyFileWarning()  # Muestra advertencia
        else:
            self.selected_file = archivo.name
            df = pd.read_csv(archivo)
            self.original_df = df.copy()  # Actualiza el DataFrame original
            self.displayContent(df)


    def save_file(self):
        if self.trv:
            file = asksaveasfile(mode='w', defaultextension=".csv", filetypes=[('CSV File', '*.csv')])
            if file is None:
                return  # El usuario canceló la operación de guardado
            else:
                # Obtener los datos del treeview
                data = []
                for child in self.trv.get_children():
                    values = self.trv.item(child, 'values')
                    data.append(values)

                # Obtener los nombres de las columnas del treeview
                headers = self.headers

                # Crear un DataFrame de Pandas con los datos y las columnas
                df = pd.DataFrame(data, columns=headers)

                # Guardar el DataFrame en un archivo CSV
                df.to_csv(file.name, index=False)
                file.close()  # Cierra el archivo

                messagebox.showinfo("Éxito", "El archivo se ha guardado correctamente.")
        else:
            messagebox.showwarning("Advertencia", "No se ha seleccionado ningún archivo.")

    def reset_file(self):
        if self.original_df is not None:
            self.displayContent(self.original_df)
            messagebox.showinfo("Éxito", "Se ha restaurado el archivo original.")
        else:
            messagebox.showwarning("Advertencia", "No se ha cargado ningún archivo original.")

    def displayContent(self, df):

        self.headers = list(df.columns)
        self.hideWelcomeWidgets()
        self.create_treeview(df)
        self.buttons_frame.grid()

    def displayPlot(self):
        if hasattr(self, 'selected_file'):
            df = pd.read_csv(self.selected_file)
            columns = df.columns
            if len(columns) >= 2:
                # Aquí puedes agregar el código para seleccionar las columnas y generar el scatter plot
                column_window = ColumnSelectionWindow(columns, self.plot_selected_columns)
                column_window.mainloop()
            else:
                messagebox.showwarning("Advertencia",
                                       "El archivo seleccionado no tiene suficientes columnas para graficar.")
        else:
            messagebox.showwarning("Advertencia", "No se ha seleccionado ningún archivo.")

    def plot_selected_columns(self, columns):
        df = pd.read_csv(self.selected_file)
        if len(columns) >= 2:  # Verifica si hay al menos dos columnas seleccionadas
            # Verifica si las columnas seleccionadas son numéricas
            numeric_columns = [col for col in columns if np.issubdtype(df[col].dtype, np.number)]
            if len(numeric_columns) == len(columns):
                plt.scatter(df[columns[0]], df[columns[1]])
                plt.xlabel(columns[0])
                plt.ylabel(columns[1])
                plt.title('Diagrama de Dispersión')
                plt.show()
            else:
                messagebox.showwarning("Advertencia", "Las columnas seleccionadas deben ser numéricas.")
        else:
            messagebox.showwarning("Advertencia",
                                   "Selecciona al menos dos columnas para crear un diagrama de dispersión.")

    def preprocess(self):
        if self.selected_file:
            df = pd.read_csv(self.selected_file)
            data_preprocessor = DataPreprocessor(df)
            cleaned_data = data_preprocessor.preprocess()
            self.displayContent(cleaned_data)
            messagebox.showinfo("Éxito", "La limpieza y normalizacion de datos se ha realizado correctamente.")
        else:
            messagebox.showwarning("Advertencia", "No se ha seleccionado ningún archivo.")



    def create_treeview(self, df):
        if self.trv:
            self.trv.destroy()

        self.trv = ttk.Treeview(self, selectmode='browse', show='headings', columns=self.headers)
        self.trv.grid(row=0, column=0, columnspan=3, padx=10, pady=20, sticky='nsew')

        for i in self.headers:
            self.trv.column(i, width=90, anchor='c')
            self.trv.heading(i, text=str(i))

        for index, row in df.iterrows():
            values = row.tolist()
            self.trv.insert("", 'end', values=values)

        # Establecer un ancho fijo para la última columna
        last_column = self.headers[-1]
        self.trv.column(last_column, width=200)

        vsb = ttk.Scrollbar(self, orient="vertical", command=self.trv.yview)
        hsb = ttk.Scrollbar(self, orient="horizontal", command=self.trv.xview)
        vsb.grid(row=0, column=2, sticky='ns')
        hsb.grid(row=1, column=0, columnspan=3, sticky='ew')
        self.trv.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.trv.config(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.trv.bind("<Configure>", self.adjust_scrollbars)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def adjust_scrollbars(self, event=None):
        self.trv.update_idletasks()
        self.trv.yview_moveto(0)
        self.trv.xview_moveto(0)

    def showResultsWindow(self):
        window = resultWindow()
        window.run()

    def hideWelcomeWidgets(self):
        self.imageFrame.grid_forget()
        self.labelBienvenida.grid_forget()
        self.labelSelect.grid_forget()


if __name__ == '__main__':
    main = mainWindow()
    main.run()
