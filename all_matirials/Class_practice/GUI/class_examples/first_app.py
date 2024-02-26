import random
import tkinter as tk


class App:
    def __init__(self):
        self.__entry = None
        self.__btn = None
        self.__title = None
        self.__entry_text = None
        self.__root = tk.Tk()
        self.__root.title('First App')
        self.__root.geometry('800x200')
        self.create_lbl()
        self.create_btn()
        self.create_entry()
        self.__root.mainloop()

    def create_lbl(self):
        self.__title = tk.Label(
            self.__root,
            text='My List',
            font=('David', 26),
            bg='yellow',
            fg='blue',
            anchor='sw',
            width=10,
            height=3

        )
        self.__title.grid()

    def on_click(self):
        colors = ['red', 'orange', 'blue', 'green', 'purple', 'pink']
        color = colors[random.randint(0, len(colors) - 1)]
        self.__btn.config(bg=color)

    def create_btn(self):
        self.__btn = tk.Button(
            self.__root,
            text='Submit',
            font=('David', 26),
            bg='grey',
            fg='green',
            anchor='center',
            width=10,
            command=self.on_click

        )
        self.__btn.grid(column=0, row=1)

    def on_entry_changed(self, *args):
        self.__title.config(text=self.__entry_text.get())

    def create_entry(self):
        self.__entry_text = tk.StringVar()
        self.__entry = tk.Entry(
            self.__root,
            font=('David', 16),
            bg='grey',
            fg='black',
            width=10,
            textvariable=self.__entry_text
        )
        self.__entry_text.trace("w", self.on_entry_changed)
        self.__entry.grid(column=0, row=2)


app = App()
