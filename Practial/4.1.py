def merge_dicts(d1, d2):
    newDict = {}
    for i in d1:
        newDict[i] = d1[i]
    for i in d2:
        newDict[i] = d2[i]
    
    return newDict

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 5, 'd': 6}

print("Merged Dictionary:", merge_dicts(d1, d2))
