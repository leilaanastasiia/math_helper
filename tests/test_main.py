import pytest
from math import pi
from main import Square, Rectangle, Circle, Triangle, parse_input


def test_invalid_shape():
    with pytest.raises(ValueError) as err_info:
        parse_input("Squareeee")
    assert str(err_info.value) == "An unavailable shape. Try again."


def test_valid_shape():
    result = parse_input("Square TopRight 2 2 Side 5")
    assert result.perimeter() == 20
    assert result.area() == 25
    assert isinstance(result, Square)


def test_square_valid_input():
    square = Square("Square TopRight 2 2 Side 5")
    assert square.perimeter() == 20
    assert square.area() == 25


def test_square_invalid_side():
    with pytest.raises(ValueError) as err_info:
        Square("Square TopRight 2 2 Side -2")
    assert str(err_info.value) == "Side's value can be only positive"


def test_square_lost_parameters():
    with pytest.raises(ValueError) as err_info:
        Square("Square Side 5")
    assert str(err_info.value) == "Please, enter all parameters as shown in the example above."


def test_rectangle_valid_input():
    rectangle = Rectangle("Rectangle TopRight 3 3 BottomLeft 1 1")
    assert rectangle.perimeter() == 8
    assert rectangle.area() == 4


def test_rectangle_invalid_parameters():
    with pytest.raises(ValueError) as err_info:
        Rectangle("Rectangle TopRight -2 3 BottomLeft 1 1")
    assert str(err_info.value) == "Wrong coordinates."
    with pytest.raises(ValueError) as err_info:
        Rectangle("Rectangle TopRight 3 -2 BottomLeft 1 1")
    assert str(err_info.value) == "Wrong coordinates."


def test_rectangle_lost_parameters():
    with pytest.raises(ValueError) as err_info:
        Rectangle("Rectangle TopRight 2 3")
    assert str(err_info.value) == "Please, enter all parameters as shown in the example above."


def test_circle_valid_input():
    circle = Circle("Circle Center 1 1 Radius 3")
    assert circle.perimeter() == round(18.85, 2)
    assert circle.area() == round(28, 2)


def test_circle_invalid_radius():
    with pytest.raises(ValueError) as err_info:
        Circle("Circle Center 1 1 Radius -2")
    assert str(err_info.value) == "Radius' value can be only positive"


def test_circle_lost_parameters():
    with pytest.raises(ValueError) as err_info:
        Circle("Circle Radius -2")
    assert str(err_info.value) == "Please, enter all parameters as shown in the example above."


def test_triangle_valid_input():
    triangle = Triangle("Triangle Point1 5 5 Point2 8 8 Point3 10 2")
    assert triangle.perimeter() == round(16.4, 2)
    assert triangle.area() == round(12.01, 2)


def test_triangle_lost_parameters():
    with pytest.raises(ValueError) as err_info:
        Triangle("Triangle Point1 5 5 ")
    assert str(err_info.value) == "Please, enter all parameters as shown in the example above."
