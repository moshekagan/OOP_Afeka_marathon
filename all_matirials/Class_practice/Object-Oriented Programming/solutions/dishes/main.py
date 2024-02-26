import csv


class Ingredient:
    HEALTH_VALUE = 100
    CARBS_FACTOR = 4
    FATS_FACTOR = 9
    PROTEINS_FACTOR = 4

    def __init__(self, name, carbs, fats, proteins):
        self.name = name
        self.carbs = carbs
        self.fats = fats
        self.proteins = proteins

    def __str__(self):
        return f'{self.name}\t{self.calculate_calories()} Kcal per 100g'

    def __repr__(self):
        return self.__str__()

    def calculate_calories(self):
        return round(self.carbs * self.CARBS_FACTOR \
                     + self.fats * self.FATS_FACTOR \
                     + self.proteins * self.PROTEINS_FACTOR, 2)

    def is_healthy(self):
        return self.calculate_calories() < self.HEALTH_VALUE


class Dish:
    MAX_INGREDIENTS = 7

    def __init__(self, name, is_vegetarian=False):
        self.name = name
        self.is_vegetarian = is_vegetarian
        self.ingredients = []

    def __str__(self):
        is_vegetarian = 'vegetarian' if self.is_vegetarian else 'not vegetarian'
        st = f'{self.name},{is_vegetarian}, total: {self.calculate_total_calories()} Kcal\n'
        for item in self.ingredients:
            st += f'\t{str(item[0])}, weight: {str(item[1])} \n'
        return st

    def calculate_total_calories(self):
        total_calories = 0
        for item in self.ingredients:
            total_calories += item[0].calculate_calories() * (item[1] / 100)
        return round(total_calories, 2)

    def can_add_ingredient(self, ingredient, weight):
        return len(self.ingredients) < self.MAX_INGREDIENTS \
            and (ingredient, weight) not in self.ingredients

    def add_ingredient(self, ingredient, weight):
        if self.can_add_ingredient(ingredient, weight):
            self.ingredients.append((ingredient, weight))
            return True
        return False

    def remove_ingredient(self, ingredient):
        self.ingredients.remove(ingredient)

    def display_menu(self):
        is_vegetarian = 'vegetarian' if self.is_vegetarian else 'not vegetarian'
        return f'{self.name},{is_vegetarian}, total: {self.calculate_total_calories()} Kcal'


def read_ingredients_list(filename):
    d = {}
    csv_file = open(filename)
    read = csv.reader(csv_file)
    next(read)
    for row in read:
        name = row[0]
        carbs = float(row[1])
        fats = float(row[2])
        proteins = float(row[3])
        ingredient = Ingredient(name, carbs, fats, proteins)
        d[name] = ingredient
    csv_file.close()
    return d


def read_dishes_list(filename, ingredients_dict):
    dishes = []
    dishes_file = open(filename, 'r')
    for row in dishes_file:
        dish_attributes = row.rstrip().split(',')
        name = dish_attributes[0]
        is_vegetarian = dish_attributes[1] == 'True'
        dish = Dish(name, is_vegetarian)
        ingredient_amount = int(dish_attributes[2])
        for line in range(ingredient_amount):
            ingredient_line = dishes_file.readline().rstrip().split(',')
            ingredient_name = ingredient_line[0]
            ingredient_weight = int(ingredient_line[1])
            dish.add_ingredient(ingredients_dict[ingredient_name], ingredient_weight)
        # print(dish)
        dishes.append(dish)
    dishes_file.close()
    return dishes


def create_dishes(ingredients_dict):
    dishes = []
    bread = Dish('bread', True)
    bread.add_ingredient(ingredients_dict['butter'], 20)
    bread.add_ingredient(ingredients_dict['honey'], 40)
    bread.add_ingredient(ingredients_dict['flour'], 150)
    dishes.append(bread)

    lentil_soup = Dish('lentil soup', True)
    lentil_soup.add_ingredient(ingredients_dict['olive oil'], 30)
    lentil_soup.add_ingredient(ingredients_dict['lentil'], 50)
    lentil_soup.add_ingredient(ingredients_dict['onion'], 120)
    lentil_soup.add_ingredient(ingredients_dict['garlic'], 30)
    lentil_soup.add_ingredient(ingredients_dict['celery'], 150)
    dishes.append(lentil_soup)

    vegetable_salad = Dish('vegetable salad', True)
    vegetable_salad.add_ingredient(ingredients_dict['olive oil'], 30)
    vegetable_salad.add_ingredient(ingredients_dict['cucumber'], 90)
    vegetable_salad.add_ingredient(ingredients_dict['tomato'], 120)
    vegetable_salad.add_ingredient(ingredients_dict['lettuce'], 150)
    dishes.append(vegetable_salad)

    sweet_potato_patties = Dish('sweet potato patties', True)
    sweet_potato_patties.add_ingredient(ingredients_dict['egg'], 120)
    sweet_potato_patties.add_ingredient(ingredients_dict['sweet potato'], 150)
    sweet_potato_patties.add_ingredient(ingredients_dict['flour'], 30)
    sweet_potato_patties.add_ingredient(ingredients_dict['olive oil'], 30)
    dishes.append(sweet_potato_patties)

    chicken_and_leek_meatballs = Dish('chicken and leek meatballs')
    chicken_and_leek_meatballs.add_ingredient(ingredients_dict['olive oil'], 30)
    chicken_and_leek_meatballs.add_ingredient(ingredients_dict['leeks'], 150)
    chicken_and_leek_meatballs.add_ingredient(ingredients_dict['breadcrumbs'], 30)
    chicken_and_leek_meatballs.add_ingredient(ingredients_dict['garlic'], 20)
    chicken_and_leek_meatballs.add_ingredient(ingredients_dict['celery'], 80)
    chicken_and_leek_meatballs.add_ingredient(ingredients_dict['chicken'], 150)
    dishes.append(chicken_and_leek_meatballs)

    chicken_stuffed_with_rice = Dish('chicken stuffed with rice')
    chicken_stuffed_with_rice.add_ingredient(ingredients_dict['olive oil'], 20)
    chicken_stuffed_with_rice.add_ingredient(ingredients_dict['chicken'], 150)
    chicken_stuffed_with_rice.add_ingredient(ingredients_dict['onion'], 120)
    chicken_stuffed_with_rice.add_ingredient(ingredients_dict['garlic'], 30)
    chicken_stuffed_with_rice.add_ingredient(ingredients_dict['rice'], 120)
    dishes.append(chicken_stuffed_with_rice)
    return dishes


def show_menu(dishes):
    if len(dishes) == 0:
        return 9
    print('Menu :')
    for i, dish in enumerate(dishes):
        print(f'{i + 1}: {dish.display_menu()}')
    return int(input('Enter Dish number or 9 for Exit : '))


def main():
    ingredients_dict = read_ingredients_list('ingredients_list.csv')
    dishes = read_dishes_list('dishes_list.txt', ingredients_dict)
    quit_chose = False
    user_dishes = []
    while not quit_chose:
        user_chosen = show_menu(dishes)
        quit_chose = user_chosen == 9
        if not quit_chose:
            user_dishes.append(dishes[user_chosen - 1])
    if len(user_dishes) > 0:
        print('\nyour dishes are :')
        print('\n'.join(str(dish.display_menu()) for dish in user_dishes))
    print('By...')


if __name__ == '__main__':
    main()
