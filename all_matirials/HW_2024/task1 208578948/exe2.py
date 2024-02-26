def Task2():
    print("The Capital Test")
    import random
    used_numbers = []
    wrong_answer = []
    wrong_countries = []
    with open("StatesANC.txt", 'r') as file:
        state_info = file.readlines()
        state_info = [line.strip() for line in state_info]

    for i in range(5):
        num = random.randint(0,49)
        while num in used_numbers:
            num = random.randint(0, 49)
        used_numbers.append(num)
        item = state_info[num].split(',')
        capital = input(f"what is the capital of {item[0]}?")
        if capital != item[3]:
            wrong_answer.append(num)
            wrong_countries.append(item)
    print()
    wrong_answers_amount = len(wrong_answer)
    if wrong_answers_amount == 0:
        print("All your answers are correct, Congratulations!")
    else:
        print(f"you had {wrong_answers_amount} mistakes, learn from your mistakes!")
        for country in wrong_countries:
            print(f"the state of {country[0]} is {country[3]}")




if __name__ == '__main__':
    Task2()

