from _1_lecture.exceptions_and_errors.get_float_number_from_user import get_float_number_from_user

try:
    num1 = get_float_number_from_user()
    num2 = get_float_number_from_user()

    calc_div = num1 / num2
    print(f'{num1} / {num2} = {calc_div}')
except ValueError:
    print('Invalid input')
except ZeroDivisionError as e:
    print("Can't divide by zero")
