# 1. Создать программно файл в текстовом формате, записать в него построчно
# данные, вводимые пользователем. Об окончании ввода данных свидетельствует
# пустая строка.

out_f = open("file1-2.txt", 'w')

while True:
    data = input("Enter data: ")
    if data == '':
        break
    else:
        out_f.write(data + '\n')
out_f.close()

# создаваемый файл используется в следующем (2-м) задании для подсчета строк и слов