def flatten_dict(d):
    flat = {}
    for i in d:
        if type(d[i]) is dict:
            for inner_i in d[i]:
                flat[(i, inner_i)] = d[i][inner_i]
        else:
            flat[(i,)] = d[i]
    return flat

dict = {'a': 1, 'b': {'x': 10, 'y': 20}}
print("Flattened Dictionary:", flatten_dict(dict))
