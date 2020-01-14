from tkinter import *


class WordMetadata:
    def __init__(self, word, sent_num, sent_pos):
        self.word = word
        self.sent_num = sent_num
        self.sent_pos = sent_pos


class WordReaderGui(Tk):

    def __init__(self):
        super().__init__()
        super().title("Welcome to LikeGeeks app")
        super().geometry('650x800')
        # lbl = Label(window, text="Hello")
        #
        # lbl.grid(column=0, row=0)
        # btn = Button(window, text="Click Me")
        #
        # btn.grid(column=1, row=0)


    # def clicked():
    #     lbl.configure(text="Button was clicked !!")
    #
    # btn = Button(window, text="Click Me", command=clicked)
    #
    # btn.grid(column=1, row=0)
    # btn = Button(window, text="Click Me", command=clicked)
    #
    # btn.grid(column=1, row=0)
    # window.mainloop()
    # btn = Button(window, text="Click Me", command=clicked)
    #
    # btn.grid(column=1, row=0)
    pass
