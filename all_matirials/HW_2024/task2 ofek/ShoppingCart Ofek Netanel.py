import random

class ShoppingCart:
    def __init__(self, customer):
        self.__customer = customer
        self.__items = []
        self.__address = None
        self.__tot = 0

    def add_item(self, item):
        self.__items.append(item)
        self.__tot += item[1] * item[2]

    def delete_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
            self.__tot -= item[1] * item[2]
        else:
            print(f"Delete Error: Item {item} is not in cart")

    def print_cart(self):
        print(self)

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address

    def __str__(self):
        cart_str = f"Shipping: {self.__address}\n"
        cart_str += "Cart:\n"
        for item in self.__items:
            cart_str += f"item name:  {item[0]} quantity: {item[1]} unit price: {item[2]} item ID: {item[3]}\n"
        cart_str += f"total payment: {self.__tot}"
        return cart_str

def demo():
    """Demonstrate use of class"""
    r = ShoppingCart('Rich')
    r.add_item(('aa', 3, 23, 123))
    r.add_item(('bb', 2, 13, 246))
    r.add_item(('cc', 2, 13, 246))
    r.delete_item(('cc', 1, 1, 1))
    r.delete_item(('cc', 2, 13, 246))
    r.set_address('123 Main, Somewhere, AZ')
    print("from print_cart:")
    r.print_cart()
    print("from __str__(self)")
    print(r)

demo()