import random
from tkinter import *

people = [
    "Bruce Wayne",
    "Clark Kent",
    "Peter Parker",
    "Rick Blaine",
    "Willie Wonka",
]
people.sort()

places = [
    "Wayne Enterprises",
    "Daily Planet",
    "Daily Bugle",
    "Rick's American Cafe",
    "Chocolate Factory",
]

window = Tk()
window.wm_attributes("-topmost", 1)

window.title("Workpalce")

Label(window, text="Person").grid(row=0, column=0)
Label(window, text="Workplace").grid(row=0, column=1)

persons_list_var = StringVar()
persons_list_box = Listbox(window,
                           height=len(people),
                           listvariable=persons_list_var,
                           exportselection=False)

persons_list_box.grid(row=1, column=0, padx=10, sticky=N)
persons_list_var.set(tuple(people))

workplace_list_var = StringVar()
workplace_list_box = Listbox(window,
                             height=len(places),
                             listvariable=workplace_list_var,
                             exportselection=False)

workplace_list_box.grid(row=1, column=1, padx=10, sticky=N)
workplace_list_var.set(tuple(sorted(places)))


def handle_determine_match():
    selected_person = persons_list_box.get(persons_list_box.curselection())
    selected_workplace = workplace_list_box.get(workplace_list_box.curselection())
    # TODO - complete it


btn = Button(window, text="Determine if Match is Correct", command=handle_determine_match)
btn.grid(row=2, column=0, columnspan=2, pady=10)

Label(window, text="Answer:").grid(row=3, column=0)
answer = StringVar()

answer_entry = Entry(window, textvariable=answer)
answer_entry.grid(row=3, column=1)

window.mainloop()