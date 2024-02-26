from geometricObject import GeometricObject

class Rectangle(GeometricObject):
    def __init__(self, width=1, height=1, \
                 color="green", \
                 filled=True):
        pass # change it

    def getWidth(self):
        return 0 # change it

    def setWidth(self, width):
        pass # change it

    def getHeight(self):
        return 0 # change it

    def setHeight(self, height):
        pass # change it

    def getArea(self):
        return self.__width * self.__height

    def getPerimeter(self):
        return 2 * (self.__width + self.__height)
    
    def writeObject(self, outFile):
        pass # change it

    def __str__(self):
        return "" # change it
