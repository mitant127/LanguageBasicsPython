# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

# о денении на ноль - https://www.youtube.com/watch?v=ICYPwVELEvs

def division(a, b):
    return a / b


def checktype():
    while True:
        val = input(": ")
        if val.isalpha():
            print("Вы ввели не число")
        else:
            val = float(val)
            return val


print("Введите делимое - ")
arg_1 = checktype()
print("Введите делитель - ")
arg_2 = checktype()

if arg_2 == 0:
    if arg_1 == 0:
        print("При делении ноля на ноль мы получаем любое число (неопределенность)")
    else:
        print("Делить на ноль нельзы, но спецыально для вас мы это сделаем!")
        print('∞')
else:
    print(division(arg_1, arg_2))
