# 6. а) скрипт бесконечный итератор, генерирующий целые числа, начиная с указанного

from itertools import count
from sys import argv

name, start_num = argv

for el in count(int(start_num)):
    if el < 1000:
        print(el)
    else:
        break

