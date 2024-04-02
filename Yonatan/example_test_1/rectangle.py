from geometricObject import GeometricObject

class Rectangle(GeometricObject):
    def __init__(self, width=1, height=1, color="green", filled=True):
        if width < 0:
            raise ValueError(f"Rectangle.__width {width} must be > 0")
        if height < 0:
            raise ValueError(f"Rectangle.__height {height} must be > 0")

        super().__init__(color, filled)
        self.__width = width
        self.__height = height

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        if width > 0:
            self.__width = width

    def getHeight(self):
        return self.__height

    def setHeight(self, height):
        if height > 0:
            self.__height = height

    def getArea(self):
        return self.__width * self.__height

    def getPerimeter(self):
        return 2 * (self.__width + self.__height)
    
    def writeObject(self, outFile):
        outFile.write(self.__str__())

    def __str__(self):
        return f"Rectangle: {super().__str__()} width: {self.getWidth()} height: {self.getHeight()} area: {self.getArea()}"


# r = Rectangle(1, 3)
# print(r)
# r.setWidth(10)
# print(r)
#