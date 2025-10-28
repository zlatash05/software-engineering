class Phone:
    def __init__(self, battery, brand):
        self.battery = battery
        self.brand = brand

    def get_battery(self):
        return self.battery

    def get_brand(self):
        return self.brand

my_phone = Phone(80, "Samsung")
print(my_phone.get_battery())
print(my_phone.get_brand())