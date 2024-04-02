class GeometricObject:
    def __init__(self, color="white", filled=True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def getFilled(self):
        return self.__filled

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled

    def __str__(self):
        return "color: " + self.__color + \
            " filled: " + str(self.__filled)



# go = GeometricObject()
# print(go.getColor())
# print(go.getFilled())
#
# print()
#
# go_2 = GeometricObject("blue", False)
# print(go_2.getColor())
# print(go_2.getFilled())
#
# go_2.setColor("red")
# print(go_2.getColor())
#
# go_2.setFilled(True)
# print(go_2.getFilled())
#
# if go_2.isFilled():
#     print("Filled")
# else:
#     print("Not filled")
#
# print(go_2)