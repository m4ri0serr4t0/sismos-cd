import tkinter as tk
from tkinter import ttk
import pandas as pd


class resultWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Results")
        self.geometry("500x400")

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

    def adjust_scrollbars(self, event=None):
        self.trv.update_idletasks()
        self.trv.yview_moveto(0)
        self.trv.xview_moveto(0)



    def run(self):
        self.mainloop()
