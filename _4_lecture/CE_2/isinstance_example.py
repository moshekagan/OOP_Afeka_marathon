from _4_lecture.CE_2.student import Student, LGstudent, PFstudent

s = Student("John", 90, 80)
lg_s = LGstudent("John", 90, 80)
pf_s = PFstudent("John", 90, 80)


if isinstance(s, Student) == True:
    print("s is a Student")
else:
    print("s is not a Student")

if isinstance(lg_s, Student) == True:
    print("lg_s is a Student")
else:
    print("lg_s is not a Student")

if isinstance(lg_s, LGstudent) == True:
    print("lg_s is a LGstudent")
else:
    print("lg_s is not a LGstudent")

if isinstance(s, LGstudent) == True:
    print("s is a LGstudent")
else:
    print("s is not a LGstudent")

if isinstance(pf_s, int) == True:
    print("pf_s is an int")
else:
    print("pf_s is not an int")