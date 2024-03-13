from tkinter import *
from tkinter import font
import sys


class Oscars:
    def __init__(self):
        try:
            self.__window = Tk()
            self.__window.wm_attributes("-topmost", 1)
            self.__myfont = font.Font(family='Helvetica', size=14, slant="italic")
            self.__window.title("Academy Award Winners")

            Label(self.__window,
                  text="GENRES",
                  font=self.__myfont).grid(row=0, column=0)
            Label(self.__window,
                  text="FILMS",
                  font=self.__myfont).grid(row=0, column=1)

            self.__L = []  # all movies genres

            for line in open("Oscars.txt", 'r'):
                l = line.split(',')[1].rstrip()   # l is the genre of the movie
                if l not in self.__L:
                    self.__L.append(l)

            self.__L.sort()  # sort the list of genres

            self.__conOFlstGenres = StringVar()
            self.__lstGenres = Listbox(self.__window,
                                       width=9,
                                       height=len(self.__L),
                                       font=self.__myfont,
                                       listvariable=self.__conOFlstGenres)

            self.__lstGenres.grid(row=1, column=0, padx=10, sticky=N)
            self.__conOFlstGenres.set(tuple(self.__L))

            self.__lstGenres.bind("<<ListboxSelect>>", self.films)

            self.__yscroll = Scrollbar(self.__window, orient=VERTICAL)
            self.__yscroll.grid(row=1, column=2, sticky=NS)

            self.__conOFlstFilms = StringVar()
            self.__lstFilms = Listbox(self.__window,
                                      width=50,
                                      height=len(self.__L),
                                      font=self.__myfont,
                                      listvariable=self.__conOFlstFilms,
                                      yscrollcommand=self.__yscroll.set)
            self.__lstFilms.grid(row=1, column=1, sticky=NSEW)

            self.__yscroll["command"] = self.__lstFilms.yview

            self.__window.mainloop()
        except KeyboardInterrupt:
            return
        except TclError:
            return

    def films(self, e):
        try:
            selected_gener_list = self.__lstGenres.curselection()
            selected_gener_index = selected_gener_list[0]
            selected_gener = self.__L[selected_gener_index]

            movies = []

            for line in open("Oscars.txt", 'r'):
                split_line = line.split(',')    # split_line[0] is the movie name, split_line[1] is the genre split_line[2] is the year
                name = split_line[0].rstrip()
                genre = split_line[1].rstrip()
                year = split_line[2].rstrip()

                if genre == selected_gener:
                    movies.append(f"{name.capitalize()} ({year})")

            movies.sort()

            header = [
                f"List of {len(movies)} {selected_gener} films in oscars file:",
                "\n"
            ]

            movies = header + movies

            # Option B
            # movies.insert(0, f"List of {len(movies)} {selected_gener} films in oscars file:")
            # movies.insert(1, "\n")

            self.__conOFlstFilms.set(tuple(movies))
        except IndexError:
            return
        except TclError:
            return

Oscars()
