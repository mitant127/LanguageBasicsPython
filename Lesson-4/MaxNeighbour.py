# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.


my_list = [4, 32, 98, 12, 11, 56, 73, 22]
new_list = [el for el in my_list if my_list.index(el) < (len(my_list)) if my_list[my_list.index(el)] > my_list[my_list.index(el) - 1]]
# new_list = [el for el in my_list ]

print(new_list)
