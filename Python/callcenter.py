class Call(object):
    def __init__(self, uniqueid, name, number, time, reason):
        self.uniqueid = uniqueid
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
        
    def display(self):
        print 'ID:', self.uniqueid, 'Name:', self.name, 'Phone Number:', self.number, 'Time of Call:', self.time, 'Reason For Call:', self.reason
        return self

caller1 = Call(1,'Jordan','(562)777-7777','1:30pm','bored')
caller2 = Call(2,'Tom','(562)333-3333','2:30pm','hungry')
caller3 = Call(3,'Jerry','(562)111-3333','12:30pm','none')
caller4 = Call(4,'Abigail','(562)222-3333','5:30pm','dunno')

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.size = len(self.calls)

    def add(self, call):
        self.calls.append(call)
        self.size += 1
        return self

    def remove(self):
        self.calls.remove(self.calls[0])
        self.size -= 1
        return self

    def info(self):
        print self.calls
        for phonecall in self.calls:
            print 'Name:', phonecall.name, 'Phone Number:', phonecall.number, 'Queue:', self.calls.index(phonecall)+1
        return self

c = CallCenter()


print c.add(caller1).add(caller2).add(caller3).add(caller4).info()
