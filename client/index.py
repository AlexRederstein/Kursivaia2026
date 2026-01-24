import tkinter as tk
from tkinter import Frame, Button
from tkinter import ttk

from components.header import header 
from components.body import body 
from components.footer import footer 


root = tk.Tk()

root.title("Панель управления базой данных")
root.geometry("1000x600")
style = ttk.Style()
style.theme_use("vista")
root.minsize(width=600, height=400)

# Компоненты
header = header()
body = body()
# footer = footer()

root.mainloop()


