import os
import tkinter
import tkinter as tk
from random import random
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter import messagebox
import matplotlib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler

from Scripts.GUI.CrossValidation import CrossValidationInfoWindow
from Scripts.GUI.DataProcessor import DataPreprocessor
from Scripts.GUI.DeltaRule import ReglaDelta
from Scripts.GUI.IterationsWindow import IterationsWindow


matplotlib.use('TkAgg')
import pandas as pd
from tkinter import ttk
from PIL import ImageTk, Image
import webbrowser
from matplotlib import pyplot as plt
from ResultsWindow import resultWindow
from Scripts.GUI.ColumnSelectionWindow import ColumnSelectionWindow
import numpy as np
from tkinter import simpledialog


def showEmptyFileWarning():
    messagebox.showwarning("Advertencia", "Selecciona un archivo")


def openLink():
    webbrowser.open('https://www.linkedin.com/in/jos%C3%A9-mario-mart%C3%ADnez-serrato-1465b0213/')



class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.train_test_sets = None
        self.title("MyJ Data Processor")
        self.geometry("390x300")

        icon = ImageTk.PhotoImage(Image.open("myj.ico"))

        # Establecer el icono de la ventana principal
        self.iconphoto(True, icon)

        self.menu_bar = tk.Menu(self)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Abrir Archivo", command=self.open_file)
        self.file_menu.add_command(label="Guardar Archivo", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.quit)

        self.preprocess_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.preprocess_menu.add_command(label="Preprocesar", command=self.preprocess)
        self.preprocess_menu.add_command(label="Validación Cruzada", command=self.perform_cross_validation)

        self.visualization_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.visualization_menu.add_command(label="Disperssion Plot", command=self.displayDisperssionPlot)


        self.classify_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.classify_menu.add_command(label="Clasificar",
                                       state=tk.DISABLED, command=self.rna_classify)  # Opción deshabilitada inicialmente

        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="Contacto", command=openLink)

        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)
        self.menu_bar.add_cascade(label="Preprocesado", menu=self.preprocess_menu)
        self.menu_bar.add_cascade(label="Clasificacion", menu=self.classify_menu)
        self.menu_bar.add_cascade(label="Visualizacion", menu=self.visualization_menu)

        self.menu_bar.add_cascade(label="Ayuda", menu=self.help_menu)

        self.config(menu=self.menu_bar)

        self.imageFrame = ttk.Frame(self, width=400, height=400)
        self.imageFrame.grid(row=5, column=14, columnspan=3, padx=10, pady=20)

        self.labelBienvenida = ttk.Label(self, text="Welcome to MyJ Data Processor by Mario Martinez y Juan Zarate!")
        self.labelSelect = ttk.Label(self, text="Open a CSV File to Begin")

        self.labelBienvenida.grid(row=9, column=13, columnspan=5, padx=10, pady=5, )
        self.labelSelect.grid(row=11, column=13, columnspan=5, padx=10, pady=5)

        self.imageMyJ = ImageTk.PhotoImage(Image.open("myj.jpg"))
        self.imageLabel = ttk.Label(self.imageFrame, image=self.imageMyJ)
        self.imageLabel.pack()

        self.buttons_table_frame = ttk.Frame(self)
        self.buttons_table_frame.grid(row=0, column=4, rowspan=2, padx=10, pady=20, sticky='nsew')
        self.buttons_table_frame.grid_remove()

        # self.file_table = ttk.Treeview(self.buttons_table_frame, selectmode='browse', show='headings', columns=['Nombre'])
        # self.file_table.heading('Nombre', text='Nombre del Archivo')
        # .file_table.pack(pady=5)

        self.buttons_frame = ttk.Frame(self.buttons_table_frame)
        self.buttons_frame.pack(pady=5)

        # self.buttons_frame.grid(row=0, column=4, rowspan=2, padx=10, pady=20, sticky='nsew')
        # self.buttons_frame.grid_remove()  # Ocultar el Frame inicialmente

        # self.button4 = ttk.Button(self.buttons_frame, text="Algoritmo")
        # self.button4.pack(pady=5)

        self.buttonReset = ttk.Button(self.buttons_frame, text="Eliminar cambios", command=self.reset_file)
        self.buttonReset.pack(pady=40)

        self.original_df = None
        self.processed_df = None
        self.cleaned_data = None

        self.label_file_name = None

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
            self.geometry("500x400")
            if self.label_file_name:
                self.label_file_name.pack_forget()

            self.selected_file = archivo.name
            df = pd.read_csv(archivo)
            self.original_df = df.copy()

            self.file_name = os.path.basename(self.selected_file)
            self.label_file_name = ttk.Label(self.buttons_table_frame, text="Archivo: " + self.file_name)
            self.label_file_name.pack(pady=5)
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
        if self.selected_file:
            original_file = self.selected_file.replace("processed_", "")
            df = pd.read_csv(original_file)
            self.cleaned_data = None  # Restablece los datos preprocesados a None
            self.displayContent(df)  # Muestra el archivo original en el Treeview
            self.selected_file = original_file  # Restablece el archivo seleccionado al original

            self.classify_menu.entryconfig("Clasificar", state=tk.DISABLED)
            self.cross_validation_done = False

            # Obtener el nombre del archivo sin la ruta completa

            messagebox.showinfo("Éxito", "Se han eliminado los cambios y se ha restaurado el archivo original.")
        else:
            messagebox.showwarning("Advertencia", "No se ha cargado ningún archivo original.")

    def displayContent(self, df):

        self.headers = list(df.columns)
        self.hideWelcomeWidgets()
        self.create_treeview(df)
        self.buttons_table_frame.grid()

    def displayDisperssionPlot(self):
        if hasattr(self, 'selected_file'):
            selected_file = self.selected_file.replace("\\", "/")
            df = pd.read_csv(selected_file)
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
        if hasattr(self, 'selected_file'):
            self.selected_file = self.selected_file.replace("\\", "/")
            df = pd.read_csv(self.selected_file)
            data_preprocessor = DataPreprocessor(df)
            cleaned_data = data_preprocessor.preprocess()
            self.cleaned_data = cleaned_data.copy()  # Almacena los datos preprocesados
            processed_file = os.path.join(
                "processed_" + os.path.basename(self.selected_file))  # Genera la ruta del archivo procesado
            cleaned_data.to_csv(processed_file, index=False)  # Guarda los datos preprocesados en un archivo CSV
            self.displayContent(cleaned_data)  # Muestra los datos preprocesados en el Treeview
            messagebox.showinfo("Éxito", "La limpieza y normalización de datos se ha realizado correctamente.")
        else:
            messagebox.showwarning("Advertencia", "No se ha seleccionado ningún archivo.")

    def perform_cross_validation(self):
        if self.cleaned_data is not None:
            iterations_window = IterationsWindow(self)
            self.wait_window(iterations_window)
            iterations = iterations_window.result

            if iterations is not None:
                kf = KFold(n_splits=iterations, shuffle=True)
                train_test_sets = []
                scaler = StandardScaler()  # Instanciar el objeto StandardScaler

                for train_index, test_index in kf.split(self.cleaned_data):
                    train_set = self.cleaned_data.iloc[train_index]
                    test_set = self.cleaned_data.iloc[test_index]

                    # Aplicar la normalización estándar a los conjuntos de entrenamiento y prueba
                    train_set_normalized = scaler.fit_transform(train_set)
                    test_set_normalized = scaler.transform(test_set)

                    train_test_sets.append((train_set_normalized, test_set_normalized))

                self.train_test_sets = train_test_sets  # Almacena los conjuntos de entrenamiento y prueba
                print(train_test_sets)

                # Habilitar la pestaña "Clasificar"
                self.classify_menu.entryconfig("Clasificar", state=tk.NORMAL)

                # Mostrar un mensaje de éxito
                messagebox.showinfo("Éxito", "La validación cruzada se ha completado correctamente.")
                self.show_cross_validation_info()
        else:
            messagebox.showwarning("Advertencia", "No se han preprocesado los datos.")

    def show_cross_validation_info(self):
        if self.train_test_sets is not None:
            info_window = tk.Toplevel(self)
            info_window.title("Información de Validación Cruzada")

            scrollbar = tk.Scrollbar(info_window)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            text = tk.Text(info_window, height=20, width=50, yscrollcommand=scrollbar.set)
            text.pack(side=tk.LEFT, fill=tk.BOTH)

            scrollbar.config(command=text.yview)

            for i, (train_set, test_set) in enumerate(self.train_test_sets):
                iteration_label = tk.Label(text, text=f"Iteración {i + 1}")
                text.window_create(tk.END, window=iteration_label)
                text.insert(tk.END, '\n')

                train_label = tk.Label(text, text="Conjunto de Entrenamiento:")
                text.window_create(tk.END, window=train_label)
                text.insert(tk.END, '\n')

                train_text = tk.Text(text, height=10, width=50)
                train_text.insert(tk.END, str(train_set))
                text.window_create(tk.END, window=train_text)
                text.insert(tk.END, '\n')

                test_label = tk.Label(text, text="Conjunto de Prueba:")
                text.window_create(tk.END, window=test_label)
                text.insert(tk.END, '\n')

                test_text = tk.Text(text, height=10, width=50)
                test_text.insert(tk.END, str(test_set))
                text.window_create(tk.END, window=test_text)
                text.insert(tk.END, '\n')

                separator = tk.Label(text, text="-----------------------")
                text.window_create(tk.END, window=separator)
                text.insert(tk.END, '\n')

    def rna_classify(self):
        if hasattr(self, 'train_test_sets'):
            for train_test_set in self.train_test_sets:
                train_set, test_set = train_test_set  # Desempaquetar los conjuntos de entrenamiento y prueba
                X_train = train_set[:, :-1]
                y_train = train_set[:, -1]
                X_test = test_set[:, :-1]
                y_test = test_set[:, -1]

                self.rna_classify_with_sets(X_train, y_train, X_test, y_test)
        else:
            messagebox.showwarning("Advertencia",
                                   "No se han realizado la validación cruzada o no se han preprocesado los datos.")

    def rna_classify_with_sets(self, X_train, y_train, X_test, y_test):
        # Crear una instancia de ReglaDelta
        regla_delta = ReglaDelta(input_size=X_train.shape[1], learning_rate=0.1)

        # Entrenar la red neuronal
        regla_delta.train(X_train, y_train, epochs=100)
        regla_delta.train(X_train, y_train, epochs=100)

        # Guardar los resultados en un nuevo archivo CSV
        results = {'Error cuadrático': regla_delta.errors}
        df_results = pd.DataFrame(results)
        #df_results.to_csv('resultadosGrecia.csv', index=False)

        # Graficar la evolución del error durante el entrenamiento
        regla_delta.plot_errors()

        # Contar los errores en la clasificación
        errors = regla_delta.count_errors(X_test, y_test)
        try:
            messagebox.showinfo("Número de errores", f"Número de errores en la clasificación: {errors}")
        except tkinter.TclError:
            pass


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
    main = MainWindow()
    main.run()
