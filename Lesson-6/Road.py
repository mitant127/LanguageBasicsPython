# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра
# класса. Атрибуты сделать защищенными. Определить метод расчета массы
# асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного
# кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т


class Road:
    def __init__(self, lenght, widht):
        self.lenght = lenght
        self.widht = widht

    def mass(self, depth):
        self.depth = depth
        print(f"{(self.lenght * self.widht * 25 * depth)/1000} Ton")


road_1 = Road(int(input("Enter lenght Road ")), int(input("Enter widht Road ")))
road_1.mass(int(input("Enter depth Road ")))
