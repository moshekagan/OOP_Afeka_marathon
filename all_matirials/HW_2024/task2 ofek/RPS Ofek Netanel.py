import random
choices = ["rock", "paper", "scissors"]

class Contestant:
    def __init__(self, name):
        self.__name = name
        self.__points = 0

    def get_name(self):
        return self.__name

    def get_points(self):
        return self.__points

    def update_points(self):
        self.__points += 1

    def choose(self):
        pass

    def __str__(self):
        return f"{self.__name}s score: {self.__points}"


class Human(Contestant):
    def choose(self):
        while True:
            try:
                choice = input(f"{self.get_name()}, select: rock, paper or scissors?")
                choice = choice.lower()
                if choice in choices:
                    return choice
                else:
                    raise ValueError("Invalid Choice, Please select one of the suggested options.")
            except ValueError as e:
                print(e)

class Computer(Contestant):
    def choose(self):
        return choices[random.randint(0,2)]

def RPS():
    human_name = input("Insert player name:")
    human = Human(human_name)

    PC_name = input("Insert PC name:")
    PC = Computer(PC_name)

    for i in range (3):
        human_choice = human.choose()
        PC_choice = PC.choose()

        if human_choice != PC_choice:
            if ((human_choice == "rock" and PC_choice == "scissors")
            or (human_choice == "scissors" and PC_choice == "paper")
            or (human_choice == "paper" and PC_choice == "rock")):
                human.update_points()
            else:
                PC.update_points()
        print(f"{human}  {PC}")
    if human.get_points() > PC.get_points():
        print(f"{human_name} Wins!")
    elif human.get_points() < PC.get_points():
        print(f"{PC_name} Wins!")
    else:
        print("Standoff! Its a draw!")



if __name__ == '__main__' :
    RPS()