import tkinter as tk
from components.createWindow import CreateWindow


class Info(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.master = master
        self.row_id = None

        self.textarea = tk.Text(self, state="disabled", wrap="word")

        self.buttons = tk.Frame(self)
        self.delete = tk.Button(self.buttons, text="Удалить", fg="red",)
        self.edit = tk.Button(self.buttons, text="Редактирвать",)

        self.textarea.pack(fill=tk.BOTH, expand=True)
        
        self.delete.pack(side=tk.RIGHT)
        self.edit.pack(side=tk.RIGHT)
        self.buttons.pack(side=tk.BOTTOM, fill=tk.X)


    def dataFlow(self, row):
        self.textarea.config(state="normal")
        self.textarea.delete("1.0", tk.END)
        text = f"Заголовок: {row['title']}\nОписание: {row['description']}\nТекст статьи: {row['text']}\n\nДата публикации: {row['creation_date']}"
        self.textarea.insert(tk.END, text)
        self.textarea.config(state="disabled")