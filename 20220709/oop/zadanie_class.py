from math import pi


class Circle:
    def __init__(self, radius=1):
        self._radius = radius
        self._area = pi * radius**2
        self._diameter = 2 * self._radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
            self._diameter = value * 2
            self._area = pi * value ** 2
        else:
            raise ValueError("Radius cannot be negative")

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2
        self._diameter = value
        self._area = pi * self._radius ** 2

    @property
    def area(self):
        return pi * self._radius ** 2

    @area.setter
    def area(self, value):
        self._area = value
        self._radius = (value / pi) ** 0.5
        self._diameter = 2 * self._radius

#
# print("Ustawienie promienia 5")
# c = Circle(5)

# c.radius
# print(c.radius)
# print(c.diameter)
# print(c.area)

# print("Promień domyślnie powinien przyjemować wartość 1:")
# c = Circle()
# print(c.radius)
# print(c.diameter)

# print("Kiedy promień się zmienia zmieniają się też średnica i pole powierzchni, np")
# c = Circle(2)
# c.radius = 1
# print(c.radius)
# print(c.diameter)
# print(c.area)
#
#
c = Circle(1)
c.diameter = 10
print(c.radius)
print(c.area)
#
# c = Circle(1)
# c.area = pi * 5 ** 2
# print(c.radius)

c = Circle(5)
c.radius = 3
c.radius = -2
print(c.radius)