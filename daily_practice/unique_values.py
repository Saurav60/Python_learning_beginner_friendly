list1 = [1,2,3,2,4,4,5,5,6,6,7,8,9,9,9]
frequency = {}

for num in list1:
    if num in frequency:
        frequency[num] += 1 
    else:
        frequency[num] = 1

for num, count in frequency.items():
    if count > 1:
        print(num,count)
