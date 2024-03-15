from _4_lecture.CE_2.student import LGstudent, PFstudent


def validate_grade(grade, grade_name):
    if grade < 0 or grade > 100:
        raise ValueError(f"Invalid {grade_name} grade, {grade} is not between 0 and 100")

def main():
    lg_students = []
    pf_students = []

    continue_input = "Y"

    while continue_input.upper() == "Y":
        is_ok = True
        try:
            name = input("Enter student name: ")
            midterm = float(input("Enter student midterm grade (0-100): "))
            validate_grade(midterm, "midterm")

            final = float(input("Enter student final grade (0-100): "))
            validate_grade(final, "final")

            student_type = input("Enter student type (LG/PF): ")
            student_type = student_type.upper()

            if student_type != "LG" and student_type != "PF":
                raise NameError(f"Invalid student type, {student_type} is not LG or PF")

            if student_type == "LG":
                student = LGstudent(name, midterm, final)
                lg_students.append(student)
            elif student_type == "PF":
                student = PFstudent(name, midterm, final)
                pf_students.append(student)

        except ValueError as e:
            print(f"Error: {e}")
            is_ok = False
        except NameError as e:
            print(f"Error: {e}")
            is_ok = False

        if is_ok == True:
            continue_input = input("Do you want to enter another student? (Y/N): ")
        else:
            continue_input = "Y"


    lg_students.sort(key=lambda item: (item.getAverage(), item.getName()))
    pf_students.sort(key=lambda item: (item.getAverage(), item.getName()))

    print_students(lg_students, "List of LGStudents:")
    print_students(pf_students, "List of PFStudents:")


def print_students(students, title):
    print(title)
    for student in students:
        print(student)


if __name__ == '__main__':
    main()