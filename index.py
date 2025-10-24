import tkinter as tk
from tkinter import ttk
from connection import Connection
from components.table import Table
from components.toolbar import Toolbar
from components.editStateWindow import editStateWindow


root = tk.Tk()


def setUp():
    connection = Connection()
    rows = connection.getAll()
    for row in rows:
        list = ( row.id, row.title, row.desc, row.creationDate)
        tableFrame.insert('', tk.END, values=list)


def get_state(event):
    selected_item = event.widget.selection()[0]
    id = event.widget.item(selected_item)['values'][0]
    connection = Connection()
    res = connection.get(id)
    editStateWindow(root, res)

root.title("Панель управления базой данных")
root.geometry("1000x600")
root.minsize(width=600, height=400)



style = ttk.Style()
style.theme_use("vista")

Toolbar(root)


container = tk.Frame(root)
container.pack(fill=tk.BOTH, expand=True, pady=5)


tableFrame = Table(container)
tableFrame.bind('<Double-1>', get_state)



setUp()

root.mainloop()


