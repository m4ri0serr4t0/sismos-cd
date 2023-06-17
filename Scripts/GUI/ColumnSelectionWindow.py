import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox


class ColumnSelectionWindow(tk.Toplevel):
    def __init__(self, columns, callback):
        super().__init__()
        self.title("Selección de Columnas")
        self.resizable(False, False)

        self.callback = callback
        self.columns = columns
        self.selected_columns = []

        self.label = ttk.Label(self, text="Selecciona las columnas:")
        self.label.pack(pady=10)

        for column in columns:
            var = tk.IntVar()
            self.selected_columns.append(var)
            ttk.Checkbutton(self, text=column, variable=var, onvalue=1, offvalue=0).pack()

        self.button = ttk.Button(self, text="Graficar", command=self.on_graph_button)
        self.button.pack(pady=10)



    def on_graph_button(self):
        selected_columns = [column for column, var in zip(self.columns, self.selected_columns) if var.get() == 1]
        if selected_columns:
            self.callback(selected_columns)
            self.destroy()
        else:
            messagebox.showwarning("Advertencia", "Selecciona al menos una columna antes de graficar.")
