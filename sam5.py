class Phone:
    def __init__(self, battery):
        self.__battery = battery

    def get_battery(self):
        return self.__battery

    def set_battery(self, new_battery):
        if 0 <= new_battery <= 100:
            self.__battery = new_battery
        else:
            print("Заряд должен быть от 0 до 100%")

    def make_sound(self):
        return "звонит"


class Smartphone(Phone):
    def __init__(self, battery):
        super().__init__(battery)

    def make_sound(self):
        return "играет мелодия"


class Tablet(Phone):
    def __init__(self, battery):
        super().__init__(battery)

    def make_sound(self):
        return "издает звуковой сигнал"


devices = [Phone(50), Smartphone(100), Tablet(80)]

for device in devices:
    print(device.make_sound())
    