class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        print self.health
        return self
        
    def displayHealth(self):
        print 'Name:', self.name, 'Health:', self.health
        return self

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
        print self

    def fly(self):
        self.health -= 10
        return self

d1 = Dog('Dog')
d2 = Dragon('Puff')
print d1.run()
print d2.walk().fly().displayHealth()
