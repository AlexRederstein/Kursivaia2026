import tkinter as tk

from components.header import Header 
from components.body import Body
from database.index import DBManager
from tkinter import messagebox

class Main(tk.Tk):
    def __init__(self, user):
        super().__init__()

        self.name = f"{user['lastname']} {user['firstname']} {user['surename']}"
        self.user_id = user['user_id']
        self.role = user['role']

        self.title("Панель управления базой данных")
        self.geometry("1000x600")
        self.minsize(width=600, height=400)

        self.header = Header(master=self)
        self.header.pack(fill=tk.X)

        self.body = Body(master=self)
        self.body.pack(fill=tk.BOTH, expand=True)


class Auth(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Авторизация")
        self.geometry("300x100")
        self.resizable(False, False)

        frame = tk.Frame(self)
        tk.Label(frame, text="Логин:").grid(row=0, column=0)
        self.login_entry = tk.Entry(frame)
        self.login_entry.grid(row=0, column=1, sticky="nsew")

        tk.Label(frame, text="Пароль:").grid(row=1, column=0)
        self.password_entry = tk.Entry(frame, show="*")
        self.password_entry.grid(row=1, column=1, sticky="nsew")

        tk.Button(frame, text="Войти", command=self.authenticate).grid(row=2, column=1, sticky="nsew")

        frame.pack(padx=10, pady=10)
        


    def authenticate(self):
        login = self.login_entry.get()
        password = self.password_entry.get()
        service = DBManager()
        res = service.login(login=login, password=password)
    
        if isinstance(res, str):
            messagebox.showerror(title="Ошибка авторизации", message=res)
        else:
            self.destroy()
            Main(user=res).mainloop()




if __name__ == "__main__":
    app = Auth()
    app.mainloop()