from tkinter import Frame, Button, LEFT, TOP, RIGHT, X

def header():
    frame = Frame()
    search = Button(frame, text="Открыть статью...")
    create = Button(frame, text="Создать статью...")
    user = Button(frame, text="Пользователь")
    search.pack(side=LEFT)
    create.pack(side=LEFT)
    user.pack(side=RIGHT)
    frame.pack(side=TOP, fill=X)
    return frame