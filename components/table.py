import tkinter as tk
from tkinter import ttk
from database.index import DBManager

class Table(ttk.Treeview):
    
    def __init__(self, master=None, callback=None):
        super().__init__(master, columns=("Index", "Title", "Description", "Date"), show="headings")

        self.master = master
        self.heading("#0", text="hidden")
        self.heading("Index", text="№")
        self.heading("Title", text="Заголовок")
        self.heading("Description", text="Описание")
        self.heading("Date", text="Дата публикации")

        self.column("Index", anchor=tk.CENTER, width=50, minwidth=50, stretch=False)
        self.column("Title", anchor=tk.W, width=100, minwidth=150, stretch=True)
        self.column("Description", anchor=tk.W, width=150, minwidth=100, stretch=True)
        self.column("Date", anchor=tk.CENTER, width=150, minwidth=100, stretch=True)