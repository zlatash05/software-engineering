class Phone:
    def __init__(self, battery):
        self.battery = battery

    def get_battery(self):
        return self.battery

my_phone = Phone(80)
print(my_phone.get_battery())