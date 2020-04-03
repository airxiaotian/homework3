def combine_dict(dict1, dict2):
    dict3 = {}
    for k in dict1.keys():
        dict3[k] = dict1.get(k)
    for k in dict2.keys():
        dict3[k] = dict3.get(k, 0) + dict2.get(k)
    return dict3

dict1 = {1: 1, 2: 2, 3: 3}
dict2 = {1: 1, 3: 3, 5: 5}
print(combine_dict(dict1,dict2))