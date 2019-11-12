# 6 б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import cycle
from sys import argv

name, status = argv

i = 0
if status == 'start':
    for el in cycle([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]):
        i += 1
        if i < 100:
            print(el)
        else:
            break
