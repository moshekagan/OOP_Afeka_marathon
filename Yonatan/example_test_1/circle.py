from geometricObject import GeometricObject
import math


class Circle(GeometricObject):
    def __init__(self, radius, color="Black", filled=False):
        if radius < 0:
            raise ValueError(f"Circle.__radius {radius} must be > 0")

        self.__radius = radius
        super().__init__(color, filled)

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        # Option A:
        if radius <= 0:
            return
        else:
            self.__radius = radius

        # Option B:
        # if radius > 0:
        #     self.__radius = radius

    def getArea(self):
        return self.__radius * self.__radius * math.pi
  
    def getDiameter(self):
        return self.__radius * 2
  
    def getPerimeter(self):
        return self.getDiameter() * math.pi

    def writeObject(self, outFile):
        outFile.write(self.__str__())

    def __str__(self):
        return f"Circle: {super().__str__()} radius: {self.__radius} area: {self.getArea()}"

    # def __str__(self):
    #     return "Circle: " + super().__str__() + " radius: " + str(self.__radius) + " area: " + str(self.getArea())
