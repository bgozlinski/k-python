from math import pi


class Circle:
    def __init__(self, radius=1):
        self.radius = radius

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
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return pi * self.radius**2

    @area.setter
    def area(self, value):
        self.radius = (value / pi) ** 0.5


c = Circle(5)
assert c.radius == 5
assert c.diameter == 10
assert c.area == 78.53981633974483

c = Circle()
assert c.radius == 1
assert c.diameter == 2

c = Circle(2)
c.radius = 1
assert c.diameter == 2
assert c.area == 3.141592653589793

c = Circle(1)
c.diameter = 4
assert c.radius == 2.0

c = Circle(1)
c.area = pi * 5**2
assert c.radius == 5.0

c = Circle(5)
c.radius = 3
c.radius = -2
