from tkinter import Frame, Button, BOTH, LEFT, RIGHT, Y, X, CENTER, W, Label, Text, WORD, END, BOTTOM
from tkinter.ttk import Treeview, Scrollbar, Style
from database.index import getAllArticles, getArticle, deleteArticle
from components.createFrame import open_create_frame
from textwrap import dedent

row_id = None

def body():

    frame = Frame(bg="lightgrey")
    frame.pack(expand=True, fill=BOTH)
    frame.columnconfigure(0, weight=1, uniform="equal")
    frame.columnconfigure(1, weight=1, uniform="equal")
    frame.rowconfigure(0, weight=1)

    articles = Treeview(frame, columns=("#", "Title", "Description", "Date"), show="headings")
    scrollbar = Scrollbar(articles, orient="vertical", command=articles.yview)
    articles.configure(yscrollcommand=scrollbar.set)

    articles.heading("#0", text="hidden")
    articles.heading("#", text="№")
    articles.heading("Title", text="Заголовок")
    articles.heading("Description", text="Описание")
    articles.heading("Date", text="Дата публикации")

    articles.column("#", anchor=CENTER, width=50, minwidth=50, stretch=False)
    articles.column("Title", anchor=W, width=100, minwidth=150, stretch=True)
    articles.column("Description", anchor=W, width=150, minwidth=100, stretch=True)
    articles.column("Date", anchor=CENTER, width=150, minwidth=100, stretch=True)
    
    # scrollbar.grid(row=0, column=0, sticky="ns", padx=(0,5))
    articles.grid(row=0, column=0, sticky="nsew", padx=(5,0), pady=5)

    info_frame = Frame(frame)
    info_text = Text(info_frame, state='disabled', wrap="word")
    buttons = Frame(info_frame)
    delete = Button(buttons, text="Удалить", fg="red", command=lambda: deleteArticle(str(row_id)))
    update = Button(buttons, text="Редактирвать")

    buttons.pack(side=BOTTOM, fill=X)
    delete.pack(side=RIGHT)
    update.pack(side=RIGHT)

    info_text.pack(fill=BOTH, expand=True)
    info_frame.grid(row=0, column=1, sticky="nsew", padx=(0, 5), pady=5)
    # info_frame.grid(row=0, column=1, sticky="nswe", padx=(0, 5), pady=5)

    def on_select(event):
        selection = articles.selection()
        if selection:
            item_id = selection[0]
            
            global row_id
            row_id = articles.item(item_id)["text"]
            print(row_id)
            res = getArticle(str(row_id))
            if res:
                info_text.config(state='normal')
                info_text.delete("1.0", END)
                article = dedent(f"""
                                Заголовок: {res[5]}
                                Описание: {res[2]}
                                Текст статьи: {res[1]}
                                Дата публикации: {res[3]}
                                """)
                update.config(command=lambda: open_create_frame(res))
                info_text.insert("1.0", article)
                info_text.config(state='disabled') 
                
            
    
    articles.bind("<ButtonRelease-1>", on_select)
    flowRows(articles)

    return frame


def flowRows(table):
    data = getAllArticles()
    table.delete(*table.get_children())
    for index, row in enumerate(data):
        table.insert("", "end", text=str(row[0]), values=(index+1, row[5], row[2], row[3]))
        # table.insert('', 'end', values=row)

def pullArticle(article):
    pass
