import csv
import random


def read_employees_csv_file():
    employees = []
    csv_file = open("employees_list.csv")
    read = csv.reader(csv_file)
    for row in read:
        e_id = row[0]
        firstname = row[1]
        lastname = row[2]
        phone = row[3]
        address = row[4]
        gender = row[5]
        employee = Employee(e_id, firstname, lastname, phone, address, gender)
        employees.append(employee)

    return employees


class ManagerEmployeesOverflowError(Exception):
    def __init__(self):
        super().__init__("Error: You have exceeded the maximum amount for employees")


class ManagerEmployeesExistError(Exception):
    def __init__(self):
        super().__init__("Error: Employee already exist")


class Person:
    def __init__(self, e_id, firstname, lastname):
        self.e_id = e_id
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return f'{self.__class__.__name__}: {self.e_id}, {self.firstname}, {self.lastname}'


class Employee(Person):
    def __init__(self, e_id, firstname, lastname, phone_number, address, gender):
        super().__init__(e_id, firstname, lastname)
        self.phone_number = phone_number
        self.address = address
        self.gender = gender

    def __str__(self):
        return f'{super().__str__()},' \
               f'  {self.phone_number}, {self.address},{self.gender} '


class Manager(Employee):
    def __init__(self, e_id, firstname, lastname, address, phone_number, gender, max_employees, employees=None):
        super().__init__(e_id, firstname, lastname, address, phone_number, gender)
        self.max_employees = max_employees
        if employees is None:
            employees = []
        self.employees = employees[:self.max_employees]
        if len(employees) > max_employees:
            raise ManagerEmployeesOverflowError()

    def print_employees(self):
        if self.employees:
            print(f'Employees list of manager: {self.firstname}, {self.lastname}:')
            for employee in self.employees:
                print(employee)
        else:
            print(f'There are no employees yet for manager: {self.firstname}, {self.lastname}:')

    def add_employee(self, employee):
        if len(self.employees) == self.max_employees:
            raise ManagerEmployeesOverflowError()
        if employee in self.employees:
            raise ManagerEmployeesExistError()
        self.employees.append(employee)


def print_employees(employees):
    for e in employees:
        print(e)


def convert_random_employee_to_manager(employees):
    temp = [e for e in employees if not isinstance(e, Manager)]
    index = random.randint(0, len(temp) - 1)
    e = temp[index]
    print(f'convert {e.firstname} {e.lastname} to be manager')
    index = employees.index(e)
    max_employees = random.randint(2, 4)
    employees[index] = Manager(e.e_id, e.firstname, e.lastname, e.phone_number, e.address, e.gender, max_employees)


def add_random_employee_to_random_manager(employees):
    try:
        temp = [e for e in employees if not isinstance(e, Manager)]
        index = random.randint(0, len(temp) - 1)
        e = temp[index]
        temp = [e for e in employees if isinstance(e, Manager)]
        index = random.randint(0, len(temp) - 1)
        m = temp[index]
        print(f'try to add {e.firstname} {e.lastname} to manager'
              f' {m.firstname} {m.lastname} {len(m.employees)}/{m.max_employees}')
        m.add_employee(e)
    except (ManagerEmployeesOverflowError, ManagerEmployeesExistError) as e:
        print(e)


def print_employees_of_managers(employees):
    managers = [e for e in employees if isinstance(e, Manager)]
    for m in managers:
        m.print_employees()


def main():
    employees = read_employees_csv_file()
    convert_random_employee_to_manager(employees)
    convert_random_employee_to_manager(employees)
    print_employees(employees)
    print()
    for _ in range(8):
        add_random_employee_to_random_manager(employees)
    print_employees_of_managers(employees)
    print('\nEmployees sorted by first name')
    print_employees(sorted(employees, key=lambda e: e.firstname))
    print('\nEmployees sorted by length of last name')
    print_employees(sorted(employees, key=lambda e: len(e.lastname)))
    print('\nEmployees sorted by city')
    print_employees(sorted(employees, key=lambda e: e.address.split(',')[1]))


if __name__ == '__main__':
    main()
