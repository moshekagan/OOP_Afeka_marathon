try:
    num1 = float(input('Enter a number: '))
    num2 = float(input('Enter a number: '))

    calc_div = num1 / num2
    print(f'{num1} / {num2} = {calc_div}')
except ValueError:
    print('Invalid input')
except ZeroDivisionError as e:
    print("Can't divide by zero")
except Exception as e:
    print(f"An error occurred: {e}")
