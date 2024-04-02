from geometricObject import GeometricObject
class RegularPolygon(GeometricObject):
    def __init__(self, side, color, filled):
        pass # change it

    def getSide(self):
        pass # change it

    def __str__(self):
        return super().__str__() + " side: " \
                  + str(self.getSide())

class Square(RegularPolygon):
    def __init__(self, side = 1, color = "red", filled = True):
        pass # change it

    def getArea(self):
        return 0 # change it

    def writeObject(self, outFile):
        outFile.write(self.__str__())

    def __str__(self):
        return "" # change it

class EquilateralTriangle(RegularPolygon):
    def __init__(self, side = 1, color = "blue", filled = False):
        pass # change it

    def getArea(self):
        return 0 # change it

    def writeObject(self, outFile):
        outFile.write(self.__str__())

    def __str__(self):
        return ""# change it

class EquilateralPentagon(RegularPolygon):
    def __init__(self, side=1, color="blue", filled=False):
        pass # change it

    def getArea(self):
        return 0 # change it

    def writeObject(self, outFile):
        outFile.write(self.__str__())

    def __str__(self):
        return "" # change it

