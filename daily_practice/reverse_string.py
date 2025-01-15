def reverse_string(s):
    list1= s.split()
    reversed_list = list1[::-1]
    str1 = ' '.join(reversed_list)
    return str1

s = 'saurav is learning'
result = reverse_string(s)
print(result)