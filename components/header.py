import tkinter as tk
from components.createWindow import CreateWindow
from components.searchWindow import SearchWindow
from components.registrationWindow import RegistrationWindow

class Header(tk.Frame):
    def __init__(self, master=None, callback=None):
        super().__init__(master)
        self.master = master
        self.callback = callback

        search = tk.Button(self, text="Поиск статей...", command=lambda: SearchWindow(self.master))
        create = tk.Button(self, text="Создать статью...", command= lambda: CreateWindow(self.master))
        update = tk.Button(self, text="Обновить таблицу", command= lambda: self.updateRows())

        label = tk.Label(self, text=f"{self.master.role}: {self.master.name}")

        if(self.master.role == 'root'):
            tk.Button(self, text="Добавить пользователя...", command=lambda: RegistrationWindow(self)).pack(side=tk.RIGHT)

        search.pack(side=tk.LEFT)
        create.pack(side=tk.LEFT)
        update.pack(side=tk.LEFT)
        label.pack(side=tk.RIGHT)

    def updateRows(self):
        self.master.body.getAllRows()