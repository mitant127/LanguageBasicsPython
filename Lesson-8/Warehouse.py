# 4. Начните работу над проектом «Склад оргтехники». Создайте класс,
# описывающий склад. А также класс «Оргтехника», который будет базовым
# для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.


class Warehouse:
    def __init__(self, pieces, warehous):
        # self.pieces = pieces
        self.warehous = {'warehous': {warehous}, 'pieces': pieces}

    def warh_in(self):
        pass

    def warh_out(self):
        pass

class OfficeMachines:

    def __init__(self, supply_voltage):
        self.supply_voltage = supply_voltage


class Printer(OfficeMachines):
    def __init__(self, supply_voltage, color):
        super().__init__(supply_voltage)
        self.color = color


class Computer(OfficeMachines):
    def __init__(self, supply_voltage, ram):
        super().__init__(supply_voltage)
        self.RAM = ram


class Monitir(OfficeMachines):
    def __init__(self, supply_voltage, screen_resolution):
        super().__init__(supply_voltage)
        self.screen_resolution = screen_resolution


comp = Computer(220, "2Gb")
comp_warh = Warehouse(25, comp)
print(f"{comp_warh.warehous}")
