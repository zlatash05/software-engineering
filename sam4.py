class Phone:
    def __init__(self, battery):
        self.__battery = battery
        self.type = "обычный телефон"

    def get_battery(self):
        return self.__battery

    def set_battery(self, new_battery):
        if 0 <= new_battery <= 100:
            self.__battery = new_battery
        else:
            print("Заряд должен быть от 0 до 100%")

    def get_type(self):
        return self.type

class Smartphone(Phone):
    def __init__(self, battery):
        super().__init__(battery)
        self.type = "смартфон"

my_phone = Phone(50)
my_smartphone = Smartphone(100)

print(my_phone.get_type())
print(my_smartphone.get_type())

print(my_phone.get_battery())
my_phone.set_battery(75)
print(my_phone.get_battery())
my_phone.set_battery(150)