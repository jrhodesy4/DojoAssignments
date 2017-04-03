def characterList(list, char):
    list2 = []
    letters = str(char)
    for word in list:
        if word.find(letters) != -1:
            list2.append(word)
    print list2;

characterList(['hey','there','friend'], 'h')
