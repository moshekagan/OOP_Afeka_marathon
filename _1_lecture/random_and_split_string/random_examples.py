import random

# Example 1: get random int
start = 1
end = 100
random_integer = random.randint(start, end)
print(random_integer)


# Example 2: get random float
random_float = random.random()
print(random_float)

# if we need float that bigger then 1
print(random_float * 100)

# if I want it to be int
print(int(random_float * 100))


# Example 3: choice from list
names = ['John', 'Smith', 'Avi', "Yossi"]

# option a:
random_index = random.randint(0, len(names) - 1)
random_name = names[random_index]
print(random_name)

# option b:
random_name = random.choice(names)
print(random_name)
