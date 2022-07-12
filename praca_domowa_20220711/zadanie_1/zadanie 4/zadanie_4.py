from math import pi, sqrt


class Figure:
    def __init__(self, parameter):
        self.parameter = parameter

    def __add__(self, other):
        if isinstance(other, Figure):
            return self.area + other.area
        else:
            return Figure(self.area + other.area)

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
        if self.area == other.area:
            return True
        else:
            return False

    @property
    def parameter(self):
        return self._parameter

    @parameter.setter
    def parameter(self, value):
        if value < 0:
            raise ValueError("Value cant be below 0")
        self._parameter = value


class Circle(Figure):
    def __init__(self, parameter=1):
        super().__init__(parameter)

    @property
    def diameter(self):
        return self.parameter * 2

    @diameter.setter
    def diameter(self, value):
        self.parameter = value / 2

    @property
    def area(self):
        return pi * self.parameter**2

    @area.setter
    def area(self, value):
        self.parameter = sqrt(value / pi)


class Square(Figure):
    def __init__(self, parameter=1):
        super().__init__(parameter)

    @property
    def area(self):
        return self.parameter**2

    # area = side^2 => side = sqrt(area)
    @area.setter
    def area(self, value):
        self.parameter = sqrt(value)


class Triangle(Figure):
    def __init__(self, parameter=1):
        super().__init__(parameter)

    @property
    def area(self):
        return (self.parameter**2 * sqrt(3)) / 4

    @area.setter
    def area(self, value):
        self.parameter = 2 * sqrt((value * sqrt(3)) / 3)
