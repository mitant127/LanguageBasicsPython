#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и
# секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.


usertime = int(input("Введите время в секундах:"))

seconds = usertime % 60
minutes = usertime // 60 % 60
hours = usertime // 60 // 60

print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
