# Example 3: Sorting a list of Students
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years'

    def __repr__(self):
        return self.__str__()


s1 = Student("John", 30)
s2 = Student("Yossi", 29)
s3 = Student("Avi", 31)

students = [s1, s2, s3]
print("students", students)

sorted_students = sorted(students, key=lambda item: item.age)
print("sorted_students by age", sorted_students)

sorted_students = sorted(students, key=lambda item: item.name)
print("sorted_students by name", sorted_students)

sorted_students = sorted(students, key=lambda item: item.name, reverse=True)
print("sorted_students by name reverse", sorted_students)
