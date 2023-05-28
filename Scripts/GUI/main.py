from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile
import tkinter as tk


def open_file():
    """
    Esta función abre el archivo tipo asm y ejecuta las ventana para el analizador léxico""
    :return:
    """
    file = askopenfile(mode='r',
                       filetypes=[('Conjunto de Datos', '*.txt')])  # Abirendo el archivo desde un file explorer
    if file is None:  # Si el usuario no selecciona algún archivo
        mostrarAdvertencia()  # Muestra advertencia
    else:
        pass



def mostrarAdvertencia():
    messagebox.showwarning("Advertencia", "Selecciona un archivo")



class Vista:

    def __init__(self, root, title, geometry):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)  # sizexsize
        # self.root.iconbitmap(icon)

        label = Label(self.root, text="Preprocesador de Datos", font='Fixedsys', width=100, height=4, fg="black")
        label.pack()

        btn = Button(self.root, text='Abrir Archivo', font='Fixedsys', background="green", command=lambda: open_file())
        btn.pack()

        btn2 = Button(self.root, text='   Salir    ', font='Fixedsys', background="red",
                      command=lambda: self.root.destroy())  # lo hizo juan
        btn2.pack()

        label3 = Label(self.root, text="Juan Y Mario", font='Fixedsys', width=100, height=4, fg="black")
        label3.pack(side=BOTTOM)

        self.root.mainloop()


# _rutaIcono = 'asm.ico'
if __name__ == '__main__':
    root = Tk()
    vista = Vista(root, 'Proyecto Ciencia de Datos', '600x200')
