try:
    num1 = float(input('Enter a number: '))
except ValueError:
    print('Invalid')
    num1 = float(input('Enter a number again: '))

try:
    num2 = float(input('Enter another number: '))
except ValueError:
    print('Invalid')
    num2 = float(input('Enter another number again: '))

try:
    calc_div = num1 / num2
    print(f'{num1} / {num2} = {calc_div}')
except ZeroDivisionError as e:
    print("Can't divide by zero")
