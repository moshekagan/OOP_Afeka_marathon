# read from file
with open("my_file.txt", "r") as file:
    for line in file:
        print(line.strip())

# write to file
with open("my_file_2.txt", "w") as file:
    file.write("Hello Gal")

# append to file
with open("my_file_3.txt", "a") as file:
    file.write("Hello Yair")

