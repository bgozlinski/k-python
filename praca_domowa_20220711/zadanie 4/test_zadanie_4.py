from zadanie_4 import Circle, Square, Triangle
from math import pi, sqrt


def test_circle():
    c = Circle(5)
    assert c.parameter == 5
    assert c.diameter == 10
    assert c.area == 78.53981633974483

    c = Circle()
    assert c.parameter == 1
    assert c.diameter == 2
    assert c.area == 3.141592653589793

    c = Circle()
    c.diameter = 4
    assert c.parameter == 2.0

    c = Circle()
    c.area = pi * 5**2
    assert c.parameter == 5.0


def test_negative_radius():
    c = Circle(5)
    c.parameter = 5
    assert c.parameter == 5
    try:
        c.parameter = -2
    except ValueError as exception:
        assert True, print(f"Value cant be below 0 {exception}")


def test_square():
    s = Square()
    assert s.parameter == 1
    assert s.area == 1

    s = Square(5)
    assert s.parameter == 5
    assert s.area == 25

    s = Square(5)
    assert s.parameter == 5
    assert s.area == 25

    s.area = 36
    assert s.parameter == 6


def test_triangle():
    t = Triangle()
    assert t.parameter == 1
    assert t.area == 0.4330127018922193

    t = Triangle(5)
    assert t.parameter == 5
    assert t.area == 10.825317547305483

    t.area = 36
    assert t.parameter == 9.11802822781911


def test_circle_overloading():
    c1 = Circle()  # area 3.14
    c2 = Circle(2)  # area 12.56

    assert (c1 == c2) == False
    assert (c1 > c2) == False
    assert (c1 < c2) == True
    assert (c1 <= c2) == True
    assert (c1 >= c2) == False
    assert (c1 + c2) == 15.707963267948966


def test_square_overloading():
    s1 = Square(5)
    s2 = Square(8)
    assert (s1 == s2) == False
    assert (s1 + s2) == 89

    s2 = Square(5)
    assert (s1 == s2) == True
    assert (s1 + s2) == 50


def test_figures_overloading():

    s1 = Square(5)
    s2 = Square(8)
    c1 = Circle()
    c2 = Circle(3)
    t1 = Triangle()
    t2 = Triangle(5)

    assert ((s1 + c1) and (c1 + s1)) == 28.141592653589793
    assert ((s2 + c2) and (c2 + s2)) == 92.27433388230814
    assert ((t1 + c1) and (c1 + t1)) == 0.4330127018922193 + 3.141592653589793
    assert ((t2 + c2) and (c2 + t2)) == 39.09965142961362
    assert t1 + s1 + c1 == 0.4330127018922193 + 28.141592653589793
