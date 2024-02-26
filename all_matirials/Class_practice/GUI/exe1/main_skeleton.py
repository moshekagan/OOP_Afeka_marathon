import csv
import tkinter as tk


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
        return f'{self.__sku}, {self.__name}, {self.__description}, {self.__quantity}, {self.__location}'

    def __repr__(self):
        return self.__str__()

    def get_name(self):
        return self.__name

class App(tk.Tk):
    def __init__(self, products):
        super().__init__()
        self.__products = products
        self.__products_list = None
        self.__title = None

    def show(self):
        self.geometry(f'{APP_WIDTH}x{APP_HEIGHT}')
        self.title('Products')
        self.create_title()
        row = 1
        self.create_list(row)

        self.mainloop()

    def create_title(self):
        self.__title = tk.Label(self, text='My App')
        self.__title.grid()

    def create_list(self, row):
        self.__title = tk.Label(self, text='All Products')
        self.__title.grid(row= row + 1)
        self.__products_list = tk.Listbox(
            self, height=20
        )
        self.__products_list.grid(row=row + 2)
        self.__products_list.bind('<<ListboxSelect>>', lambda event: self.on_select(event))
        i = 0
        for p in self.__products:
            self.__products_list.insert(i, p.get_name())
            i +=1


    def on_select(self, event):
        print(event)

def read_products_csv_file(filename):
    l1 = []
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            l1.append(
                Product(
                    row[0],
                    row[1],
                    row[2],
                    int(row[3]),
                    row[4])
            )

    return l1


def main():
    products = read_products_csv_file('products_list.csv')
    # for p in products:
    #     print(p)
    print(products)
    app = App(products)
    app.show()


if __name__ == '__main__':
    main()
