def draw_stars(list):
    for i in list:
        if type(i) is int:
            i = '*' * i
            print i
        if type(i) is str:
            i = i[0].lower() * len(i)
            print i

draw_stars([4,'Tom',1,'Michael',5,7,'Jimmy Smith'])
