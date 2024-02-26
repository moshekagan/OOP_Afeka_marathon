try:
    with open('Ages.txt', 'r') as file:
        for l in file:
            line = l.strip()
            print(line)

            try:
                num = int(line)
            except ValueError as e:
                print(f"'{line}' is not an integer")

        raise EOFError
except EOFError as e:
    print(f"EOFError: End of File")

print("By")
