class Employee:
    ID = 0
    RAISE_AMT = 1.04

    def __init__(self, firstname, lastname, salary):
        Employee.ID += 1
        self.id = Employee.ID
        self.firstname = firstname
        self.lastname = lastname
        self.email = firstname + '.' + lastname + '@email.com'
        self.salary = salary

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return isinstance(other, Employee) and self.id == other.id

    def apply_raise(self):
        self.salary = int(self.salary * self.RAISE_AMT)


class Developer(Employee):
    RAISE_AMT = 1.10

    def __init__(self, firstname, lastname, salary, prog_langs=[]):
        super().__init__(firstname, lastname, salary)
        self.prog_langs = prog_langs

    def __str__(self):
        return f"{super().__str__()} is a developer"


class Manager(Employee):
    RAISE_AMT = 1.15

    def __init__(self, first_name, lastname, salary, employees=None):
        super().__init__(first_name, lastname, salary)
        if employees is None:
            employees = []
        self.employees = employees

    def __str__(self):
        return f"{super().__str__()} is a manager"

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for employee in self.employees:
            print('\t', employee)

    def print_employees_salary(self):
        for emp in self.employees:
            print('\t', emp, emp.salary)

    def apply_all_raise(self):
        for emp in self.employees:
            emp.apply_raise()



def main():
    employees_details = [
        ['', 'Mor', 'Avner', 10000],
        ['developer', 'Moshe', 'Cohen', 20000, ['java', 'python', 'c++']],
        ['developer', 'Kobi', 'Shalom', 22000, ['java', 'nodeJs']],
        ['', 'Tom', 'Keren', 12000],
        ['developer', 'Liat', 'Barak', 30000, ['java', 'python', 'javascript', 'dart']]
    ]
    employees = []
    for item in employees_details:
        if item[0] == 'developer':
            employees.append(Developer(item[1], item[2], item[3], item[4]))
        else:
            employees.append(Employee(item[1], item[2], item[3]))

    manager = Manager('Galit', 'Mor', 35000, employees)
    print(manager)
    manager.print_employees_salary()
    manager.apply_all_raise()
    print('After apply salary')
    manager.print_employees_salary()
    manager.add_employee(Developer('Yael', 'Marom', 20000, ['java', 'angular']))
    print('After adding new employee')
    manager.print_employees_salary()


if __name__ == '__main__':
    main()
