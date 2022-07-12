from zadanie_1 import Circle
from math import pi, sqrt


def test_create_class():
    c = Circle(5)
    assert c.radius == 5
    assert c.diameter == 10
    assert c.area == 78.53981633974483


def test_default_radius():
    c = Circle()
    assert c.radius == 1
    assert c.diameter == 2


def test_change_radius():
    c = Circle(2)
    c.radius = 1
    assert c.diameter == 2
    assert c.area == 3.141592653589793


def test_change_diameter():
    c = Circle()
    c.diameter = 4
    assert c.radius == 2.0


def test_change_area():
    c = Circle()
    c.area = sqrt(pi * 5)


def test_negative_radius():
    c = Circle(5)
    c.radius = 5
    assert c.radius == 5
    try:
        c.radius = -2
    except ValueError as exception:
        assert True, print(f"Negative radius raised and exception {exception}")

