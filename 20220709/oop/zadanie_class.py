from math import pi


class Circle:
    def __init__(self, radius=1):
        self._radius = radius
        self._area = pi * radius ** 2
        self._diameter = 2 * self._radius

    @property
    def diameter(self):
        return self._diameter

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return self._area

    @diameter.setter
    def diameter(self, value):
        self._diameter = value

    @radius.setter
    def radius(self, value):
        self._radius = value

    @area.setter
    def area(self, value):
        self._area = value






    # @property
    # def radius(self):
    #     return len(self.radius)


c = Circle(5)

print(c.radius)

print(c.diameter)

c.diameter = 2
print(c.diameter)
print(c.radius)

c.radius = 1000

print(c.radius)

