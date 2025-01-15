arr = [10,9,2,1]
full_array = list(range(min(arr),max(arr)+1))
#using set operations to find missing numbers 
missing_numbers = set(full_array) - set(arr)
result = sorted(missing_numbers)
print(result)