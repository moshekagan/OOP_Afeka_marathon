class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        # return super().__str__()
        return f'name:{self.name}, age: {self.age}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (type(self) == type(other) and
                self.name == other.name and self.age == other.age)


p1 = Person('Yael', 26)
print(p1)
p2 = Person('Bar', 26)
print(p2)
print(p1 == [])
