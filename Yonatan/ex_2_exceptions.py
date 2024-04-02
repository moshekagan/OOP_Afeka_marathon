# def my_divide():
#     number = int(input("Enter a number: "))
#     print(3 / number)
#
# try:
#     my_divide()
# except ZeroDivisionError:
#     print("Cannot divide by zero")
#

def foo():
    raise ValueError("This is a ValueError")


try:
    foo()
except ValueError as e:
    print(e)