# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может
# продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма
# вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
# вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно
# добавить сумму этих чисел к полученной ранее сумме и после этого завершить
# программу.

summa = 0
exit = 0


while True:
    print("Enter a number with a space")
    text = input("Fot exit enter 'q'")
    my_list = text.split()

    if 'q' in my_list:
        j = my_list.index('q')
        while j < len(my_list):         # удаляем заначения после 'q'
            my_list.pop(j)
            exit = 1

    i = 0
    while i < len(my_list):
        my_list[i] = int(my_list[i])
        i += 1
    summa = summa + sum(my_list)
    print(summa)

    if exit == 1:
        break
