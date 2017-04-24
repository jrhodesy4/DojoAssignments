import random
def randomScores(nums):
    nums = random.sample(xrange(60,100), 10)
    print nums
    for i in nums:
        if i > 89:
            print "Score:" + str(i), "Your grade is A"
        elif i > 79:
            print "Score:" + str(i), "Your grade is B"
        elif i > 69:
            print "Score:" + str(i), "Your grade is C"
        else:
            print "Score:" + str(i), "Your grade is D"

randomScores("x")
