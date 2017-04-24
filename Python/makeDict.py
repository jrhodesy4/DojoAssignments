def make_dict(arr1, arr2):
    if len(arr1) > len(arr2):
        arr3 = zip(arr1,arr2)
    if len(arr2) > len(arr1):
        arr3 = zip(arr2,arr1)
        newDict = dict(arr3)
        print newDict

make_dict(['anna', 'eli', 'pariece'],['horse', 'cat', 'spider', 'dog'])
