from geometricObject import GeometricObject

class Polygon(GeometricObject):
    def __init__(self, name = "un known",
           shape = "un known", numberOfSides = 0,
           color = "black", filled = False):

        if numberOfSides <= 2:
            raise ValueError(f"Polygon: name: {name}"
                             f"shape: {shape},"
                             f"numoberfsides: {numberOfSides} must be > 2")

        super().__init__(name, shape, filled, color)
        self.__numberOfSides = numberOfSides


    def getNumberOfSides(self):
        return(self.__numberOfSides)

    def writeObject(self, outFile):
        outFile.write(self.__str__())

    def __str__(self):
        return f"GeometricObject: {super().__str__()}" \
               f"numberOfSides: {self.getNumberOfSides()}\n"

