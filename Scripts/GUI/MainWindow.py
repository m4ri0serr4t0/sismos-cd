import tkinter as tk
from tkinter.filedialog import askopenfile
from tkinter import messagebox

import matplotlib

matplotlib.use('TkAgg')
import pandas as pd
from tkinter import ttk
from PIL import ImageTk, Image
import webbrowser
from matplotlib import pyplot as plt

from ResultsWindow import resultWindow
from Plots import plot
from Scripts.GUI.ColumnSelectionWindow import ColumnSelectionWindow


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
        self.file_menu.add_command(label="Guardar Archivo", command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.quit)

        self.visualization_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.visualization_menu.add_command(label="Plot", command=self.displayPlot)

        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="Contacto", command=openLink)

        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)
        self.menu_bar.add_cascade(label="Visualizacion", menu=self.visualization_menu)
        self.menu_bar.add_cascade(label="Ayuda", menu=self.help_menu)

        self.config(menu=self.menu_bar)

        self.imageFrame = ttk.Frame(self, width=300, height=300)
        self.imageFrame.grid(row=5, column=1, columnspan=3, padx=10, pady=20)

        self.labelBienvenida = ttk.Label(self, text="Bienvenido :)")
        self.labelBienvenida.grid(row=7, column=2, columnspan=3, padx=10, pady=5)

        self.imageMyJ = ImageTk.PhotoImage(Image.open("myj.jpg"))
        self.imageLabel = ttk.Label(self.imageFrame, image=self.imageMyJ)
        self.imageLabel.pack()

        self.buttons_frame = ttk.Frame(self)
        self.buttons_frame.grid(row=0, column=4, rowspan=2, padx=10, pady=20, sticky='nsew')
        self.buttons_frame.grid_remove()  # Ocultar el Frame inicialmente

        self.button1 = ttk.Button(self.buttons_frame, text="Preprocesado", command=resultWindow)
        self.button1.pack(pady=5)

        self.button2 = ttk.Button(self.buttons_frame, text="Validacion Cruzada", command=resultWindow)
        self.button2.pack(pady=5)

        self.button3 = ttk.Button(self.buttons_frame, text="Algoritmo 1")
        self.button3.pack(pady=5)

        self.button4 = ttk.Button(self.buttons_frame, text="Algoritmo 2")
        self.button4.pack(pady=5)

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
            self.displayContent(archivo)

    def displayContent(self, file):
        global df
        df = pd.read_csv(file)
        self.headers = list(df.columns)
        self.hideWelcomeWidgets()
        self.create_treeview()
        self.buttons_frame.grid()

    def displayPlot(self):
        if hasattr(self, 'selected_file'):
            df = pd.read_csv(self.selected_file)
            columns = df.columns
            if len(columns) >= 2:
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
            plt.hist(df[columns], bins=10, alpha=0.5, label=columns)
            plt.xlabel('Valor')
            plt.ylabel('Frecuencia')
            plt.title('Histograma')
            plt.legend()
            plt.show()
        else:
            messagebox.showwarning("Advertencia", "Selecciona al menos dos columnas para crear un histograma.")

    def create_treeview(self):
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


if __name__ == '__main__':
    main = mainWindow()
    main.run()
