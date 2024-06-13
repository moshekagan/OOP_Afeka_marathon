class GeometricObject:
    def __init__(self, name = "un known",
                 shape = "un known",
                 color = "black",
                 filled = False):
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
        return f"GeometricObject: Name:{self.getName()}" \
               f"Shape: {self.getShape()} Color: {self.getColor()}" \
               f"Filled: {self.getFilled()}\n"

# a = GeometricObject("Yoni","Light","Yellow",False)
# print(a)