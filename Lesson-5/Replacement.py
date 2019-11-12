# -*- coding: utf-8 -*-
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться на
# русские. Новый блок строк должен записываться в новый текстовый файл.

with open('file4.txt', encoding='utf-8') as f_inp:
    with open('file4a.txt', 'w', encoding='utf-8') as f_out:
        data = f_inp.read()
        data = data.replace("One", "Один")
        data = data.replace("Two", "Два")
        data = data.replace("Three", "Три")
        data = data.replace("Four", "Четыре")
        f_out.write(data)

