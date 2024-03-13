from geometricObject import GeometricObject
import math

class Circle(GeometricObject):
    def __init__(self, radius, color="Black", filled=False):
        if radius <= 0:
            raise ValueError(f"Circle.__radius [{radius}] - must be positive")

        self.__radius = radius
        super().__init__(color, filled)

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        if radius > 0:
            self.__radius = radius

    def getArea(self):
        return self.__radius * self.__radius * math.pi
  
    def getDiameter(self):
        return self.__radius * 2
  
    def getPerimeter(self):
        return self.getDiameter() * math.pi

    def writeObject(self, outFile):
        outFile.write(self.__str__() + "\n")

    def my_str(self, another_circle):
        return f"My color is: {self.getColor()} and the other color is: {another_circle.getColor()}"

    def __str__(self):
        return f"Circle: {super().__str__()} radius: {self.getRadius()}, area: {self.getArea()}"


# g1 = GeometricObject("Red", True)
# g2 = GeometricObject("Green", False)
#
# g1.getColor()
# g2.getColor()
#
# c1 = Circle(5, "Blue", True)
# c1.getColor()
#
# c2 = Circle(10, "Yellow", False)
#
# print(c1.my_str(c2))
# print(c2.my_str(Circle))
