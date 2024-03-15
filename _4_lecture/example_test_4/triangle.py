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
                         shape="triangle",
                         numberOfSides=3,
                         color=color,
                         filled=filled)

    def isEquilateral(self):
        if self.__side1 == self.__side2 and self.__side2 == self.__side3 and self.__side1 == self.__side3:
            return True
        else:
            return False

    def isIsosceles(self):
        if self.__side1 == self.__side2 or self.__side2 == self.__side3 or self.__side1 == self.__side3:
            return True
        else:
            return False

    def isRightAngled(self):
        s1_sqaure = self.__side1 * self.__side1
        s2_sqaure = self.__side2 * self.__side2
        s3_sqaure = self.__side3 ** 2  # or self.__side3 * self.__side3

        if s1_sqaure + s2_sqaure == s3_sqaure:
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
            s * (s - self.__side1) * \
            (s - self.__side2) * (s - self.__side3))
        return area

    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def writeObject(self, outFile):
        outFile.write(self.__str__())

    def __str__(self):
        return (f"{super().__str__()}\n side1: {self.__side1}, side2: {self.__side2}, side3: {self.__side3},\n"
                f" area: {self.getArea()}, perimeter: {self.getPerimeter()}\n"
                f" isEquilateral: {self.isEquilateral()}\b isIsosceles: {self.isIsosceles()}\b isRightAngled: {self.isRightAngled()}")
