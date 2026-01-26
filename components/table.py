import tkinter as tk
from tkinter import ttk
from database.index import getAllArticles

class table(ttk.Treeview):
    
    def __init__(self, parent=None, **flags):
        super().__init__(parent, **flags)
        # articles = ttk.Treeview(parent, columns=("#", "Title", "Description", "Date"), show="headings")
        # scrollbar = ttk.Scrollbar(parent, orient="vertical", command=articles.yview)
        # self.configure(yscrollcommand=scrollbar.set)

        self.heading("#0", text="hidden")
        self.heading("#", text="№")
        self.heading("Title", text="Заголовок")
        self.heading("Description", text="Описание")
        self.heading("Date", text="Дата публикации")

        self.column("#", anchor=tk.CENTER, width=50, minwidth=50, stretch=False)
        self.column("Title", anchor=tk.W, width=100, minwidth=150, stretch=True)
        self.column("Description", anchor=tk.W, width=150, minwidth=100, stretch=True)
        self.column("Date", anchor=tk.CENTER, width=150, minwidth=100, stretch=True)
        self.grid(row=0, column=0, sticky="nsew", padx=(5,0), pady=5)
        

        self.bind("<ButtonRelease-1>", self.on_select)
        # return articles

    def getAllRows(self):
        data = getAllArticles()
        if data:
            # print(data)
            # self.delete(*self.get_children())

            for index, row in enumerate(data):
                self.insert("", "end", text=str(row[0]), values=(index+1, row[5], row[2], row[3]))
        else:
            return False
        
    def on_select(self):
        print(self.selection())