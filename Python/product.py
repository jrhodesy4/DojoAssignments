class Product(object):
    def __init__(self, price, name, weight, brand, cost, status):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status
    def sell(self):
        self.status = 'sold'
        print self.status
        return self
    def addTax(self,tax):
        self.price = self.price + tax
        print self.price
    def Return(self, reason):
        if reason == 'defective':
            self.status = 'defective'
            self.price = 0
            print 'Status:', self.status
        if reason == 'like new':
            self.status = 'for sale'
            print self.status
        if reason == 'opened':
            self.status = 'used'
            self.price = self.price - self.price * 0.2
            print self.price
    def displayinfo(self):
        print 'Price:', self.price, 'Name:', self.name, 'Weight:', self.weight, 'Brand:', self.brand, 'Cost:', self.cost, 'Status:', self.status
        return self

product1 = Product(20, 'Cereal', '2 lbs', 'Fruit Loops', 15, 'For Sale')

print product1.displayinfo().sell().displayinfo()
print product1.addTax(.25)
print product1.displayinfo()
print product1.Return('opened')
print product1.displayinfo()
