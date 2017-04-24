class Bike(object):
    def __init__(self, price, speed, miles):
        self.price = price
        self.max_speed = speed
        self.miles = miles
    def displayinfo(self):
        print 'Price:', self.price, 'Speed:', self.max_speed, 'Miles:', self.miles
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing"
        if self.miles > 4:
            self.miles -= 5
        return self

bike1 = Bike(200, '25mph', 20)
bike2 = Bike(150, '20mph', 15)
bike3 = Bike(100, '15mph', 30)

print bike1.ride().ride().ride().reverse().displayinfo()
print bike2.ride().ride().displayinfo()
print bike3.reverse().reverse().reverse().displayinfo()
