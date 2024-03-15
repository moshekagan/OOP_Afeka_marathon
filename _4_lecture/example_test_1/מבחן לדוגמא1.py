from tkinter import *


class Calculator:
    def __init__(self):
        self.__window = Tk()
        self.__window.wm_attributes("-topmost", 1)
        self.__window.title("Calculate")

        Label(self.__window, text="First \nNumber:").grid(row=0, column=0)
        Label(self.__window, text="Second \nNumber: ").grid(row=0, column=2)

        # entries numbers
        self.__conOFentFirst = StringVar()
        self.__entFirst = Entry(self.__window, width=10, textvariable=self.__conOFentFirst)
        self.__entFirst.grid(row=1, column=0)

        self.__conOFentSecond = StringVar()
        self.__entSecond = Entry(self.__window, width=10, textvariable=self.__conOFentSecond)
        self.__entSecond.grid(row=1, column=2)

        # actions
        self.__btnAdd = Button(self.__window, text='+', width=3, command=self.add)
        self.__btnAdd.grid(row=0, column=1, padx=15)

        self.__btnSubtract = Button(self.__window, text='-', width=3, command=self.subtract)
        self.__btnSubtract.grid(row=1, column=1, padx=15)

        self.__btnMultiply = Button(self.__window, text='x', width=3, command=self.multiply)
        self.__btnMultiply.grid(row=2, column=1, padx=15)

        self.__btnDivide = Button(self.__window, text='/', width=3, command=self.divide)
        self.__btnDivide.grid(row=3, column=1, padx=15)

        # result
        Label(self.__window, text="Result").grid(row=4, column=0, sticky=W)
        self.__conOFentResult = StringVar()
        self.__entResult = Entry(self.__window, state="readonly", width=35, textvariable=self.__conOFentResult)
        self.__entResult.grid(row=4, column=0, columnspan=4, padx=40, pady=5)

        # errors
        self.__msgError1 = StringVar()
        Label(self.__window, textvariable=self.__msgError1).grid(row=5, column=0, columnspan=20, sticky=W)

        self.__msgError2 = StringVar()
        Label(self.__window, textvariable=self.__msgError2).grid(row=6, column=0, columnspan=20, sticky=W)

        # error messages
        self.__errMsg1 = "Wrong First Number, Must Be Float!"
        self.__errMsg2 = "Wrong Second Number, Must Be Float!"
        self.__errMsg3 = "Wrong Denominator(Second Number)! " + " Not Zero!"

        self.__window.mainloop()

    def perform(self, op):
        self.__conOFentResult.set("")
        self.__msgError1.set("")
        self.__msgError2.set("")

        a = None
        b = None

        is_ok = True

        try:
            a = float(self.__entFirst.get())
        except ValueError:
            self.__msgError1.set(self.__errMsg1)
            is_ok = False

        try:
            b = float(self.__entSecond.get())
        except ValueError:
            self.__msgError2.set(self.__errMsg2)
            is_ok = False

        if op == "/" and b == 0:
            self.__msgError2.set(self.__errMsg3)
            is_ok = False

        if is_ok == True:
            if op == "+":
                result = a + b
                result = round(result, 2)
                self.__conOFentResult.set(f"{a} + {b} = {result}")
            elif op == "-":
                result = a - b
                result = round(result, 2)
                self.__conOFentResult.set(f"{a} - {b} = {result}")
            elif op == "*":
                result = a * b
                result = round(result, 2)
                self.__conOFentResult.set(f"{a} * {b} = {result}")
            elif op == "/":
                result = a / b
                result = round(result, 2)
                self.__conOFentResult.set(f"{a} / {b} = {result}")

    def add(self):
        self.perform("+")

    def subtract(self):
        self.perform("-")

    def multiply(self):
        self.perform("*")

    def divide(self):
        self.perform("/")


def main():
    Calculator()


main()
