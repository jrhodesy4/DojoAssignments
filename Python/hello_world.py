str = "It's thanksgiving day. It's my birthday,too!"
words = str.split(' ')
print words.index('day.')
print str.replace('day','month')

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[(len(x)-1)]
newArr = [x[0],x[(len(x)-1)]]
print newArr

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x = sorted(x)
one = x[0:5]
two = x[5:11]
print one
print two
two.insert(0, x[0:5])
print two
