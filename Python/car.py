class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.max_speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    def display_all(self):
        print 'Price:', self.price, 'Speed:', self.max_speed, 'Fuel:', self.fuel, 'Mileage:', self.mileage, 'Tax:', self.tax
        return self

car1 = Car(20000, '400mph', 'Full', '15mpg')
car2 = Car(10000, '400mph', 'Not Full', '2mpg')
car3 = Car(2000, '10mph', 'Not Full', '45mpg')
car4 = Car(1234, '123mph', 'Full', '5mpg')
car5 = Car(100000, '200mph', 'Full', '23mpg')
car6 = Car(1, '333mph', 'Not Full', '11mpg')

print car1.display_all()
print car2.display_all()
print car3.display_all()
print car4.display_all()
print car5.display_all()
print car6.display_all()
