class GeometricObject:
    def __init__(self,
                 name="un known",
                 shape="un known",
                 color="black",
                 filled=False):
        self.__name = name
        self.__shape = shape
        self.__color = color
        self.__filled = filled

    def getName(self):
        return self.__name

    def getShape(self):
        return self.__shape

    def getColor(self):
        return self.__color

    def getFilled(self):
        return self.__filled

    def isFilled(self):
        return self.__filled

    def writeObject(self, outFile):
        outFile.write(self.__str__())

    def __str__(self):
        return (f"name: {self.__name} "
                f"shape: {self.__shape} "
                f"\t\t color: {self.__color}, filled: {self.__filled}")

