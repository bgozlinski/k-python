from math import pi, sqrt


class Figure:
    def __init__(self, parameter):
        self.parameter = parameter

    def __lt__(self, other):
        if self.parameter < other.parameter:
            return True
        else:
            return False

    def __le__(self, other):
        if self.parameter <= other.parameter:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.parameter > other.parameter:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.parameter >= other.parameter:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.parameter == other.parameter:
            return True
        else:
            return False

    @property
    def parameter(self):
        return self.parameter

    @parameter.setter
    def parameter(self, value):
        if value < 0:
            raise ValueError("Value cant be below 0")
        self.parameter = value


class Circle(Figure):

    @property
    def diameter(self):
        return self.parameter * 2

    @diameter.setter
    def diameter(self, value):
        self.parameter = value / 2

    @property
    def area(self):
        return pi * self.parameter ** 2

    @area.setter
    def area(self, value):
        self.parameter = sqrt(value / pi)


class Square(Figure):

    @property
    def area(self):
        return self.parameter ** 2

    # area = side^2 => side = sqrt(area)
    @area.setter
    def area(self, value):
        self.parameter = sqrt(value)


s = Square(parameter=2)
# c = Circle(2)
# c2 = Square(2)
# print(c1.area)
# print(c2.area)
#
# print(c1 > c2)
