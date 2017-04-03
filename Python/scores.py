def scores(num):
    import random
    # num = random.randint()
    if num > 89:
        print "Score:" + str(num), "Your grade is A"
    elif num > 79:
        print "Score:" + str(num), "Your grade is B"
    elif num > 69:
        print "Score:" + str(num), "Your grade is C"
    else:
        print "Score:" + str(num), "Your grade is D"

scores(50)

import random
num = random.randint()
print num
