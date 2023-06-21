import tkinter as tk
from tkinter import ttk


class CrossValidationInfoWindow(tk.Toplevel):
    def __init__(self, parent, train_test_sets, headers):
        super().__init__(parent)
        self.title("Información de Validación Cruzada")
        self.geometry("500x400")

        self.train_test_sets = train_test_sets
        self.headers = headers

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self)
        frame.pack(padx=10, pady=10, fill='both', expand=True)

        for i, (train_set, test_set) in enumerate(self.train_test_sets):
            train_treeview = ttk.Treeview(frame, selectmode='browse', show='headings', columns=self.headers)
            train_treeview.grid(row=0, column=i, padx=10, pady=10, sticky='nsew')

            for header in self.headers:
                train_treeview.column(header, width=90, anchor='c')
                train_treeview.heading(header, text=header)

            for index, row in enumerate(train_set):
                train_treeview.insert("", 'end', values=row)

            train_vsb = ttk.Scrollbar(frame, orient="vertical", command=train_treeview.yview)
            train_hsb = ttk.Scrollbar(frame, orient="horizontal", command=train_treeview.xview)
            train_vsb.grid(row=0, column=i + 1, sticky='ns')
            train_hsb.grid(row=1, column=i, columnspan=2, sticky='ew')
            train_treeview.configure(yscrollcommand=train_vsb.set, xscrollcommand=train_hsb.set)
            train_treeview.config(yscrollcommand=train_vsb.set, xscrollcommand=train_hsb.set)
            train_treeview.bind("<Configure>", self.adjust_scrollbars)

            test_treeview = ttk.Treeview(frame, selectmode='browse', show='headings', columns=self.headers)
            test_treeview.grid(row=2, column=i, padx=10, pady=10, sticky='nsew')

            for header in self.headers:
                test_treeview.column(header, width=90, anchor='c')
                test_treeview.heading(header, text=header)

            for index, row in enumerate(test_set):
                test_treeview.insert("", 'end', values=row)

            test_vsb = ttk.Scrollbar(frame, orient="vertical", command=test_treeview.yview)
            test_hsb = ttk.Scrollbar(frame, orient="horizontal", command=test_treeview.xview)
            test_vsb.grid(row=2, column=i + 1, sticky='ns')
            test_hsb.grid(row=3, column=i, columnspan=2, sticky='ew')
            test_treeview.configure(yscrollcommand=test_vsb.set, xscrollcommand=test_hsb.set)
            test_treeview.config(yscrollcommand=test_vsb.set, xscrollcommand=test_hsb.set)
            test_treeview.bind("<Configure>", self.adjust_scrollbars)

    def adjust_scrollbars(self, event):
        for child in self.winfo_children():
            if isinstance(child, ttk.Treeview):
                child.configure(scrollregion=child.bbox("all"))
