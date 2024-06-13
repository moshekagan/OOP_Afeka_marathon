import math
from polygon import Polygon

class Triangle(Polygon):
    def __init__(self, a = 5, b = 4 , c = 3,
            color = "Black", filled = False,
            name = "no-name"):

        super().__init__(name, color, filled)
        self.__side1 = a
        self.__side2 = b
        self.__side3 = c

        if a + b < c or a + c < b or b + c < a:
            raise ValueError(f"name:{name},color:{color}"
                             f"filled{filled}, side1 + side2 must be > side3")


    def isEquilateral(self):
        if self.__side1 == self.__side2 == self.__side3:
            return True
        else:
            return False

    def isIsosceles(self):
        if self.__side1 == self.__side2 or self.__side2 == self.__side3\
                or self.__side2 == self.__side3:
            return True
        else:
            return False

    def isRightAngled(self):
        if self.__side1 + self.__side2 == self.__side3:
            return True
        else:
            return False

    def getSide1(self):
        return self.__side1

    def getSide2(self):
        return self.__side2

    def getSide3(self):
        return self.__side3

    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        area = math.sqrt(
            s * (s-self.__side1) * \
              (s-self.__side2) * (s-self.__side3))
        return area
  
    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3
  
    def writeObject(self, outFile):
        outFile.write(self.__str__())

    def __str__(self):
        return f"triangle: {super().__str__()}" \
               f"side1: {self.getSide1()}" \
               f"side2: {self.getSide2()}" \
               f"side3: {self.getSide3()}" \
               f"perimeter: {self.getPerimeter()}" \
               f"area: {self.getArea()}" \
               f"equilateral triangle: {self.isEquilateral()}" \
               f"isosceles triangle: {self.isIsosceles()}" \
               f"rightAngles triangle: {self.isRightAngled()}\n"
