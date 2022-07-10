from abc import ABC, abstractmethod


class IBonus(ABC):

    @abstractmethod
    def calculated(self): ...


class BonusA(IBonus):
    def calculated(self):
        print("Calculate from BonusA")


b = BonusA()