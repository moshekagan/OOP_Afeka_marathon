try:
    with open("Agegs_1.txt", "r") as file:
        for line in file:
            print(line)
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")

try:
    with open('Ages.txt', 'r') as file:
        for l in file:
            line = l.strip()
            print(line)

            try:
                num = int(line)
            except ValueError as e:
                print(f"'{line}' is not an integer")

            if line == "":
                raise EOFError

        raise EOFError
except EOFError as e:
    print(f"EOFError: End of File")

print("By")
