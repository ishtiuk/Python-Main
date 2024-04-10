class SmartDevice:
    type = 'Smart'

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def electric(self):
        print('We eat electrons')
        print('They are yummy')


class SmartWatch(SmartDevice):
    def __init__(self, brand, price, gps, steps_count):
        # super().__init__(brand, price)
        SmartDevice.__init__(self, brand, price)
        self.gps = gps
        self.step_count = steps_count


my_watch = SmartWatch('FitBit', 810, True, 0)
print(my_watch.brand)
print(my_watch.price)
print(my_watch.gps)
print(my_watch.step_count)