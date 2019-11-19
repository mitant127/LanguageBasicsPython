# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие
# атрибуты: speed, color, name, is_police (булево).  А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
# WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который
# должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ
# к атрибутам, выведите результат. Выполните вызов методов и также покажите
# результат.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print("Car go")

    def stop(self):
        self.speed = 0
        print("Car stop")

    def turn(self):
        print("Car turn")


    def show_speed(self):
        print(f"Speed - {self.speed}")


class TownCar(Car):
    def __init__(self, speed):
        super().__init__(speed, "Yellow", "TownCar", False)

    def show_speed(self):
        if self.speed > 60:
            print("Over speed")
        else:
            print(f"Speed - {self.speed}")


class SportCar(Car):
    def __init__(self, speed):
        super().__init__(speed, "Red", "SportCar", False)


class WorkCar(Car):
    def __init__(self, speed):
        super().__init__(speed, "White", "WorkCar", False)

    def show_speed(self):
        if self.speed > 40:
            print("Over speed")
        else:
            print(f"Speed - {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed):
        super().__init__(speed, "black and white", "police", True)


car_0 = Car(40, "Green", "Car", False)
car_0.go()
print(f"car_0: {car_0.name}, {car_0.is_police}, {car_0.color}")
car_0.show_speed()

car_1 = PoliceCar(100)
car_1.turn()
print(f"car_1: {car_1.name}, {car_1.is_police}, {car_1.color}")
car_1.show_speed()

car_2 = WorkCar(45)
car_1.turn = "left"
car_2.turn()
print(f"car_2: {car_2.name}, {car_2.is_police}, {car_2.color}")
car_2.show_speed()

car_3 = SportCar(80)
print(f"car_3: {car_3.name}, {car_3.is_police}, {car_3.color}")
car_3.show_speed()

car_4 = TownCar(50)
car_4.stop()
print(f"car_4: {car_4.name}, {car_4.is_police}, {car_4.color}")
car_4.show_speed()
