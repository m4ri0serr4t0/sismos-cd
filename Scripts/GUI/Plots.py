import matplotlib
import PIL
import tkinter as tk
from tkinter import ttk


class plot(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Plot")
        self.geometry("300x300")

    def run(self):
        self.mainloop()


