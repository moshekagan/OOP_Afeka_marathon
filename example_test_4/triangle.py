import math
from polygon import Polygon

class Triangle(Polygon):
    def __init__(self, a = 5, b = 4 , c = 3,
            color = "Black", filled = False,
            name = "no-name"):
        pass  # change it

    def isEquilateral(self):
        pass # change it

    def isIsosceles(self):
        pass # change it

    def isRightAngled(self):
        pass # change it

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
        return "" # change it
