# 7. Реализовать проект «Операции с комплексными числами». Создайте класс
# «Комплексное число», реализуйте перегрузку методов сложения и умножения
# комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f"{self.a + other.a} + {self.b + other.b}i")

    def __mul__(self, other):
        print(f"{self.a * other.a - self.b * other.b} + {self.b * other.a + self.a * other.b}i")


compi_1 = ComplexNumber(1, 2)
compi_2 = ComplexNumber(3, 4)
compi_1 + compi_2
compi_1 * compi_2
