import tkinter as tk
from tkinter import ttk
from connection import Connection



# Таблица для строк БД
def Table(container):
    columns = ('id', 'title', 'desc', 'datePublished')
    tableFrame = ttk.Treeview(container, show="headings", columns=columns, selectmode="browse")
    tableFrame.heading('#1', text='Id')
    tableFrame.heading('#2', text='Заголовок')
    tableFrame.heading('#3', text='Описание')
    tableFrame.heading('#4', text='Дата публикации')

    tableFrame.pack(expand=True, fill=tk.BOTH, padx=5)

    return tableFrame
