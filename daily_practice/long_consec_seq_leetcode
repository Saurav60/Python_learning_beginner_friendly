def longest_consecutive_sequence(nums):
    if not nums:
        return []
    unique_nums = sorted(set(nums))

    longest_streak = []
    current_streak = [unique_nums[0]]

    for i in range(1,len(unique_nums)):
        if unique_nums[i] == unique_nums[i-1] + 1:
            current_streak.append(unique_nums[i])
        else:
            if len(current_streak) > len(longest_streak):
                longest_streak = current_streak 
            current_streak = [unique_nums[i]]
    if len(current_streak) > len(longest_streak):
        longest_streak = current_streak 
    return longest_streak 

nums = [1,2,5,6,7,8,3,4,9,10,12,11]
result = longest_consecutive_sequence(nums)
print(result)
