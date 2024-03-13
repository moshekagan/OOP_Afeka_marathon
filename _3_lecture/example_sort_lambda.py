class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

    def __repr__(self):
        return str(self)

persons = [

    Person("David", 32),
    Person("Alice", 25),
    Person("Bob", 20),
    Person("Ali", 31),
    Person("Charlie", 35),
    Person("Benny", 35)
]

persons.sort(key=lambda item: item.age)
print(persons)

persons.sort(key=lambda item: item.name)
print(persons)


def sort_by_age_and_name(item):
    return item.age, item.name


persons.sort(key=sort_by_age_and_name)
print(persons)

# Option B:
persons.sort(key=lambda item: (item.age, item.name))
print(persons)