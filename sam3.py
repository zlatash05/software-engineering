class Phone:
    def __init__(self, battery):
        self.battery = battery
        self.type = "обычный телефон"

    def get_battery(self):
        return self.battery

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