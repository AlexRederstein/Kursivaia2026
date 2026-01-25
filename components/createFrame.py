import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import datetime
from database.index import pushData, updateData

import os
import sys

def setInput(container, title = ''):
    frame = tk.Frame(container)
    label = ttk.Label(frame, text=f"{title}:")
    input = tk.Entry(frame)
    label.pack(side=tk.LEFT, padx=(0, 5))
    input.pack(expand=True, fill=tk.X)
    frame.pack(fill=tk.X, pady=(5,0), padx=(5,5))
    return input

def setTextArea(container, title = ''):
    frame = tk.Frame(container)
    label = ttk.Label(frame, text=f"{title}:")
    textArea = tk.Text(frame, width=50)
    label.grid(row=0, column=0)
    textArea.grid(row=1, column=0)
    frame.pack(fill=tk.BOTH, padx=5, pady=(0, 5))
    return textArea

def open_create_frame(data = False):
    window = tk.Toplevel()
    window.title("Создание новой записи")
    window.minsize(width=400, height=650)
    window.grab_set()

    header = setInput(window, 'Заголовок')
    desc = setInput(window, 'Описание')
    text = setTextArea(window, 'Текст статьи')

    buttons = tk.Frame(window)
    sendButton = tk.Button(buttons, text='Сохранить', command=lambda: sendData(header, desc, text))
    sendButton.pack(side=tk.RIGHT)
    buttons.pack(side=tk.BOTTOM, fill=tk.X, pady=5, padx=5)

    if(data):
        print(data)
        header.insert(0, data[5])
        desc.insert(0, data[2])
        text.insert("1.0", data[1])

    def sendData(header, desc, text):
        row = {
            "title": header.get(),
            "description": desc.get(),
            "text": text.get("1.0", tk.END)
        }

        if data:
            # print(str(data[0]))
            updateData(row, str(data[0]))
        else:
            pushData(row)
        
        python = sys.executable
        os.execl(python, python, *sys.argv)
        


    # style = ttk.Style()
    # style.theme_use("vista")


    # titleframe = ttk.Frame(window)
    # titleframe.pack(side=tk.TOP, pady=10, padx=5, anchor=tk.W)


    # descframe = ttk.Frame(window)
    # descframe.pack(side=tk.TOP, pady=10, padx=5, anchor=tk.W)

    # textframe = ttk.Frame(window)
    # textframe.pack(fill=tk.BOTH, pady=10, padx=5, expand=True)

    # # Поля для ввода

    # labeltitle = ttk.Label(titleframe, text="Заголовок:")
    # inputtitle = tk.Text(titleframe, width=50, height=1)
    # inputtitle.insert("1.0", data.title)
    

    # labeldesc = ttk.Label(descframe, text="Описание:")
    # inputdesc = tk.Text(descframe, width=50, height=4)
    # inputdesc.insert("1.0", data.desc)
    

    # labeltext = ttk.Label(textframe, text="Текст статьи:")
    # inputtext = tk.Text(textframe, width=50)
    # inputtext.insert("1.0", data.text)
    

    # labeltitle.pack(side=tk.TOP, anchor=tk.NW)
    # inputtitle.pack(side=tk.BOTTOM, anchor=tk.CENTER)

    # labeldesc.pack(side=tk.TOP, anchor=tk.NW)
    # inputdesc.pack(side=tk.BOTTOM, anchor=tk.W)

    # labeltext.pack(side=tk.TOP, anchor=tk.NW)
    # inputtext.pack(fill=tk.BOTH, expand=True)

    # Нижняя панель окна

    # bottompanel = ttk.Frame(window)
    # bottompanel.pack(side=tk.BOTTOM, fill=tk.X, pady=10, padx=5)

    # bottompanel_button_send = ttk.Button(bottompanel, text="Сохранить статью", command=lambda: updateState(inputtitle, inputdesc, inputtext))
    # bottompanel_button_cancel = ttk.Button(bottompanel, text="Отмена", command=window.destroy)

    # bottompanel_button_send.pack(side=tk.RIGHT)
    # bottompanel_button_cancel.pack(side=tk.RIGHT)


# def updateState(title, desc, text):
#     pass
    # data = {
    #     "title": title.get("1.0", tk.END),
    #     "desc": desc.get("1.0", tk.END),
    #     "text": text.get("1.0", tk.END),
    #     "creationDate": datetime.datetime.now()
    # }

    # connection = Connection('states')
    # connection.create(data)
    # messagebox.showinfo('Уведомление','Запись была создана')