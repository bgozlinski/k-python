
def square_area(x: int) -> float:
    return x ** 2


def triangle_area(x, y, z):
    s = (x + y + z) / 2
    return (s*(s-x)*(s-y)*(s-z)) ** 0.5

