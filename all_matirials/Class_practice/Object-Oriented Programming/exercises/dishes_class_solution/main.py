import csv


class Ingredient:
    def __init__(self, name, carb, fats, proteins):
        self.__name = name
        self.__carb = carb
        self.__fats = fats
        self.__proteins = proteins

    def __str__(self):
        return (f'{self.__name}, {self.__carb},'
                f' {self.__fats}, {self.__proteins}')

    def calculate_calories(self):
        pass

    def is_healthy(self):
        pass

    def get_name(self):
        return self.__name

    def get_carb(self):
        return self.__carb

    def get_fats(self):
        return self.__fats

    def get_proteins(self):
        return self.__proteins


class Dish:
    MAX_INGREDIENTS = 7

    def __init__(self, name, is_vegetarian, ingredients):
        self.__name = name
        self.__is_vegetarian = is_vegetarian
        self.__ingredients = ingredients

    def __str__(self):
        return "need to implementation..."

    def calculate_total_calories(self):
        return 0

    def add_ingredient(self):
        pass

    def remove_ingredient(self):
        pass


def read_ingredients(filename):
    ingredients = []
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader) # ignore header
        for row in reader:
            ingredients.append(
                Ingredient(row[0],
                           float(row[1]),
                           float(row[2]),
                           float(row[3])))
    return ingredients


def main():
    ingredients = read_ingredients('ingredients_list.csv')
    ingredients_dict = {i.get_name():
                            (i.get_carb(),
                             i.get_fats(),
                             i.get_proteins()) for i in ingredients}
    print(ingredients_dict)



main()


