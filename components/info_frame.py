import tkinter as tk


def info_frame(frame):
    info_frame = tk.Frame(frame)
    info_text = tk.Text(info_frame, state='disabled', wrap="word")
    buttons = tk.Frame(info_frame)
    delete = tk.Button(buttons, text="Удалить", fg="red")
    update = tk.Button(buttons, text="Редактирвать")

    buttons.pack(side=tk.BOTTOM, fill=tk.X)
    delete.pack(side=tk.RIGHT)
    update.pack(side=tk.RIGHT)

    info_text.pack(fill=tk.BOTH, expand=True)
    return info_frame