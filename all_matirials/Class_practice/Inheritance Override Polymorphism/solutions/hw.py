class Player:
    ID_COUNTER = 0

    def __init__(self, name, strength):
        Player.ID_COUNTER += 1
        self.id = Player.ID_COUNTER
        self.name = name
        self.strength = strength

    def __str__(self):
        return f'{type(self).__name__}: {self.name}, strength: {self.strength}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return isinstance(other, Player) and self.id == other.id

    def is_alive(self):
        return self.strength > 0

    def knock_out(self):
        last = self.strength
        self.strength = 0
        return last


class Policeman(Player):
    MAX_ARREST = 5

    def __init__(self, name, strength, arrested_criminals=None):
        super().__init__(name, strength)
        if arrested_criminals is None:
            arrested_criminals = []
        self.arrested_criminals = arrested_criminals

    def arrest_all(self):
        return len(self.arrested_criminals) == self.MAX_ARREST

    def arrest(self, criminal):
        if self.is_alive() and criminal.is_alive() and not self.arrest_all():
            if self.strength > criminal.strength:
                self.strength -= criminal.knock_out()
                criminal.arrest()
                self.arrested_criminals.append(criminal)
                return True
            if criminal.strength > self.strength:
                criminal.strength -= self.knock_out()
                return False
            self.knock_out()
            criminal.knock_out()
        return False

    def show_arrested_criminals(self):
        print(self.__str__())
        for c in self.arrested_criminals:
            print(f'\t{c}')


class Criminal(Player):
    def __init__(self,name, strength):
        super().__init__(name, strength)
        self.num_of_arrest = 0

    def __str__(self):
        return f'{super().__str__()}, arrest: {self.num_of_arrest}'

    def __repr__(self):
        return self.__str__()

    def arrest(self):
        self.num_of_arrest += 1


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
    for policeman in police_mans:
        for criminal in criminals:
            if policeman.arrest(criminal):
                print(f'{policeman.name} arrested {criminal}')

    for policeman in police_mans:
        policeman.show_arrested_criminals()


if __name__ == '__main__':
    main()