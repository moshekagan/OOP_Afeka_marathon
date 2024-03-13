from geometricObject import GeometricObject

class Polygon(GeometricObject):
    def __init__(self, name = "un known",
           shape = "un known", numberOfSides = 0,
           color = "black", filled = False):
        pass # change it


    def getNumberOfSides(self):
        return(self.__numberOfSides)

    def writeObject(self, outFile):
        outFile.write(self.__str__())

    def __str__(self):
        return "" # change it
