import random

class Player:

    def __init__(self, name = 'player', level = 0, character = 'Default'):
        self.__name = name
        self.__level = level
        self.__character = character

    def __str__(self):
        return f'player name:{self.__name}\nlevel:{self.__level}\ncharacter:{self.__character}'

    def Name_The_Character(self):
        return self.__name

    def Character_Level(self):
        return self.__level


    def Pick_Your_Character(self):
        return self.__character


def Character_Battle(player1, player2):
    player1.level = player1.Character_Level()
    player2.level = player2.Character_Level()
    if player1.level > player2.level:
        print(f"{player1.Name_The_Character()}'s character's level is {player1.level},{player2.Name_The_Character()}'s character's level is {player2.level}, {player1.Name_The_Character()} wins!")

    elif player1.level == player2.level:
        print(f"{player1.Name_The_Character()}'s character's level is {player1.level},{player2.Name_The_Character()}'s character's level is {player2.level}, It's a tie!")
    else:
        print(f"{player1.Name_The_Character()}'s character's level is {player1.level},{player2.Name_The_Character()}'s character's level is {player2.level}, {player2.Name_The_Character()} wins!")


if __name__ == '__main__':
    while True:
        try:
            n= int(input("Insert your character level (0-99):"))
            if 1<=n<=99:
                break
            else:
                raise ValueError(n)
        except ValueError as e:
            print(f"Number must be integer from 1 to 99. the wrong value is {e}")

Player1 = Player('ofek', random.randint(0,n), 'Bahoor Tov')
Player2 = Player('Dekel', random.randint(0,n) , 'Chahla')

Character_Battle(Player1,Player2)
