def count_palindrome(array):
    count = 0
    for i in array:
        if (is_palindrome(i)):
            count = count + 1
    return count

def is_palindrome(str):
    for i in range(0, len(str)):
        if (str[i] != str[len(str) - i - 1]):
            return False
    return True

sample = ['abdefc', 'xygyz', 'abeba', '123321']
print(count_palindrome(sample))