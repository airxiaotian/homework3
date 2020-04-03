def sort_tuple_list(list):
    list.sort(key=get_first)
    return list

def get_first(e):
    return e[0]

arr = [(1, 2), (1, 3), (2, 3), (3, 4)]
print(sort_tuple_list(arr))