def remove_tuples(arr, value):
    new_arr = arr.copy()
    new_arr.reverse()
    for i in new_arr:
        if (has_elememt(i, value)):
            arr.remove(i)
        
def has_elememt(tup,value):
    for i in tup:
        if (i == value):
            return True
    return False

arr = [(1, 2), (1, 3), (2, 3), (2, 4)]
remove_tuples(arr, 2)
print(arr)