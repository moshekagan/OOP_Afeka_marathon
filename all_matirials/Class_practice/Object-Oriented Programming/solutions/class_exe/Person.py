class Person:
    def __new__(cls, *args, **kwargs):
        print('creating new Person instance')
        return super().__new__(cls)

    def __init__(self, name, age):
        print('initializing Person instance')
        self.name = name
        self.age = age

    def __str__(self):
        print('__str__')
        return f'{self.name}, {self.age}'

    def __repr__(self):
        print('__repr__')
        return f'in __repr__ function : {self.name}, {self.age}'

    def __eq__(self, other):
        return isinstance(other, Person) and self.age == other.age

    def __hash__(self):
        return hash(self.age)
