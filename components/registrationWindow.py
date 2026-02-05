import tkinter as tk
from tkinter import messagebox
from database.index import DBManager

class RegistrationWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master=master)

        frame = tk.Frame(self)
        frame.pack(padx=10, pady=10)
        self.grab_set()
        self.title("Регистрация")
        self.resizable(False, False)

        tk.Label(frame, text="Фамилия:").grid(row=0, column=0)
        self.lastnameentry = tk.Entry(frame)
        self.lastnameentry.grid(row=0, column=1)

        tk.Label(frame, text="Имя:").grid(row=1, column=0)
        self.firstnameentry = tk.Entry(frame)
        self.firstnameentry.grid(row=1, column=1)

        tk.Label(frame, text="Отчество:").grid(row=2, column=0)
        self.surenameentry = tk.Entry(frame)
        self.surenameentry.grid(row=2, column=1)

        tk.Label(frame, text="Логин:").grid(row=3, column=0)
        self.loginentry = tk.Entry(frame)
        self.loginentry.grid(row=3, column=1)

        tk.Label(frame, text="Роль:").grid(row=4, column=0)
        self.selected = tk.StringVar()
        options = ["author", "root"]
        self.roleentry = tk.OptionMenu(frame, self.selected, *options)
        self.selected.set(options[0])
        self.roleentry.grid(row=4, column=1, sticky="nswe")

        tk.Label(frame, text="Пароль:").grid(row=5, column=0)
        self.passwordentry = tk.Entry(frame, show="*")
        self.passwordentry.grid(row=5, column=1)

        tk.Label(frame, text="Повторите пароль:").grid(row=6, column=0)
        self.repeatpasswordentry = tk.Entry(frame, show="*")
        self.repeatpasswordentry.grid(row=6, column=1)

        button = tk.Button(frame, text="Регистрация", command= self.registration)
        button.grid(row=7, column=1, sticky="e")

        
    def registration(self):
        

        if self.passwordentry.get() != self.repeatpasswordentry.get():
            messagebox.showerror(title="Ошибка регистрации", message="Пароли должны совпадать")
            return
        data = {
            "lastname": self.lastnameentry.get(),
            "firstname": self.firstnameentry.get(),
            "surename": self.surenameentry.get(),
            "login": self.loginentry.get(),
            "pass": self.passwordentry.get(),
            "role": self.selected.get(),
        }


        
        for item in data:
            if data[item] == '' or item == None:
                messagebox.showerror(title="Ошибка регистрации", message="Введите все поля")
                return


        service = DBManager()
        res = service.registration(data)

        if isinstance(res, str):
            messagebox.showerror(title="Ошибка регистрации", message=res)
        else:
            messagebox.showinfo(title="Инфо", message="Регистрация прошла успешно")
            self.destroy()