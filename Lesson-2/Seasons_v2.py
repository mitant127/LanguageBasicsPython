# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.


my_dict = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'Summer',
           7: 'Summer', 8: 'Summer', 9: 'Autumn', 10: 'Autumn', 11: 'Autumn', 12: 'winter'}

while True:
    print("Введите номер месяца от 1 до 12")
    month = int(input(" - "))
    if month > 12:
        print("Вы ввели слишком большое число.")
    elif month < 1:
        print("Вы ввели слишком маленькое  число.")
    else:
        break

print(my_dict.get(month))
