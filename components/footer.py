from tkinter import Frame, Button

def footer():
    frame = Frame()
    btn = Button(frame, text="text")
    btn.pack()
    frame.pack()
    return frame