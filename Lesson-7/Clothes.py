# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь
# определенное название. К типам одежды в этом проекте относятся пальто и
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост
# (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих
# методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на
# этом уроке знания: реализовать абстрактные классы для основных классов
# проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(size)
        self.size = size
        self.name = name

    @property
    def tissue_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(height)
        self.height = height
        self.name = name

    @property
    def tissue_consumption(self):
        return 2 * self.height + 0.3


coat_1 = Coat("Coat_48", 48)
print(f"Расход ткани на польто размера {coat_1.size}: {coat_1.tissue_consumption}")
suit_1 = Suit("Suit_180", 180)
print(f"Расход ткани на костюм на рост {suit_1.height}: {suit_1.tissue_consumption}")
