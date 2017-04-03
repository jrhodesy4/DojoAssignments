def typeList(list):
    total = 0
    string = 0
    i = 0
    if (all(isinstance(i, int) for i in list)):
        print "The array you entered is of integer type"
    elif (all(isinstance(i, str) for i in list)):
        print "The array you entered is of string type"
    else:
        print "The array you entered is of mixed type"
    # if (isinstance(i, str) for i in list):
    #     string += i
    #     print string
    for i in list:
        if type(i) is str:
            print "String:" + " " + i
    # if (isinstance(i,int) for i in list):
    #     total += i
    #     total = sum(total)
    #     print total
    for i in list:
        if type(i) is int:
            total += i
    print "Sum:" + " " + str(total)


typeList([3,2,'hello',33,22]);
