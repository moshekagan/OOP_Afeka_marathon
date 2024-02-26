try:
    num1 = int(input('Enter numbers: '))
    num2 = int(input('Enter numbers: '))
    print(num1 / num2)
except ValueError as e:
    print(f'exception {e} {2 + 4}')
except ZeroDivisionError as e:
    print('ZeroDivisionError', e)
except Exception as e:
    print('Exception', e)
else:
    print('No errors')
finally:
    print('finally...')
print('rest code....')