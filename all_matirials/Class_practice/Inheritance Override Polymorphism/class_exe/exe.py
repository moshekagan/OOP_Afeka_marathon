class Employee:
    id = 0

    def __init__(self, firstname, lastname, salary):
        Employee.id += 1
        self.id = Employee.id
        self.__firstname = firstname
        self.lastname = lastname
        self.email = f'{firstname}.{lastname}@email.com'
        self.salary = salary

    def __str__(self):
        return (f'{self.__class__.__name__}:{self.id}, {self.__firstname}, {self.lastname},'
                f' {self.email}, {self.salary}')

    def apply_raise(self):
        self.salary *= 1.04


class Developer(Employee):
    def __init__(self, firstname, lastname, salary, prog_langs=None):
        super().__init__(firstname, lastname, salary)
        if prog_langs is None:
            prog_langs = []
        self.prog_langs = prog_langs

    # def __str__(self):
    #     return f'{super().__str__()}, {self.prog_langs}'


def main():
    p1 = Employee('Yael', 'Zur', 18500)
    print(p1)
    p2 = Employee('Avi', 'Barak', 15500)
    print(p2)
    d1 = Developer('Yosi', 'Shalom', 28500, ['java', 'Python'])
    print(d1)
    d2 = Developer('Mor', 'Kor', 15500, )
    print(d2)


main()
