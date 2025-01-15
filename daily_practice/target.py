def sum_unique_pairs(nums,target):
    pairs = set()
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    return list(pairs) 
result = sum_unique_pairs([1,2,3,4,5,6],7)
print(result)