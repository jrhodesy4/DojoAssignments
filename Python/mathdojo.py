class MathDojo(object):
    def __init__(self):
        self.total = 0
    def add(self, *args):
        for num in args:
            if type(num) == int:
                self.total += num
            elif type(num) == float:
                self.total += num
            elif type(num) == list:
                self.total += sum(num)

        return self
    def subtract(self, *args):
        for num in args:
            if type(num) == int:
                self.total -= num
            elif type(num) == float:
                self.total += num
            elif type(num) == list:
                self.total -= sum(num)
        return self
        
    def result(self):
        print self.total
        return self


print MathDojo().add(2).add(2, 5).subtract(3, 2).result()

print MathDojo().add([1],3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2,[2,3],[1.1,2.3]).result()
