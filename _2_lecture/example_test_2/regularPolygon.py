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
        return super().__str__() + " side: " + str(self.getSide())


class Square(RegularPolygon):
    def __init__(self, side=1, color="red", filled=True):
        super().__init__(side, color, filled)

    def getArea(self):
        return self.getSide() * self.getSide()

    def writeObject(self, outFile):
        outFile.write(self.__str__() + "\n")

    def __str__(self):
        return f"Square: {super().__str__()} area: {self.getArea()}"


class EquilateralTriangle(RegularPolygon):
    def __init__(self, side=1, color="blue", filled=False):
        super().__init__(side, color, filled)

    def getArea(self):
        return self.getSide() * self.getSide() * 0.433

    def writeObject(self, outFile):
        outFile.write(self.__str__() + "\n") # change it

    def __str__(self):
        return f"EquilateralTriangle {super().__str__()} area: {self.getArea()}"


class EquilateralPentagon(RegularPolygon):
    def __init__(self, side=1, color="blue", filled=False):
        super().__init__(side, color, filled)

    def getArea(self):
        return self.getSide() * self.getSide() * 1.72048

    def writeObject(self, outFile):
        outFile.write(self.__str__() + "\n")

    def __str__(self):
        return f"EquilateralPentagon {super().__str__()} area: {self.getArea()}"
