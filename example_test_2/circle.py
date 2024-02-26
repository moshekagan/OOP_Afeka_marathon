from geometricObject import GeometricObject
import math

class Circle(GeometricObject):
    def __init__(self, radius, color = "Black", filled = False):
        pass # change it

    def getRadius(self):
        return 0 # change it

    def setRadius(self, radius):
        pass # change it

    def getArea(self):
        return self.__radius * self.__radius * math.pi
  
    def getDiameter(self):
        return 0 # change it
  
    def getPerimeter(self):
        return 0 # change it

    def writeObject(self, outFile):
        pass # change it

    def __str__(self):
        return "" # change it