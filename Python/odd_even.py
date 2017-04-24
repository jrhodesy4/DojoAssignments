def odd_even():
    for i in range(1,2001):
        if i % 2 == 0:
            print "Number is" + " " + str(i)
            print "This is an even number"
        else:
            print "Number is" + " " + str(i)
            print "This is an odd number"

odd_even()

def multiply(arr,b):
    for i in range(len(arr)):
        arr[i] *= b
    print arr
    return arr

multiply([2,4,10,16],5)

def layered_multiples(arr):
    newList = []
    for i in range(len(arr)):
        arr[i] = '1' * arr[i]
        newList.append([arr[i]])
    print newList

layered_multiples(multiply([2,4,5],3))
# print x


# more than one for loop
# make a new list everytime you go through the for loop
