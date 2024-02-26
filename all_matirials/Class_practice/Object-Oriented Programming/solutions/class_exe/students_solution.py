import random


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = []

    def __str__(self):
        student = f'{self.name}, {self.age}'
        for course in self.courses:
            student += f'\n{course}'
        return student

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)


def main():
    student_list = [
        ['yotam', 25],
        ['yael', 27],
        ['moshe', 22],
        ['ron', 29],
        ['mor', 24],
    ]
    students = []
    print('student list')
    for student in student_list:
        students.append(Student(student[0], student[1]))
    for s in students:
        print(s)
    courses = ['python', 'java', 'math']
    for s in students:
        s.add_course(courses[random.randint(0, len(courses) - 1)])
        s.add_course(courses[random.randint(0, len(courses) - 1)])

    print('\nstudent list')
    for s in students:
        print(f'{s}\n')

    sorted_students = sorted(students, key=lambda s1: s1.age)
    print('\nsorted student list')
    for s in sorted_students:
        print(f'{s}\n')


if __name__ == '__main__':
    main()
