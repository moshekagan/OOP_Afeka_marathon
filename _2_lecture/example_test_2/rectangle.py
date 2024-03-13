from geometricObject import GeometricObject


class Rectangle(GeometricObject):
    def __is_validate(self, value, name):
        if value <= 0:
            raise ValueError(f"Rectangle.__{name} [{value}] - must be positive")

    def __init__(self, width=1, height=1, color="green", filled=True):
        self.__is_validate(width, "width")
        self.__is_validate(height, "height")

        # Option B:
        # if width <= 0:
        #     raise ValueError(f"Rectangle.__width [{width}] - must be positive")
        #
        # if height <= 0:
        #     raise ValueError(f"Rectangle.__height [{height}] - must be positive")
        self.__width = width
        self.__height = height

        super().__init__(color, filled)

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
        outFile.write(self.__str__() + "\n")

    def __str__(self):
        return f"Rectangle: {super().__str__()} width: {self.__width}, height: {self.__height}, area: {self.getArea()}"
