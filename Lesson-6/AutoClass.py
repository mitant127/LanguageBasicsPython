# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут
# color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав
# экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его
# нарушении выводить соответствующее сообщение и завершать скрипт.

# from time import sleep
import time


class TrafficLight:
    __color = "Red"

    def running(self):
        while True:
            color_list = ('red', 'yellou', 'green')
            for i in color_list:
                _TrafficLight_color = i
                if _TrafficLight_color == 'red':
                    print(('\x1b[7;31;41m' + i + '\x1b[0m'))
                    time.sleep(7)
                elif _TrafficLight_color == 'yellou':
                    print(('\x1b[7;33;43m' + i + '\x1b[0m'))
                    time.sleep(2)
                elif _TrafficLight_color == 'green':
                    print(('\x1b[7;32;42m' + i + '\x1b[0m'))
                    time.sleep(7)


e = TrafficLight()
print(e.running())
