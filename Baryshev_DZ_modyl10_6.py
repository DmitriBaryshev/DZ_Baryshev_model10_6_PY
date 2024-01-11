# Задание 1
import math


class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


class RightTriangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Trapezoid(Shape):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height


rectangle = Rectangle(5, 4)
print("Площадь прямоугольника:", rectangle.area())

circle = Circle(3)
print("Площадь круга:", circle.area())

triangle = RightTriangle(4, 3)
print("Площадь прямоугольного треугольника:", triangle.area())

trapezoid = Trapezoid(3, 7, 4)
print("Площадь трапеции:", trapezoid.area())


# Задание 2
import math


class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


class RightTriangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Trapezoid(Shape):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height


rectangle = Rectangle(5, 4)
print("Площадь прямоугольника:", rectangle.area())

circle = Circle(3)
print("Площадь круга:", circle.area())

triangle = RightTriangle(4, 3)
print("Площадь прямоугольного треугольника:", triangle.area())

trapezoid = Trapezoid(3, 7, 4)
print("Площадь трапеции:", trapezoid.area())


# Задание 3
import pickle


class Shape:
    def __init__(self):
        pass

    def show(self):
        pass

    def save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)


class Square(Shape):
    def __init__(self, x, y, side_length):
        self.x = x
        self.y = y
        self.side_length = side_length

    def show(self):
        print(f"Квадрат с координатами ({self.x}, {self.y}) и длиной стороны {self.side_length}")


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(f"Прямоугольник с координатами ({self.x}, {self.y}) и размерами {self.width}x{self.height}")


class Circle(Shape):
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def show(self):
        print(f"Окружность с центром в точке ({self.center_x}, {self.center_y}) и радиусом {self.radius}")


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(f"Эллипс с координатами ({self.x}, {self.y}) и размерами {self.width}x{self.height}")


# Создание списка фигур
shapes = [
    Square(0, 0, 5),
    Rectangle(2, 3, 4, 6),
    Circle(1, 1, 3),
    Ellipse(5, 5, 4, 2)
]

# Сохранение фигур в файл
filename = 'shapes.dat'
with open(filename, 'wb') as file:
    for shape in shapes:
        shape.save(filename)

# Загрузка фигур из файла
loaded_shapes = []
for _ in range(len(shapes)):
    loaded_shapes.append(Shape.load(filename))

# Отображение информации о каждой из фигур
for shape in loaded_shapes:
    shape.show()
