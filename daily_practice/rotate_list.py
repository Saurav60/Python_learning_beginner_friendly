"""
Rotate a list to the right by k steps.
"""
def rotate_list(lst, k):
    k %= len(lst)
    return lst[-k:] + lst[:-k]
#Example
print(rotate_list([1, 2, 3, 4, 5], 2))
