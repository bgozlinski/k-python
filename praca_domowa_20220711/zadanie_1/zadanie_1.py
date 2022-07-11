#  zadanie 1
#  Stwórz klasę reprezentującą okręg (Circle)
#
#  Okrąg powinien mieć promień (radius), średnicę (diameter) i pole powierzchni (area) oraz przy-
#  jemną reprezentację napisową

from math import pi, sqrt

class Circle():

    def __init__(self, radius=1):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self._radius = value /2

    @property
    def area(self):
        return pi * self._radius ** 2

    @area.setter
    def area(self, value):
        self._radius = sqrt(value / pi)
