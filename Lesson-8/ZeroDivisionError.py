# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления
# на нуль. Проверьте его работу на данных, вводимых пользователем. При вводе
# пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.


class ZeroDivisionErr(Exception):
    def __init__(self, txt):
        self.txt = txt


divid = input("Enter dividend: ")
divis = input("Enter division: ")

try:
    divis = int(divis)
    divid = int(divid)
    if divis == 0:
        raise ZeroDivisionErr("Деление на ноль запрещено.")
except ValueError:
    print('Not number')
except ZeroDivisionErr as err:
    print(err)
else:
    print(f"{divid}/{divis}={divid / divis}")
