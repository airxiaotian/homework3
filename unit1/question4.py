def find_longest_word(arr):
    longest_word = ''
    for i in arr:
        if (len(i) > len(longest_word)):
            longest_word = i
    return longest_word

arr = ['a', 'apple', 'bb', 'boy']
print(find_longest_word(arr))