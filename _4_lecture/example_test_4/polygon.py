from geometricObject import GeometricObject


class Polygon(GeometricObject):
    def __init__(self,
                 name="un known",
                 shape="un known",
                 numberOfSides=0,
                 color="black",
                 filled=False):
        if numberOfSides <= 2:
            raise ValueError(f"name: {name}, shape: {shape}, numberOfSides = {numberOfSides} must be > 2")

        self.__numberOfSides = numberOfSides
        super().__init__(name, shape, color, filled)

    def getNumberOfSides(self):
        return (self.__numberOfSides)

    def writeObject(self, outFile):
        outFile.write(self.__str__())

    def __str__(self):
        return f"{super().__str__()}, numberOfSides: {self.getNumberOfSides()}"
