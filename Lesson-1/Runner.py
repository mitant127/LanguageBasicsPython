# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.


a = int(input("Введите результат первого дня "))
b = int(input("Введите цель "))

i = 0
while b > a:
    a = a * 1.1
    i += 1
print(f"Вы достигнете вашей цели на {i + 1} день")
