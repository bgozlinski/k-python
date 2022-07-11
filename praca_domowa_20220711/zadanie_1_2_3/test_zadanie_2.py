from zadanie_1 import Circle

def test_operator_overloading():
    c1 = Circle()  # area 3.14
    c2 = Circle(2)  # area 12.56

    assert(c1 == c2) == False
    assert(c1 > c2) == False
    assert(c1 < c2) == True
    assert(c1 <= c2) == True
    assert(c1 >= c2) == False
    assert(c1 + c2) == 15.707963267948966




