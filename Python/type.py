def findType(var):
    if type(var) == int and var < 100:
        print "That's a small number"
    elif type(var) == int and var >= 100:
        print "That's a big number!"
    if type(var) == str and len(var) <= 50:
        print "Short sentence"
    elif type(var) == str and len(var) > 50:
        print "Long sentence"
    if type(var) == list and len(var) >= 10:
        print "Big list!"
    elif type(var) == list and len(var) < 10:
        print "Short list"

findType("hey there");
