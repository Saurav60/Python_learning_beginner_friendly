def reverse_string_without_builtin(s):
    reversed_string = ''
    for char in s:
        reversed_string= char + reversed_string
    return reversed_string
s= 'mahesh'
result = reverse_string_without_builtin(s)
print(result)