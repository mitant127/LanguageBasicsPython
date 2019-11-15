# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

f_inp = open('file1-2.txt')
counter = {}

i = 0
for line in f_inp:
    i += 1
    counter[i] = len(line.split())

print(counter)
f_inp.close()


