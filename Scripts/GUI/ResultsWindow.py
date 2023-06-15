import tkinter as tk
from tkinter import ttk
import pandas as pd

class resultWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Results")
        self.geometry("500x400")

    def run(self):
        self.mainloop()


