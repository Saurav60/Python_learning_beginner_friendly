#Write a Python function to find a list's longest consecutive sequence of unique numbers.
def longest_consecutive_sequence(nums):
    if not nums:
        return []
    nums_set = set(nums)
    longest_sequence = []
    
    for num in nums_set:
        if num-1 not in nums_set:
            current_num = num
            current_sequence = [num]
            while num + 1 in nums_set:
                current_num += 1
                current_sequence.append(current_num)

            if len(current_sequence) > len(longest_sequence)
            longest_sequence = current_sequence
    return longest_sequence 


# Example usage
nums = [100, 4, 200, 1, 3, 2, 2, 101]
result = longest_consecutive_sequence(nums)
print(f"Longest consecutive sequence: {result}")
output
Longest consecutive sequence: [1, 2, 3, 4]







