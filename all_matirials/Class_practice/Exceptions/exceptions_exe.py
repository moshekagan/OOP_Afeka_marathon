def divide_numbers():
    try:
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
        result = num1 / num2
        print('Result:', result)
    except ZeroDivisionError:
        print('Error: Cannot divide by zero')


def q1():
    divide_numbers()


def get_integer():
    try:
        num = int(input('Enter an integer: '))
        print('Entered number:', num)
    except ValueError:
        print('Error: Please enter a valid integer')


def q2():
    get_integer()


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print('File content:', content)
    except FileNotFoundError:
        print(f'Error: File {filename} not found')


def q3():
    read_file('data1.txt')


def perform_operation():
    try:
        num1 = float(input('Enter a number: '))
        num2 = float(input('Enter another number: '))
        result = num1 / num2
        print('Result:', result)
    except ZeroDivisionError:
        print('Error: Cannot divide by zero')
    except ValueError:
        print('Error: Invalid input. Please enter a number')


def q4():
    perform_operation()


def divide_numbers2():
    try:
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
        result = num1 / num2
        print('Result:', result)
    except (ZeroDivisionError, ValueError) as e:
        print(f'Error: {e}')
    else:
        print('No errors...')
    finally:
        print('Division operation completed')


def q5():
    divide_numbers2()


def sum_and_average():
    sum_numbers, counter = 0, 0
    while True:
        try:
            num = float(input('Enter the number: '))
            if num == -1:
                break
            if num < 0:
                raise ValueError('please enter only positive numbers')
            sum_numbers += num
            counter += 1
        except ValueError as e:
            print(f'Error: {e}')
    if counter > 0:
        print(f'sum numbers = {sum_numbers} of {counter} numbers'
              f', average = {(sum_numbers / counter):.2f}')
    else:
        print('No data to implement..')


def q6():
    sum_and_average()


def main():
    # q1()
    # q2()
    # q3()
    # q4()
    # q5()
    q6()


if __name__ == '__main__':
    main()
