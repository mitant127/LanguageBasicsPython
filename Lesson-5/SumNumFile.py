# 5. Создать (программно) текстовый файл, записать в него программно набор
# чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел
# в файле и выводить ее на экран.

from random import randint

with open('file5.txt', 'w') as f_out:
    f_out.write(' '.join([str(randint(0, 100)) for i in range(randint(10, 20))]))

with open('file5.txt') as f_inp:
    e = f_inp.read()
    print(e)
    print(sum(map(int, e.split())))
