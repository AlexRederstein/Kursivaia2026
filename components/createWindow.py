import tkinter as tk
from tkinter import ttk
from database.index import DBManager
from tkinter import messagebox

class CreateWindow(tk.Toplevel):
    def __init__(self, master = None, data = None):
        super().__init__(master=master)
        self.resizable(False, False)
        if data:
            self.title("Редактирование записи")
        else:
            self.title("Создание записи")
        self.minsize(width=400, height=650)
        self.grab_set()

        frame = tk.Frame(self)

        frame.columnconfigure(0, uniform="uniform", weight=3)
        frame.columnconfigure(1, uniform="uniform", weight=7)
        frame.rowconfigure(3, weight=1)

        titlelabel = tk.Label(frame, text="Заголовок:", anchor="e")
        self.titleentry = tk.Entry(frame)

        titlelabel.grid(column=0, row=0, sticky="e")
        self.titleentry.grid(column=1, row=0, sticky="we")

        desclabel = tk.Label(frame, text="Описание:", anchor="e")
        self.descentry = tk.Entry(frame)

        desclabel.grid(column=0, row=1, sticky="e")
        self.descentry.grid(column=1, row=1, sticky="we")

        textlabel = tk.Label(frame, text="Текст статьи:")
        self.textentry = tk.Text(frame)

        textlabel.grid(column=0, row=2, sticky="w")
        self.textentry.grid(column=0, row=3, columnspan=2, sticky="nsew")

        frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        if data:
            self.titleentry.insert(0, data["title"])
            self.descentry.insert(0, data["description"])
            self.textentry.insert("1.0", data["text"])
            save = tk.Button(frame, text="Обновить", anchor='e', command= lambda: self.updateData(data['article_key']))
        else:
            save = tk.Button(frame, text="Сохранить", anchor='e', command= self.pushData)

        save.grid(row=4, column=1, sticky="e", pady=(5,0))



    def pushData(self):
        data = {
            'title': self.titleentry.get(),
            'description': self.descentry.get(),
            'text': self.textentry.get("1.0", tk.END).rstrip('\n'),
            'user_key': self.master.user_id
        }
        service = DBManager()
        res = service.push(data)

        if res:
            messagebox.showinfo(title="Инфо", message="Статья сохранена")
            self.master.body.getAllRows()
            self.destroy()

    def updateData(self, id):
        data = {
            'title': self.titleentry.get(),
            'description': self.descentry.get(),
            'text': self.textentry.get("1.0", tk.END).rstrip('\n'),
            'user_key': self.master.user_id
        }
        service = DBManager()
        res = service.update(data, id)

        if res:
            messagebox.showinfo(title="Инфо", message="Статья обновлена")
            self.master.body.getAllRows()
            self.destroy()