# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год». В рамках класса реализовать два
# метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором
# @staticmethod, должен проводить валидацию числа, месяца и года (например,
# месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def data_string(cls, data_str):
        day, month, year = map(int, data_str.split("-"))
        return f"{day} - {month} - {year}"

    @staticmethod
    def valid_data(data_str):
        day, month, year = map(int, data_str.split("-"))
        if day > 31 or month > 12:
            return f"Error enter data"
        return f"Data correct"


data_1 = Data.data_string("29-09-2019")
print(data_1)
print(Data.valid_data(Data.data_string("29-09-2019")))

data_2 = Data.data_string("45-09-2019")
print(data_2)
print(Data.valid_data(Data.data_string("45-09-2019")))

data_3 = Data.data_string("19-13-2019")
print(data_3)
print(Data.valid_data(Data.data_string("19-13-2019")))

data_4 = Data.data_string("19-10-3594")
print(data_4)
print(Data.valid_data(Data.data_string("19-10-3594")))
