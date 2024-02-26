import random
import string


def guess_number():
    i = 0
    numbers = []
    while i < 5:
        num = random.randint(15, 25)
        if num not in numbers:
            numbers.append(num)
            i += 1
    num = int(input(f"Guess a number in the range of 15-25: "))
    if num in numbers:
        print(f'{num} in list {numbers}')
    else:
        print(f'{num} not in list {numbers}')


def q1():
    guess_number()


def generate_random_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def q2():
    length = int(input(f"Enter length of password: "))
    print(f'Your password: {generate_random_password(length)}')


def check_stat(amount):
    counter = 0
    for _ in range(amount):
        num = random.uniform(0, 1)
        if num > 0.5:
            counter += 1
    return counter


def q3():
    amount = 100
    print(f'{((check_stat(amount) / amount) * 100):.2f} % greater than 0.5')


def main():
    # q1()
    # q2()
    q3()


if __name__ == '__main__':
    main()
