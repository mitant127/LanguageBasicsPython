# 3. Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов. Определить, кто из сотрудников имеет
# оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.

my_list = []

with open('file3.txt') as f_inp:
    i = 0
    n = 0
    for line in f_inp:
        i += 1
        n += int(line.split(" ")[1])
        if int(line.split()[1]) < 20000:
            my_list.append(line.split()[0])
print(f"Список сотрудников с зарплатой меньше 20000: {', '.join(my_list)}")
print(f"Средняя доход сотрудников {n/i:.2f}")