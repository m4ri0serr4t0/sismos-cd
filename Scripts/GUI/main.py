import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfile
import tkinter as tk
import csv


def open_file():
    file = askopenfile(mode='r', filetypes=[('csv File', '*.csv')])  # Abriendo el archivo desde un file explorer
    if file is None:  # Si el usuario no selecciona algún archivo
        mostrarAdvertencia()  # Muestra advertencia
    else:
        contenido = file.read()
        ventana_principal.mostrar_contenido(contenido)

def load_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def display_csv_data(csv_data):
    root = tk.Tk()
    root.title("CSV Viewer")

    # Create a Text widget to display the CSV data
    text_widget = tk.Text(root)
    text_widget.pack()

    # Insert the CSV data into the Text widget
    for row in csv_data:
        line = '\t'.join(row)  # Use tab as column separator
        text_widget.insert(tk.END, line + '\n')

    root.mainloop()

def mostrarAdvertencia():
    messagebox.showwarning("Advertencia", "Selecciona un archivo")


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Proyecto Final")
        self.geometry("800x500")

        self.menu=tk.Menu(self)
        self.filemenu = tk.Menu(self.menu, tearoff=0)
        self.filemenu.add_command(label="Abrir Archivo", command=open_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Salir", command=self.quit)

        self.menu.add_cascade(label="Archivo", menu=self.filemenu)
        self.config(menu=self.menu)

        self.tools_menu = tk.Menu(self.menu, tearoff=0)
        self.tools_menu.add_command(label="Procesar", command=self.abrir_ventana_secundaria)
        self.menu.add_cascade(label="Herramientas", menu=self.tools_menu)



        self.frame_superior = tk.Frame(self)
        self.frame_superior.pack(side=tk.TOP, pady=20)

        self.scrollbar_y = tk.Scrollbar(self.frame_superior)
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.scrollbar_x = tk.Scrollbar(self.frame_superior, orient=tk.HORIZONTAL)
        self.scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.label_contenido = tk.Text(self.frame_superior, font='Fixedsys', background="gray", wrap=tk.NONE)
        self.label_contenido.pack(pady=5, fill=tk.BOTH, expand=True)

        self.label_contenido.config(yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)
        self.scrollbar_y.config(command=self.label_contenido.yview)
        self.scrollbar_x.config(command=self.label_contenido.xview)

        self.frame_inferior = tk.Frame(self)
        self.frame_inferior.pack(side=tk.BOTTOM, pady=20)


        self.update_idletasks()  # Actualiza la ventana para que los elementos se muestren correctamente centrados

    def abrir_ventana_secundaria(self):
        self.withdraw()  # Oculta la ventana principal
        contenido = self.label_contenido.get("1.0", tk.END)  # Obtiene el contenido del label_contenido
        ventana_secundaria = VentanaSecundaria(self, contenido)
        ventana_secundaria.deiconify()  # Muestra la ventana secundaria

    def mostrar_contenido(self, contenido):
        self.label_contenido.delete("1.0", tk.END)  # Borrar el contenido existente
        self.label_contenido.insert(tk.END, contenido)








class VentanaSecundaria(tk.Toplevel):
    def __init__(self, ventana_principal, contenido):
        super().__init__(ventana_principal)

        self.title("Menu de opciones")
        self.geometry("800x600")

        self.frame_derecho = tk.Frame(self, background="blue")
        self.frame_derecho.pack(side=tk.RIGHT, padx=10, pady=10)

        self.btn_limpieza_datos = tk.Button(self.frame_derecho, text="Limpieza de datos")
        self.btn_limpieza_datos.pack(pady=10)

        self.btn_validacion_cruzada = tk.Button(self.frame_derecho, text="Validacion cruzada")
        self.btn_validacion_cruzada.pack(pady=10)

        self.btn_k_medias = tk.Button(self.frame_derecho, text="K-medias")
        self.btn_k_medias.pack(pady=10)

        self.btn_r_nn = tk.Button(self.frame_derecho, text="R-NN")
        self.btn_r_nn.pack(pady=10)

        self.btn_matriz_confusion = tk.Button(self.frame_derecho, text="Matriz de confusion")
        self.btn_matriz_confusion.pack(pady=10)

        self.btn_regresar = tk.Button(self.frame_derecho, text="Regresar", command=self.cerrar_ventana)
        self.btn_regresar.pack(pady=10)

        self.frame_izquierdo = tk.Frame(self, background="orange")
        self.frame_izquierdo.pack(side=tk.LEFT, padx=10, pady=10)

        self.scrollbar_y2 = tk.Scrollbar(self.frame_izquierdo)
        self.scrollbar_y2.pack(side=tk.RIGHT, fill=tk.Y)

        self.scrollbar_x2 = tk.Scrollbar(self.frame_izquierdo, orient=tk.HORIZONTAL)
        self.scrollbar_x2.pack(side=tk.BOTTOM, fill=tk.X)

        self.label_contenido2 = tk.Text(self.frame_izquierdo, font='Fixedsys', background="gray", wrap=tk.NONE)
        self.label_contenido2.pack(pady=10, fill=tk.BOTH, expand=True)

        self.label_contenido2.config(yscrollcommand=self.scrollbar_y2.set, xscrollcommand=self.scrollbar_x2.set)
        self.scrollbar_y2.config(command=self.label_contenido2.yview)
        self.scrollbar_x2.config(command=self.label_contenido2.xview)

        self.mostrar_contenido(contenido)

    def cerrar_ventana(self):
        self.destroy()  # Cierra la ventana secundaria
        ventana_principal.deiconify()  # Muestra nuevamente la ventana principal

    def mostrar_contenido(self, contenido):
        self.label_contenido2.delete("1.0", tk.END)  # Borra el contenido existente
        self.label_contenido2.insert(tk.END, contenido)


ventana_principal = VentanaPrincipal()
ventana_principal.mainloop()