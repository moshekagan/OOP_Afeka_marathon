def get_float_number_from_user():
    is_valid = False

    while not is_valid:
        try:
            num = float(input("Enter a number: "))
            is_valid = True
            return num
        except ValueError:
            print("Invalid")


