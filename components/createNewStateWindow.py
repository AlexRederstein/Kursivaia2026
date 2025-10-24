import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from connection import Connection
import datetime


def createNewStateWindow(container):
    window = tk.Toplevel(container)
    window.title("Создание новой записи")
    window.minsize(width=400, height=650)
    window.grab_set()


    style = ttk.Style()
    style.theme_use("vista")
    window.resizable(False, False)


    titleframe = ttk.Frame(window)
    titleframe.pack(side=tk.TOP, pady=10, padx=5, anchor=tk.W)

    descframe = ttk.Frame(window)
    descframe.pack(side=tk.TOP, pady=10, padx=5, anchor=tk.W)

    textframe = ttk.Frame(window)
    textframe.pack(fill=tk.BOTH, pady=10, padx=5, expand=True)

    # Поля для ввода

    labeltitle = ttk.Label(titleframe, text="Заголовок:")
    inputtitle = tk.Text(titleframe, width=50, height=1)

    labeldesc = ttk.Label(descframe, text="Описание:")
    inputdesc = tk.Text(descframe, width=50, height=4)

    labeltext = ttk.Label(textframe, text="Текст статьи:")
    inputtext = tk.Text(textframe, width=50)

    labeltitle.pack(side=tk.TOP, anchor=tk.NW)
    inputtitle.pack(side=tk.BOTTOM, anchor=tk.CENTER)

    labeldesc.pack(side=tk.TOP, anchor=tk.NW)
    inputdesc.pack(side=tk.BOTTOM, anchor=tk.W)

    labeltext.pack(side=tk.TOP, anchor=tk.NW)
    inputtext.pack(fill=tk.BOTH, expand=True)

    # Нижняя панель окна

    bottompanel = ttk.Frame(window)
    bottompanel.pack(side=tk.BOTTOM, fill=tk.X, pady=10, padx=5)

    bottompanel_button_send = ttk.Button(bottompanel, text="Сохранить статью", command=lambda: sendState(inputtitle, inputdesc, inputtext))
    bottompanel_button_cancel = ttk.Button(bottompanel, text="Отмена", command=window.destroy)

    bottompanel_button_send.pack(side=tk.RIGHT)
    bottompanel_button_cancel.pack(side=tk.RIGHT)


def sendState(title, desc, text):
    data = {
        "title": title.get("1.0", tk.END),
        "desc": desc.get("1.0", tk.END),
        "text": text.get("1.0", tk.END),
        "creationDate": datetime.datetime.now()
    }

    connection = Connection('states')
    connection.create(data)
    messagebox.showinfo('Уведомление','Запись была создана')