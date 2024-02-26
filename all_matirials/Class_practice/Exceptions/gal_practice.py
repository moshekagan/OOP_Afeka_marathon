try:
    num = int(input('Enter number: '))
    print(num)
    if num < 0:
        raise ValueError('PINI in lesson')
except ValueError as error_pini:
    print(error_pini)
    print('custom raise')
except (NameError, NotImplemented, SyntaxError) as error_pini:
    print(error_pini)
except Exception as error_pini:
    print(error_pini)
else:
    print('no errors')
finally:
    print('always printing')
