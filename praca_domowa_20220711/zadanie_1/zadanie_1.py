#  zadanie 1
#  Stwórz klasę reprezentującą okręg (Circle)
#
#  Okrąg powinien mieć promień (radius), średnicę (diameter) i pole powierzchni (area) oraz przy-
#  jemną reprezentację napisową

from math import pi, sqrt


class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def __add__(self, other):
        area = self.area + other.area
        return sqrt(area / pi)

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

c1 = Circle()
c2 = Circle(2)

print(c1 == c2)

print(c1>c2)

print(c1<c2)

print(c1<=c2)

print(c1>=c2)

c3 = c1 + c2
print(c3)