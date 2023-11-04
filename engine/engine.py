from colorama import Fore, init

init(autoreset=True)


class Engine2D:
    def __init__(self):
        self.canvas = []
        self.current_color = Fore.WHITE  # Устанавливаем начальный цвет

    def set_color(self, color):
        self.current_color = color

    def add_shape(self, shape):
        self.canvas.append(shape)

    def draw(self):
        for shape in self.canvas:
            shape.draw(self.current_color)
        self.canvas = []


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def draw(self, color):
        print(f"{color}Drawing Circle: ({self.center[0]}, {self.center[1]}) with radius {self.radius}")


class Triangle:
    def __init__(self, vertices):
        self.vertices = vertices

    def draw(self, color):
        print(f"{color}Drawing Triangle: {self.vertices}")


class Rectangle:
    def __init__(self, top_left, width, height):
        self.top_left = top_left
        self.width = width
        self.height = height

    def draw(self, color):
        print(f"{color}Drawing Rectangle: {self.top_left}, width {self.width}, height {self.height}")


# Пример использования:

engine = Engine2D()

# Устанавливаем красный цвет
engine.set_color(Fore.RED)

# Создаем и добавляем фигуры
circle = Circle((0, 1), 5)
triangle = Triangle([(0, 0), (1, 0), (0, 1)])
rectangle = Rectangle((1, 1), 3, 2)

engine.add_shape(circle)
engine.add_shape(triangle)
engine.add_shape(rectangle)

# Рисуем все фигуры
engine.draw()

# Устанавливаем зеленый цвет
engine.set_color(Fore.GREEN)

# Создаем и добавляем еще фигуры
circle = Circle((2, 3), 4)
triangle = Triangle([(1, 1), (2, 1), (1, 2)])
rectangle = Rectangle((2, 2), 4, 3)

engine.add_shape(circle)
engine.add_shape(triangle)
engine.add_shape(rectangle)

# Рисуем все фигуры
engine.draw()
