# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к
# какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.


list = ['winter', 'spring', 'Summer', 'Autumn']

while True:
    print("Введите номер месяца от 1 до 12")
    month = input(" - ")

    if month.isalpha():
        print("Вы ввели не число")
    else:
        month = int(month)
        if month < 1:
            print("Вы ввели слишком маленькое число.")
        elif month > 12:
            print("Вы ввели слишком большое число.")
        else:
            break

if month == 12:
    print(list[0])
elif month < 3:
    print(list[0])
elif month < 6:
    print(list[1])
elif month < 9:
    print(list[2])
else:
    print(list[3])
