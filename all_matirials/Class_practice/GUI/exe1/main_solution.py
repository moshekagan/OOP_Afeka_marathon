import csv
import tkinter as tk
from tkinter import W, END

APP_WIDTH = 600
APP_HEIGHT = 600


class Product:
    def __init__(self, sku, name, description, quantity, location):
        self.__sku = sku
        self.__name = name
        self.__description = description
        self.__quantity = quantity
        self.__location = location

    def __str__(self):
        return f'{self.__sku},{self.__name},{self.__description},{self.__quantity},{self.__location}'

    def get_name(self):
        return self.__name

    def get_quantity(self):
        return self.__quantity


class App(tk.Tk):
    def __init__(self, products):
        super().__init__()
        self.__products = sorted(products, key=lambda p:p.get_quantity())
        self.__products_list = None
        self.__scrollbar = None
        self.__selected_product = None
        self.__product_detail = None

    def show(self):
        self.title('Products')
        self.geometry(f'{APP_WIDTH}x{APP_HEIGHT}')
        current_row = 0
        self.create_title(current_row)
        current_row += 1
        self.create_products_list(current_row)
        current_row += 2
        self.create_product_detail(current_row)

        self.mainloop()

    def create_title(self, current_row):
        lbl = tk.Label(self, text='My App', font=('Ariel bold', 30), width=20, fg='blue', )
        lbl.grid(row=current_row, column=0, padx=10, pady=10)

    def create_products_list(self, current_row):
        products_lbl = tk.Label(self, text='All Products', fg='blue', font=('Ariel', 12), width=20)
        products_lbl.grid(row=current_row, column=0)
        self.__products_list = tk.Listbox(self, height=10)
        self.__products_list.grid(sticky="nsew", row=current_row + 1, column=0)
        self.__products_list.bind('<<ListboxSelect>>', lambda event: self.on_select_product(event))
        self.__products_list.focus()
        self.__products_list.selection_set(0)
        for p in self.__products:
            self.__products_list.insert(END, p.get_name())
        # Create a Scrollbar
        self.__scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.__products_list.yview)
        self.__scrollbar.grid(row=current_row + 1, column=1, sticky="ns")
        # Link the Scrollbar to the Listbox
        self.__products_list.config(yscrollcommand=self.__scrollbar.set)

    def on_select_product(self, event):
        widget = event.widget
        selection = widget.curselection()
        if selection:
            product = widget.get(selection[0])
            for p in self.__products:
                if p.get_name() == product:
                    self.__selected_product = p
                    self.__product_detail.configure(text=p)
                    print(self.__selected_product)
        else:
            self.__selected_product = None

    def create_product_detail(self, current_row):
        self.__product_detail = tk.Label(self, text=self.__selected_product, font=('Ariel bold', 12),
                                         fg='blue', height=5, wraplength=400)
        self.__product_detail.grid(row=current_row, column=0, padx=10, pady=10)


def read_products_csv_file(filename):
    l1 = []
    with open(filename) as csv_file:
        read = csv.reader(csv_file)
        next(read)
        for row in read:
            sku = row[0]
            name = row[1]
            description = row[2]
            quantity = int(row[3])
            location = row[4]
            l1.append(Product(sku, name, description, quantity, location))
    return l1


def main():
    products = read_products_csv_file('products_list.csv')
    app = App(products)
    app.show()


if __name__ == '__main__':
    main()
