import random


def ex_2():
    lines = read_lines_from_file("StatesANC.txt")
    chosen_lines = random_lines_number_generator()

    wrong_answers = []

    for i in chosen_lines:
        line = lines[i].split(",")
        state = line[0]
        capital = line[2]

        answer = input(f"{i} What is the capital of {state}? ")
        if answer != capital:
            wrong_answers.append(f"{capital} is the capital of {state}")

    print(f"You missed {len(wrong_answers)} questions.")
    for i in wrong_answers:
        print(i)


def random_lines_number_generator():
    random_numbers = []

    for i in range(5):
        is_exist = True
        while is_exist:
            random_number = random.randint(0, 48)

            if not is_number_exist_in_list(random_numbers, random_number):
                random_numbers.append(random_number)
                is_exist = False

    return random_numbers


def is_number_exist_in_list(numbers, number):
    for n in numbers:
        if n == number:
            return True
    return False


def read_lines_from_file(file_name):
    res = []

    try:
        with open(file_name, 'r') as f:
            for line in f:
                res.append(line.strip())
    except FileNotFoundError:
        print(f'File {file_name} not found.')

    return res


if __name__ == '__main__':
    ex_2()
