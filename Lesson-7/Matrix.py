# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
# класса (метод __init__()), который должен принимать данные (список списков)
# для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных
# в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы
# в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции
# сложения двух объектов класса Matrix (двух матриц). Результатом сложения
# должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки
# второй матрицы и т.д.

import random

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, el)) for el in self.matrix])

    def __add__(self, other):
        summ = []
        i = 0
        while i < len(other.matrix):
            summ.append([sum(x) for x in zip(other.matrix[i], self.matrix[i])])
            i += 1
        return '\n'.join(['\t'.join(map(str, el)) for el in summ])


def matrix_3x3():
    return [[random.randint(0, 100) for _ in range(3)] for _ in range(3)]


matrx = Matrix(matrix_3x3())
print(f"{matrx}\n")
matrx2 = Matrix(matrix_3x3())
print(f"{matrx2}\n")
print(matrx + matrx2)
