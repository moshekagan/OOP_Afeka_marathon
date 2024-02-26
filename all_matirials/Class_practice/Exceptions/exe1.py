def q1():
    try:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        result = num1 / num2
        print(f'Result: {result}')
    except ZeroDivisionError as e:
        print(f'Error: {e}')


def q2():
    try:
        num = int(input("Enter number: "))
        print(f'Entered number: {num}')
    except ValueError as e:
        print(f'Error: {e}')


def q3():
    try:
        in_file = open('data1.txt')
        print(in_file.read())
        in_file.close()
    except FileNotFoundError as e:
        print(f'Error: {e}')


def main():
    # q1()
    # q2()
    q3()


if __name__ == '__main__':
    main()