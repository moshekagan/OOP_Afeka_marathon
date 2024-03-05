# Option 1:
# ----------------
is_valid_integer = False

while not is_valid_integer:
    try:
        num = int(input('Enter a nonzero integer: '))
        calc = 1 / num
        print("The result is: ", calc)

        is_valid_integer = True
    except ValueError:
        print("You didn't enter an integer, try again")
        is_valid_integer = False
    except ZeroDivisionError:
        print("You entered zero, try again")
        is_valid_integer = False


# Option 2:
# ----------------
def get_nonzero_integer_from_user():
    is_valid_integer = False
    num = None

    while not is_valid_integer:
        try:
            num = int(input('Enter a nonzero integer: '))
            if num == 0:
                raise ZeroDivisionError

            is_valid_integer = True
        except ValueError:
            print("You didn't enter an integer, try again")
            is_valid_integer = False
        except ZeroDivisionError:
            print("You entered zero, try again")
            is_valid_integer = False

    return num


nonzero = get_nonzero_integer_from_user()
print("the result is: ", 1 / nonzero)
