import random
def coinToss(number):
    recordList, heads, tails = [], 0, 0
    for i in range(5000):
         flip = random.randint(0, 1)
         if (flip == 0):
             heads += 1
             print 'Attempt#' + str(i+1) + " " + "Heads=" + str(heads) + " " + "and Tails=" + str(tails)

         else:
             tails += 1
             print 'Attempt#' + str(i+1) + " " + "Tails=" + str(tails) + " " + "and Heads=" + str(heads)

coinToss(5000)
