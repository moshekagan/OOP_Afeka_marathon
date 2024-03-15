import math
from polygon import Polygon


class Triangle(Polygon):
    def __init__(self, a=5, b=4, c=3,
                 color="Black", filled=False, name="no-name"):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError(f"all sides must be > 0, a: {a}, b: {b}, c: {c}")

        l = [a, b, c]
        l.sort()

        self.__side1 = l[0]
        self.__side2 = l[1]
        self.__side3 = l[2]

        if self.__side1 + self.__side2 <= self.__side3:
            raise ValueError(f"name: {name} shape: triangle, "
                             f"side1: {self.__side1}, side2: {self.__side2}, side3: {self.__side3} side_1 + side_2 must be > side_3")

        super().__init__(name=name,
                         shape="Triangle",
                         numberOfSides=3,
                         color=color,
                         filled=filled)

    def isEquilateral(self):
        pass  # change it

    def isIsosceles(self):
        pass  # change it

    def isRightAngled(self):
        pass  # change it

    def getSide1(self):
        return self.__side1

    def getSide2(self):
        return self.__side2

    def getSide3(self):
        return self.__side3

    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        area = math.sqrt(
            s * (s - self.__side1) * \
            (s - self.__side2) * (s - self.__side3))
        return area

    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def writeObject(self, outFile):
        outFile.write(self.__str__())

    def __str__(self):
        return ""  # change it
