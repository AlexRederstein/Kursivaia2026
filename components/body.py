from tkinter import Frame, Button, BOTH, LEFT, RIGHT, Y, X, CENTER, W, Label, Text, WORD, END, BOTTOM
from tkinter.ttk import Treeview, Scrollbar, Style
from database.index import getAllArticles, getArticle, deleteArticle
from components.createFrame import open_create_frame
from textwrap import dedent
from components.table import table
from components.info_frame import info_frame

row_id = None

def body():

    frame = Frame()
    frame.pack(expand=True, fill=BOTH)
    frame.columnconfigure(0, weight=1, uniform="equal")
    frame.columnconfigure(1, weight=1, uniform="equal")
    frame.rowconfigure(0, weight=1)

    articles = table(frame)
    articles.getAllRows()

    info = info_frame(frame)
    info.grid(row=0, column=1, sticky="nsew", padx=(0, 5), pady=5)

    return frame

    # def on_select(event):
    #     selection = articles.selection()
    #     if selection:
    #         item_id = selection[0]
            
    #         global row_id
    #         row_id = articles.item(item_id)["text"]
    #         print(row_id)
    #         res = getArticle(str(row_id))
    #         if res:
    #             info_text.config(state='normal')
    #             info_text.delete("1.0", END)
    #             article = dedent(f"""
    #                             Заголовок: {res[5]}
    #                             Описание: {res[2]}
    #                             Текст статьи: {res[1]}
    #                             Дата публикации: {res[3]}
    #                             """)
    #             update.config(command=lambda: open_create_frame(res))
    #             info_text.insert("1.0", article)
    #             info_text.config(state='disabled') 
                
            
    
    # articles.bind("<ButtonRelease-1>", on_select)
    # flowRows(articles)

    


# def flowRows(table):
#     data = getAllArticles()
#     table.delete(*table.get_children())
#     if data:
#         for index, row in enumerate(data):
#             table.insert("", "end", text=str(row[0]), values=(index+1, row[5], row[2], row[3]))
#     else:
#         return False

# def pullArticle(article):
#     pass
