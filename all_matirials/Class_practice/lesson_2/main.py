class ArrestedOverflowError(Exception):
    def __init__(self):
        super().__init__('amount of arrested overflow')


class Player:
    ID = 0

    def __init__(self, name, strength):
        Player.ID += 1
        self.__id = f'player_{Player.ID}'
        self.__name = name
        self.__strength = strength

    def __str__(self):
        return f'{self.__class__.__name__}: {self.__id}, {self.__name}, strength: {self.__strength}'

    def is_alive(self):
        return self.__strength > 0

    def knock_out(self):
        temp = self.__strength
        self.__strength = 0
        return temp

    def get_strength(self):
        return self.__strength

    def set_strength(self, strength):
        self.__strength = strength

    def get_name(self):
        return self.__name


class Criminal(Player):
    def __init__(self, name, strength):
        super().__init__(name, strength)
        self.__num_of_arrested = 0

    def __str__(self):
        return f'{super().__str__()}, arrest: {self.__num_of_arrested}'

    def arrest(self):
        self.__num_of_arrested += 1


class Policeman(Player):
    MAX_ARRESTED = 5

    def __init__(self, name, strength, arrested_criminals=None):
        super().__init__(name, strength)
        if arrested_criminals is None:
            arrested_criminals = []
        if len(arrested_criminals) > Policeman.MAX_ARRESTED:
            raise ArrestedOverflowError()
        self.__arrested_criminals = arrested_criminals

    def arrested_all(self):
        return len(self.__arrested_criminals) == Policeman.MAX_ARRESTED

    def arrest(self, criminal: Criminal):
        if (self.is_alive()
                and criminal.is_alive()
                and not self.arrested_all()):
            if self.get_strength() > criminal.get_strength():
                temp = criminal.knock_out()
                self.set_strength(self.get_strength() - temp)
                criminal.arrest()
                self.__arrested_criminals.append(criminal)
                return True
            elif criminal.get_strength() > self.get_strength():
                temp = self.knock_out()
                criminal.set_strength(criminal.get_strength() - temp)
                return False
            else:
                self.knock_out()
                criminal.knock_out()
                return False
        else:
            return False

    def show_arrested_criminals(self):
        print(self)
        for c in self.__arrested_criminals:
            print(f'\t{c}')


def main():
    police_mans = [
        Policeman("Moshe", 12),
        Policeman("Kobi", 15),
        Policeman("Yael", 10),
    ]
    criminals = [
        Criminal("Moshe", 4),
        Criminal("Kobi", 3),
        Criminal("Yael", 5),
        Criminal("Mor", 2),
        Criminal("Tom", 12),
        Criminal("Yosi", 9),
    ]
    try:
        test_police = Policeman("Moshe", 12, criminals)
    except ArrestedOverflowError as e:
        print(e)

    for policeman in police_mans:
        for criminal in criminals:
            if policeman.arrest(criminal):
                print(f'{policeman.get_name()} arrested {criminal}')

    for policeman in police_mans:
        policeman.show_arrested_criminals()


main()
