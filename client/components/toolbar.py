import tkinter as tk
from tkinter import ttk
from components.createNewStateWindow import createNewStateWindow

def Toolbar(container):
    
    
    toolbar = tk.Frame(container)
    toolbar.pack(side=tk.TOP, fill=tk.X)
    toolbar_button_open = ttk.Button(toolbar, text="Найти...")
    toolbar_button_open.pack(side=tk.LEFT)
    toolbar_button_search = ttk.Button(toolbar, text="Создать новую запись в таблице", command=lambda: createNewStateWindow(container))
    toolbar_button_search.pack(side=tk.LEFT)