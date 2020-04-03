def list_to_dict(arr):
    map = {}
    for i in range(0, len(arr),2):
        map[arr[i]] = arr[i+1]
    return map
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
print(list_to_dict(arr))