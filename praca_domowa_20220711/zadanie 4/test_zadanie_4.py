from zadanie_4 import Circle, Square
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
        assert True, print(f"Value cant be below 0 {exception}")


def test_operator_overloading():
    c1 = Circle()  # area 3.14
    c2 = Circle(2)  # area 12.56

    assert(c1 == c2) == False
    assert(c1 > c2) == False
    assert(c1 < c2) == True
    assert(c1 <= c2) == True
    assert(c1 >= c2) == False
    assert(c1 + c2) == 15.707963267948966


def test_square():
    s1 = Square(5)
    s2 = Square(8)
    assert (s1 == s2) == False
    assert (s1 + s2) == 89

    s2 = Square(5)
    assert (s1 == s2) == True
    assert (s1 + s2) == 50

    s1 = Square(5)
    s2 = Square(8)
    c1 = Circle()
    c2 = Circle(3)
    assert ((s1 + c1) and (c1 + s1)) == 28.141592653589793
    assert ((s2 + c2) and (c2 + s2)) == 92.27433388230814




# c = Circle()
# print(c.radius)
# s = Square(2)
# print(s.side)
# print("")
# print(c.area)
# print(s.area)
# print("")
# sum = c.area + s.area
# print(sum)
# print("")
# print(c.area > s.area)