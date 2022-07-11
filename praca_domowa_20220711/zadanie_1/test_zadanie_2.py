from zadanie_1 import Circle

def test_operator_overloading():
    c1 = Circle()
    c2 = Circle(2)

    assert(c1 == c2) == False
    assert(c1 > c2) == False
    assert(c1 < c2) == True
    assert(c1 <= c2) == True
    assert(c1 >= c2) == False
    assert(c1 + c2) == 2.23606797749979
