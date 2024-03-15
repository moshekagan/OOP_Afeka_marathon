import random


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = random.randint(0, 1000)

    def __str__(self):
        return f"name: {self.name}, age: {self.age}, id: {self.id}"

p1 = Person("John", 36)
p2 = Person("Alice", 25)

print(p1)
print(p2)



def foo(a, b, d, c):
    print(a, b, d, c)


foo(1, 2, 3, 4)
foo(a=1, b=2, d=3, c=4)