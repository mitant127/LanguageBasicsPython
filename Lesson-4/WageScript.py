# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия. Для выполнения расчета для
# конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv

name, worked_h, wage_h, prize = argv


def wage(worked_h, wage_h, prize):
    return worked_h * wage_h + prize


print(name)
print(wage(int(worked_h), int(wage_h), int(prize)))
