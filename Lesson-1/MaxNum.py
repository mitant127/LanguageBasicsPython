# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


number = str(input("Введите число "))
maximum = 0

i = 0
while i < len(number):
    num = int(number[i])
    if num > maximum:
        maximum = num
    i += 1
print(maximum)
