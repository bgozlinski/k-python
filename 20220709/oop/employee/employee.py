from abc import ABC, abstractmethod


class Employee:
    def __init__(self, name, rate_per_hour):
        self.name = name
        self.rate_per_hour = rate_per_hour
        self.worked_hours = 0

    def pay_salary(self):
        if self.worked_hours > 8:
            to_pay = (
                8 * self.rate_per_hour
                + (self.worked_hours - 8) * self.rate_per_hour * 2
            )
        else:
            to_pay = self.rate_per_hour * self.worked_hours
        self.worked_hours = 0
        return to_pay

    def register_time(self, hours):
        self.worked_hours = hours


class IBonus(ABC):

    @abstractmethod
    def calculate(self):
        pass


class Bonus(IBonus):
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Bonus):
            return self.__class__(self.value + other.value)


class ValueBonus(Bonus):
    order = 2

    def calculate(self, to_pay: int):
        return to_pay + self.value


class PercentBonus(Bonus):
    order = 1

    def calculate(self, to_pay: int):
        return (to_pay * self.value/100) + to_pay


class ExtraBonus(Bonus):
    order = 3

    def calculate(self, to_pay: int):
        return to_pay + 2 * self.value


class PremiumEmployee(Employee):
    def __init__(self, name, rate_per_hour):
        super().__init__(name, rate_per_hour)
        self.bonusList = {}

    def pay_salary(self):
        to_pay = super().pay_salary()

        for bonus in sorted(self.bonusList.values(), key=lambda x: x.order):
            to_pay = bonus.calculate(to_pay)

        return to_pay

    def give_bonus(self, bonus: Bonus):
        if bonus.__class__ in self.bonusList:
            self.bonusList[bonus.__class__] += bonus
        else:
            self.bonusList[bonus.__class__] = bonus
