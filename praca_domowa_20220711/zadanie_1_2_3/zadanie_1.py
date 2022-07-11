#  zadanie 1,2


from math import pi, sqrt


class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def __add__(self, other):
        # area = self.area + other.area
        # return sqrt(area / pi)
        return self.area + other.area

    def __lt__(self, other):
        if self.radius < other.radius:
            return True
        else:
            return False

    def __le__(self, other):
        if self.radius <= other.radius:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.radius > other.radius:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.radius >= other.radius:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2

    @property
    def area(self):
        return pi * self._radius**2

    @area.setter
    def area(self, value):
        self._radius = sqrt(value / pi)


class Square:
    def __init__(self, side):
        self.side = side

    def __add__(self, other):
        return self.area + other.area

    def __eq__(self, other):
        if self.side == other.side:
            return True
        else:
            return False

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = value

    @property
    def area(self):
        return self.side**2

    # area = side^2 => side = sqrt(area)
    @area.setter
    def area(self, value):
        self.side = sqrt(value)


s1 = Square(5)
s2 = Square(8)
c1 = Circle()
c2 = Circle(3)

print(
    f"Circle radius: {c1.radius}   area: {c1.area}\n"
    f"Square side:   {s1.side}   area: {s1.area}"
)
print(f"{s2 + c2}")
print(f"{c2 + s2}")
