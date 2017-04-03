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

multiply([2,4,10,16], 5)

def layered_multiples(arr):
    for i in range(len(arr)):
        
    new_array = list(arr[i])
    print new_array


x = layered_multiples(multiply([2,4,5],3))
print x
