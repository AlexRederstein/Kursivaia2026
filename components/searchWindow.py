import tkinter as tk
from database.index import DBManager
from tkinter import messagebox

class SearchWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)

        self.title("Поиск статьи")
        # self.minsize(width=400, height=650)
        self.grab_set()
        self.resizable(False, False)

        self.master = master
        frame = tk.Frame(self)

        frame.columnconfigure(0, uniform="uniform", weight=3)
        frame.columnconfigure(1, uniform="uniform", weight=7)

        keylabel = tk.Label(frame, text="ID статьи:", anchor="e")
        self.keyentry = tk.Entry(frame)

        keylabel.grid(column=0, row=0, sticky="e")
        self.keyentry.grid(column=1, row=0, sticky="we")

        titlelabel = tk.Label(frame, text="Заголовок:", anchor="e")
        self.titleentry = tk.Entry(frame)

        titlelabel.grid(column=0, row=1, sticky="e")
        self.titleentry.grid(column=1, row=1, sticky="we")

        desclabel = tk.Label(frame, text="Описание:", anchor="e")
        self.descentry = tk.Entry(frame)

        desclabel.grid(column=0, row=2, sticky="e")
        self.descentry.grid(column=1, row=2, sticky="we")

        frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        button = tk.Button(frame, text="Искать", anchor='e', command= lambda: self.searchRows())

        if self.master.role == "root":
            autorlabel = tk.Label(frame, text="ID Автора статьи:", anchor="e")
            self.autorentry = tk.Entry(frame)
            autorlabel.grid(column=0, row=3, sticky="e")
            self.autorentry.grid(column=1, row=3, sticky="we")

            button.grid(row=4, column=1, sticky="e", pady=(5,0))
        else:
            button.grid(row=3, column=1, sticky="e", pady=(5,0))


    def searchRows(self):

        if self.master.role == "root":
            data = {
                "article_key": self.keyentry.get(),
                "title": self.titleentry.get(),
                "description": self.descentry.get(),
                "user_key": self.autorentry.get(),
            }
        else:
            data = {
                "article_key": self.keyentry.get(),
                "title": self.titleentry.get(),
                "description": self.descentry.get(),
                "user_key": self.master.user_id,
            } 

        service = DBManager()
        res = service.seacrh(data)
        if res:
            self.master.body.getAllRows(rows=res)
            self.destroy()
        else:
            messagebox.showwarning(title="Предупреждение", message="Статьи не найдены")


        