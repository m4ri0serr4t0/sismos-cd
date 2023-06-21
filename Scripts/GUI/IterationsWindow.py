import tkinter as tk
from tkinter import messagebox


class IterationsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Número de Iteraciones")
        self.geometry("300x120")
        self.result = None

        self.label = tk.Label(self, text="Ingrese el número de iteraciones: (10)")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self)
        self.entry.pack(pady=5)

        self.button = tk.Button(self, text="Confirmar", command=self.confirm_iterations)
        self.button.pack(pady=10)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def confirm_iterations(self):
        iterations = self.entry.get()
        if iterations.isdigit():
            self.result = int(iterations)
            self.destroy()
        else:
            messagebox.showerror("Error", "Ingrese un número entero válido.")

    def on_close(self):
        self.result = None
        self.destroy()