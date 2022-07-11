from zadanie_1 import Circle


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
