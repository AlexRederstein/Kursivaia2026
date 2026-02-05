import tkinter as tk
from components.table import Table
from components.info import Info
from database.index import DBManager
from components.createWindow import CreateWindow
from tkinter import messagebox 

class Body(tk.Frame):
    def __init__(self, master=None, callback=None):
        super().__init__(master=master)
        self.master = master
        self.callback = callback

        self.columnconfigure(0, weight=1, uniform="equal")
        self.columnconfigure(1, weight=1, uniform="equal")
        self.rowconfigure(0, weight=1)

        self.table = Table(master=self, callback=self.getRow)
        self.table.grid(row=0, column=0, sticky="nsew")
        self.table.bind("<Double-1>", lambda event: self.getRow(event))

        self.info_frame = Info(master=self)
        self.info_frame.grid(row=0, column=1, sticky="nsew")
        

        
        if self.master.role == 'root':
            self.getAllRows()
        else:
            service = DBManager()
            rows = service.getAll(id=self.master.user_id)
            self.getAllRows(rows=rows)


    def getAllRows(self, rows=None):

        self.info_frame.textarea.config(state="normal")
        self.info_frame.textarea.delete('1.0', 'end')
        self.info_frame.textarea.config(state="disabled")

        self.info_frame.delete.config(state="disabled")
        self.info_frame.edit.config(state="disabled")

        self.table.delete(*self.table.get_children())
        
        if rows:

            for index, item in enumerate(rows):
                self.table.insert(
                    "", 
                    "end", 
                    text=str(item['article_key']),
                    values=(
                        index + 1,
                        item['title'],
                        item['description'],
                        item['creation_date']
                    )
                )
        else:
            service = DBManager()
            data = service.getAll()
            if data:
                self.info_frame.textarea.config(state="normal")
                self.info_frame.textarea.delete('1.0', 'end')
                self.info_frame.textarea.config(state="disabled")
                self.table.delete(*self.table.get_children())

                for index, item in enumerate(data):
                    self.table.insert(
                        "", 
                        "end", 
                        text=str(item['article_key']),
                        values=(
                            index + 1,
                            item['title'],
                            item['description'],
                            item['creation_date']
                        )
                    )
            
        
    def getRow(self, event):
        selection = self.table.selection()[0]
        if selection:
            self.info_frame.row_id = self.table.item(selection)["text"]
            service = DBManager()
            row = service.getRow(self.info_frame.row_id)
            self.info_frame.dataFlow(row[0])

            self.info_frame.delete.config(state="normal")
            self.info_frame.edit.config(state="normal")
            self.info_frame.delete.config(command=lambda: self.deleteRow(event=event))
            self.info_frame.edit.config(command=lambda: self.editRow(row=row[0]))

    def editRow(self, row):
        CreateWindow(master = self.master, data = row)

    def deleteRow(self, event):
        confirm = messagebox.askyesno(title="Подтверждение", message="Вы действительно хотите удалить статью?")
        if confirm:
            service = DBManager()
            res = service.delete(self.info_frame.row_id)
            if res:
                messagebox.showinfo(title="Инфо", message="Статья была удалена")
                self.getAllRows()
        else:
            return