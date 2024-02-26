from tkinter import *
from tkinter import font
import sys

class Oscars:
    def __init__(self):
      try:
        self.__window = Tk()
        self.__window.wm_attributes("-topmost", 1)
        self.__myfont = font.Font(
            family='Helvetica', size=14, slant="italic")
        self.__window.title("Academy Award Winners")
        Label(self.__window, text="GENRES",
           font = self.__myfont).grid(
              row=0, column=0)
        Label(self.__window, text="FILMS",
            font = self.__myfont).grid(row=0, column=1)
        self.__L = []
        for line in open("Oscars.txt", 'r'):
          l = line.split(',')[1].rstrip()
          if l not in self.__L:
              self.__L.append(l)
        self.__L.sort()
        self.__conOFlstGenres = StringVar()
        self.__lstGenres = \
            Listbox(self.__window, width=9, \
               height=len(self.__L), font = self.__myfont,
               listvariable=self.__conOFlstGenres)
        self.__lstGenres.grid(row=1,
                column=0, padx=10, sticky=N)
        self.__conOFlstGenres.set(tuple(self.__L))

        # change it

        self.__yscroll = Scrollbar(self.__window,
                orient=VERTICAL)
        self.__yscroll.grid(row=1, column=2,
                            sticky=NS)
        self.__conOFlstFilms = StringVar()
        self.__lstFilms = Listbox(
               self.__window, width=50,
               height=len(self.__L), font = self.__myfont,
               listvariable=self.__conOFlstFilms,
               yscrollcommand=self.__yscroll.set)
        self.__lstFilms.grid(
            row=1, column=1, sticky=NSEW)

        # change it

        self.__window.mainloop()
      except  KeyboardInterrupt:
          return

    def films(self, e):

          pass # change it

Oscars()
