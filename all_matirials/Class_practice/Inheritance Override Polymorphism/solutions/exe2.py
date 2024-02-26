import math


class Shape:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f'{self.__class__.__name__} : {self.color}'

    def get_perimeter(self):
        return 'not implemented yet'

    def get_area(self):
        return 'not implemented yet'


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def __str__(self):
        return f'{super().__str__()}, {self.radius}'

    def get_perimeter(self):
        return self.radius * 2 * math.pi

    def get_area(self):
        return self.radius ** 2 * math.pi


class Square(Shape):
    def __init__(self, color, length):
        super().__init__(color)
        self.length = length

    def __str__(self):
        return f'{super().__str__()}, {self.length}'

    def get_perimeter(self):
        return self.length * 4

    def get_area(self):
        return self.length * self.length

    def draw(self):
        print('\n'.join([' '.join(['*' for _ in range(self.length)]) for _ in range(self.length)]))


class Rectangle(Square):
    def __init__(self, color, width, height):
        super().__init__(color, width)
        self.height = height

    def __str__(self):
        return f'{super().__str__()}, {self.height}'

    def get_perimeter(self):
        return (self.length + self.height) * 2

    def get_area(self):
        return self.length * self.height

    def draw(self):
        print('\n'.join([' '.join(['*' for _ in range(self.length)]) for _ in range(self.height)]))


menu = [
    "1. Create Square",
    "2. Create Rectangle",
    "3. Create Circle",
    "4. Get perimeter for shape",
    "5. Get area for shape",
    "6. Show all shapes",
    "7. EXIT",
]


def display_menu(l1, title):
    print()
    print(title)
    for item in l1:
        print(item)


def create_shapes_menu(shapes):
    shapes_menu = []
    for ind, shape in enumerate(shapes):
        shapes_menu.append(f'{ind + 1} :{shape}')
    shapes_menu.append(f'{len(shapes) + 1} :Exit choice')
    return shapes_menu



def is_valid_input(i, l1):
    return i.isdigit() and 1 <= int(i) <= len(l1) + 1


def get_valid_user_choice(l1):
    user_input = input("What is your choice? ")

    while not is_valid_input(user_input, l1):
        print(f"Invalid input! Please choose number option from the menu: {1} - {len(l1) + 1} ")
        user_input = input("What is your choice? ")

    return int(user_input)


def create_square(shapes):
    color = input("insert color: ")
    length = int(input("insert length: "))
    shapes.append(Square(color, length))


def create_rectangle(shapes):
    color = input("insert color: ")
    width = int(input("insert width: "))
    height = int(input("insert height: "))
    shapes.append(Rectangle(color, width, height))


def create_circle(shapes):
    color = input("insert color: ")
    radius = int(input("insert radius: "))
    shapes.append(Circle(color, radius))


def show_all_shapes(shapes):
    print('Shapes:')
    for shape in shapes:
        print(shape)
        if isinstance(shape, Square):
            shape.draw()


def get_shape(shapes):
    if len(shapes) == 0:
        print('No shapes yet')
        return
    user_choice = -1
    shapes_menu = create_shapes_menu(shapes)
    while user_choice != len(shapes) + 1:
        display_menu(shapes_menu, '--- Shapes List ---')
        user_choice = get_valid_user_choice(shapes)
        if user_choice - 1 < len(shapes):
            return shapes[user_choice - 1]


def show_perimeter(shapes):
    shape = get_shape(shapes)
    if shape is not None:
        print(f'perimeter: {shape.get_perimeter()}')


def show_area(shapes):
    shape = get_shape(shapes)
    if shape is not None:
        print(f'area: {shape.get_area()}')


def main():
    global menu
    shapes = []
    user_choice = -1

    while user_choice != len(menu):
        display_menu(menu, '--- MENU ---')
        user_choice = get_valid_user_choice(menu)

        if user_choice == 1:
            create_square(shapes)
        elif user_choice == 2:
            create_rectangle(shapes)
        elif user_choice == 3:
            create_circle(shapes)
        elif user_choice == 4:
            show_perimeter(shapes)
        elif user_choice == 5:
            show_area(shapes)
        elif user_choice == 6:
            show_all_shapes(shapes)
        
    print("Bye Bye!")


if __name__ == '__main__':
    main()
