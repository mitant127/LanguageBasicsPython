# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим
# очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fibo_gen(). Функция
# отвечает за получение факториала числа, а в цикле необходимо выводить только
# первые 15 чисел.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например,
# факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.


def fibo_gen(n):
    n += 1
    num = 1
    for el in range(1, n, +1):
        num *= el
        yield num

j = 0
for i in fibo_gen(55):
    j += 1
    if j < 16:
        print(i)
    else:
        break
