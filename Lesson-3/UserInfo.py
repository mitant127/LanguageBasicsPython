# 2. Реализовать функцию, принимающую несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания, email,
# телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_info(name, surname, yearofbirth, cityofresidence, email, phone):
    userinfo['Name'] = name
    userinfo['Surname'] = surname
    userinfo['Year of birth'] = yearofbirth
    userinfo['City of residence'] = cityofresidence
    userinfo['email'] = email
    userinfo['Phone'] = phone


userinfo = {'Name': '', 'Surname': '', 'Year of birth': '', 'City of residence': '', 'email': '', 'Phone': ''}


name = input("Enter user name: ")
surname = input("Enter user surname: ")
yearofbirth = input("Enter user year of birth: ")
cityofresidence = input("Enter user city of residence: ")
email = input("Enter user email: ")
phone = input("Enter user phone: ")

user_info(name=name, surname=surname, yearofbirth=yearofbirth, cityofresidence=cityofresidence, email=email, phone=phone)

for x in userinfo: print(f"{x} - {userinfo.get(x)}")
