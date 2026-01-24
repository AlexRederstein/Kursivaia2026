from tkinter import Frame, Button, BOTH, LEFT, Y, CENTER, W, Label
from tkinter.ttk import Treeview

def body():
    frame = Frame(bg="lightgrey")
    frame.pack(expand=True, fill=BOTH)
    frame.columnconfigure(0, weight=1, minsize=200)
    frame.columnconfigure(1, weight=1, minsize=200)
    frame.rowconfigure(0, weight=1)
    
    info_frame = Frame(frame)

    text = "Lorem "
    label = Label(info_frame, text=text)
    label.pack()
    # info_frame

    articles = Treeview(frame, columns=("#", "Title", "Description", "Date"), show="headings")

    articles.heading("#", text="№")
    articles.heading("Title", text="Заголовок")
    articles.heading("Description", text="Описание")
    articles.heading("Date", text="Дата публикации")

    articles.column("#", anchor=CENTER, width=50, minwidth=50, stretch=False)
    articles.column("Title", anchor=W, width=100, minwidth=150, stretch=True)
    articles.column("Description", anchor=W, width=150, minwidth=100, stretch=True)
    articles.column("Date", anchor=CENTER, width=150, minwidth=100, stretch=False)
    
    articles.grid(row=0, column=0, sticky="nswe")
    info_frame.grid(row=0, column=1, sticky="nswe")

    return frame
