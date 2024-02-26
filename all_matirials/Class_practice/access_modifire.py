class MyClass:
    class_attribute = "I am a class-level attribute"

    def __init__(self):
        # Public attribute
        self.public_attribute = "I am public!"

        # Protected attribute (prefixed with a single underscore)
        self._protected_attribute = "I am protected!"

        # Private attribute (prefixed with double underscores)
        self.__private_attribute = "I am private!"

    @property
    def protected_attribute(self):
        return self._protected_attribute

    def get_private_attribute(self):
        return self.__private_attribute

    def set_private_attribute(self, value):
        self.__private_attribute = value


# Creating an instance of MyClass
c1 = MyClass()

# Accessing public attribute
print("Public attribute:", c1.public_attribute)

# Accessing protected attribute
print("Protected attribute:", c1.protected_attribute)

# Accessing private attribute using getter method
print("Private attribute:", c1.get_private_attribute())

# Modifying private attribute using setter method
c1.set_private_attribute("I am a modified private attribute")
print("Modified private attribute:", c1.get_private_attribute())

# Accessing class-level attribute
print("Class-level attribute:", MyClass.class_attribute)
