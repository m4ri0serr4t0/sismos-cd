import tkinter as tk
from tkinter.filedialog import askopenfile
from tkinter import messagebox
import pandas as pd
from tkinter import ttk
from PIL import ImageTk, Image

from ResultsWindow import resultWindow

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

        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="Contacto", command=self.openLink)

        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)
        self.menu_bar.add_cascade(label="Ayuda", menu=self.help_menu)
        self.config(menu=self.menu_bar)


        self.imageFrame = ttk.Frame(self, width=300, height=300)
        self.imageFrame.pack()
        self.imageFrame.place(anchor='center', relx=0.5, rely=0.5)

        self.imageMyJ = ImageTk.PhotoImage(Image.open("myj.jpg"))
        self.imageLabel = ttk.Label(self.imageFrame, image=self.imageMyJ)

        self.headers = []  # Headers del archivo csv
        self.trv = None  # Treeview widget para mostrar los datos

    def run(self):
        self.mainloop()

    def open_file(self):
        file = askopenfile(mode='r', filetypes=[('csv File', '*.csv')])  # Abriendo el archivo desde un file explorer
        if file is None:  # Si el usuario no selecciona algún archivo
            self.showEmptyFileWarning()  # Muestra advertencia
        else:
            self.displayContent(file)

    def showEmptyFileWarning(self):
        messagebox.showwarning("Advertencia", "Selecciona un archivo")

    def openLink(self):
        pass

    def displayContent(self, file):
        global df
        df = pd.read_csv(file)
        self.headers = list(df.columns)
        self.create_treeview()

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

        vsb = ttk.Scrollbar(self, orient="vertical", command=self.trv.yview)
        hsb = ttk.Scrollbar(self, orient="horizontal", command=self.trv.xview)
        vsb.grid(row=0, column=2, sticky='ns')
        hsb.grid(row=1, column=0, columnspan=3, sticky='ew')
        self.trv.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.trv.config(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.trv.bind("<Configure>", self.adjust_scrollbars)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.button = ttk.Button(self, text="Procesar")
        self.button.grid(row=1, column=3, padx=10, pady=5)

        self.button2 = ttk.Button(self, text="Procesar2", command=showResultWindow)
        self.button2.grid(row=2, column=3, padx=10, pady=5)

        self.button3 = ttk.Button(self, text="Procesar3")
        self.button3.grid(row=3, column=3, padx=10, pady=5)

    def adjust_scrollbars(self, event=None):
        self.trv.update_idletasks()
        self.trv.yview_moveto(0)
        self.trv.xview_moveto(0)

if __name__ == '__main__':

    main = mainWindow()
    #main.run()
    test = resultWindow()
    test.run()
