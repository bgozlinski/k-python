from mathematica.geometry.figures import square_area, triangle_area


def test_square_area():
    assert square_area(2) == 4
    assert square_area(6) == 12


def test_triangle_area():
    assert triangle_area(8, 3, 9) == 10
    assert triangle_area(4, 5, 3) == 6
