# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.


string = input("Введите строку: ")
str = string.split()
i = 0
while i < len(str):
    s = str[i]
    print(f"{i + 1} {s[:10]}")
    i += 1
