from geometricObject import GeometricObject
class RegularPolygon(GeometricObject):
    def __init__(self, side, color, filled):
        if side <= 0:
            raise ValueError(f"RegularPolygon.__side [{side}] - must be positive")
        self.__side = side
        super().__init__(color, filled)

    def getSide(self):
        return self.__side

    def __str__(self):
        return super().__str__() + " side: " \
                  + str(self.getSide())

class Square(RegularPolygon):
    def __init__(self, side=1, color="red", filled=True):
        super().__init__(side, color, filled)

    def getArea(self):
        return self.getSide() * self.getSide()

    def writeObject(self, outFile):
        outFile.write(self.__str__())

    def __str__(self):
        return f"Square: {super().__str__()} area: {self.getArea()}"

class EquilateralTriangle(RegularPolygon):
    def __init__(self, side = 1, color = "blue", filled = False):
        pass # change it

    def getArea(self):
        return 0 # change it

    def writeObject(self, outFile):
        pass # change it

    def __str__(self):
        return ""# change it

class EquilateralPentagon(RegularPolygon):
    def __init__(self, side=1, color="blue", filled=False):
        pass # change it

    def getArea(self):
        return 0 # change it

    def writeObject(self, outFile):
        pass # change it

    def __str__(self):
        return "" # change it

