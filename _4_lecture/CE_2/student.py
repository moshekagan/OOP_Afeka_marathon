class Student:
    def __init__(self, name="", midterm=0, final=0):
        self._name = name
        self._midterm = midterm
        self._final = final
        self._average = round((self._midterm + self._final) / 2)
      
    def setName(self, name):
        self._name = name

    def setMidterm(self, midterm):
        self._midterm = midterm

    def setFinal(self, final):
        self._final = final

    def getName(self):
        return self._name

    def getMidterm(self):
        return self._midterm

    def getFinal(self):
        return self._final

    def getAverage(self):
        return self._average
        
    def __str__(self):
        return "student name: " + self._name \
               + "    average: " + str(self._average) \
               + "    grade: "  + self.calcSemGrade()


class LGstudent(Student):
    def calcSemGrade(self):
        average = round((self._midterm + self._final) / 2)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def __str__(self):
        return f"LGstudent object: {super().__str__()}"

class PFstudent(Student):

    def calcSemGrade(self):
        average = round((self._midterm + self._final) / 2)
        if average >= 60:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return f"PFstudent object: {super().__str__()}"

