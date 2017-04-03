#Part 1 this for loop runs through 1 to 1000 and prints all the numbers
for count in range(1, 1001):
    print count

#Part 2 his for loop runs through 5 to 1000000 and prints all multiples of 5
for count in range(5, 1000001):
    if count % 5 == 0:
        print count

#Sum list- this program takes the sum of all the numbers in the list
a =[1, 2, 5, 10, 255, 3]
b = sum(a)
print b

#AvgList -this program first finds the sum of the list, then divides it by the number of values in the list, thus finding the average
a = [1, 2, 5, 10, 255, 3]
b = sum(a)
c = b/len(a)
print c
