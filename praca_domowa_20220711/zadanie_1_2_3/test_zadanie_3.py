from zadanie_1 import Circle, Square


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
