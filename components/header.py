from tkinter import Frame, Button, LEFT, TOP, RIGHT, X
from tkinter.ttk import Style
from components.createFrame import open_create_frame


def header():
    frame = Frame()
    search = Button(frame, text="Открыть статью...")
    create = Button(frame, text="Создать статью...", command=lambda: open_create_frame())
    user = Button(frame, text="Пользователь")
    search.pack(side=LEFT)
    create.pack(side=LEFT)
    user.pack(side=RIGHT)
    frame.pack(side=TOP, fill=X)



    return frame