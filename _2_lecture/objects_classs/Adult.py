class Adult:
    MIN_AGE = 21

    def __init__(self, name, age):
        self.__name = name
        if age > Adult.MIN_AGE:
            self.__age = age
        else:
            raise ValueError
        self.__graduated = False
        self.__grads = []
        self.partner = None

    def set_partner(self, partner):
        self.partner = partner

    def add_grade(self, grade):
        self.__grads.append(grade)

    def set_graduated(self):
        self.__graduated = True

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def __str__(self):
        return f'Name: {self.__name}, Age: {self.__age}, Graduated: {self.__graduated}'

    def __repr__(self):
        return self.__str__()

print(Adult.MIN_AGE)

a = Adult('John', 25)
b = Adult('Smith', 22)

a.set_partner(b)
b.set_partner(a)

a.set_partner(None)
b.set_partner(None)