import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Base class for all shapes."""

    def __init__(self, shape):
        self.shape = shape

    @abstractmethod
    def perimeter(self) -> float:
        """Shows a perimeter."""
        pass

    @abstractmethod
    def area(self) -> float:
        """Shows an area."""
        pass

    def __str__(self):
        return f'{self.shape} Perimeter {self.perimeter()} Area {self.area()}'


class Rectangle(Shape):
    """Class for a rectangle shape."""

    def __init__(self, user_input: str):
        parsed = user_input.split()
        if len(parsed) == 7:
            super().__init__(parsed[0])
            self.top_right_x = float(parsed[2])
            self.top_right_y = float(parsed[3])
            self.bottom_left_x = float(parsed[5])
            self.bottom_left_y = float(parsed[6])
            self.height = self.top_right_y - self.bottom_left_y
            if self.height < 0:
                raise ValueError('Wrong coordinates.')
            self.width = self.top_right_x - self.bottom_left_x
            if self.width < 0:
                raise ValueError('Wrong coordinates.')
        else:
            raise ValueError('Please, enter all parameters as shown in the example above.')

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def area(self) -> float:
        return self.width * self.height


class Square(Rectangle):
    """Class for a square shape."""

    def __init__(self, user_input: str):
        parsed = user_input.split()
        if len(parsed) == 6:
            self.side = float(parsed[5])
            if self.side < 0:
                raise ValueError("Side's value can be only positive")
            user_input = str(f'{parsed[0]} '
                             f'TopRight {float(parsed[2])} {float(parsed[3])} '
                             f'BottomLeft {float(parsed[2]) - float(parsed[5])} '
                             f'{float(parsed[3]) - float(parsed[5])}')
            super().__init__(user_input)
        else:
            raise ValueError('Please, enter all parameters as shown in the example above.')


class Circle(Shape):
    """Class for a circle shape."""

    def __init__(self, user_input: str):
        parsed = user_input.split()
        if len(parsed) == 6:
            super().__init__(parsed[0])
            self.center_x = float(parsed[2])
            self.center_y = float(parsed[3])
            self.radius = float(parsed[5])
            if self.radius < 0:
                raise ValueError("Radius' value can be only positive")
        else:
            raise ValueError('Please, enter all parameters as shown in the example above.')

    def perimeter(self) -> round:
        return round(2 * math.pi * self.radius, 2)

    def area(self) -> round:
        return round(math.pi * self.radius ** 2)


class Triangle(Shape):
    """Class for a triangle shape."""

    def __init__(self, user_input: str):
        parsed = user_input.split()
        if len(parsed) == 10:
            super().__init__(parsed[0])
            self.ax = float(parsed[2])
            self.ay = float(parsed[3])
            self.bx = float(parsed[5])
            self.by = float(parsed[6])
            self.cx = float(parsed[8])
            self.cy = float(parsed[9])
            self.a = math.sqrt((self.bx - self.cx) ** 2 + (self.by - self.cy) ** 2)
            self.b = math.sqrt((self.ax - self.cx) ** 2 + (self.ay - self.cy) ** 2)
            self.c = math.sqrt((self.bx - self.ax) ** 2 + (self.by - self.ay) ** 2)
        else:
            raise ValueError('Please, enter all parameters as shown in the example above.')

    def perimeter(self) -> round:
        return round(self.a + self.b + self.c, 2)

    def area(self) -> round:
        half_p = self.perimeter() / 2
        return round(math.sqrt(half_p * (half_p - self.a) * (half_p - self.b) * (half_p - self.c)), 2)


def parse_input(user_input: str) -> Shape:
    """Choose an available shape."""
    parsed = user_input.split()
    shape = parsed[0]
    shapes = {
        'Square': Square,
        'Rectangle': Rectangle,
        'Circle': Circle,
        'Triangle': Triangle,
    }
    cls = shapes.get(shape)
    if cls is not None:
        return cls(user_input)
    else:
        raise ValueError('An unavailable shape. Try again.')


def main():
    while True:
        user_input = input('Enter the type of shape and parameters. \n'
                           'Available shapes with examples: \n'
                           '- Square (Square TopRight 1 1 Side 1)), \n'
                           '- Rectangle (Rectangle TopRight 2 2 BottomLeft 1 1), \n'
                           '- Circle (Circle Center 1 1 Radius 2), \n'
                           '- Triangle (Triangle Point1 5 5 Point2 8 8 Point3 10 2). \n'
                           )
        output = parse_input(user_input)
        print(f'{output} \n\n ')


if __name__ == "__main__":
    main()
