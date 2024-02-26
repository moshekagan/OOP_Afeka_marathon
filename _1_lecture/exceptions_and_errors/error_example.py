# ----------------
# Compilation errors:
# ----------------

# if 10 < 100:
# print('10 is less than 100')

# ----------------
# Runtime errors:
# ----------------

# ValueError
num = int("ten")
print(num)

# ZeroDivisionError
num = 10 / 0
print(num)

# IndexError
numbers = [1, 3, 4, 5, 6]
num = numbers[5]
print(num)

# FileNotFoundError
with open("example.txt") as f:
    print(f.read())
