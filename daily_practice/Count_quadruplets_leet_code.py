'''Leet code problem number 1995:
Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:
nums[a] + nums[b] + nums[c] == nums[d], and
a < b < c < d
Example 1:
Input: nums = [1,2,3,6]
Output: 1
Explanation: The only quadruplet that satisfies the requirement is (0, 1, 2, 3) because 1 + 2 + 3 == 6.'''

#Solution:

from collections import defaultdict
from typing import List

def countQuadruplets(self, nums: List[int]) -> int:
    n = len(nums)
    quad_count = 0
    sum_pair = defaultdict(list)
    
    # Precompute sums of pairs (a, b) where a < b
    for a in range(n):
        for b in range(a + 1, n):
            sum_pair[nums[a] + nums[b]].append((a, b))
    
    # Check for valid quadruplets (a, b, c, d) where a < b < c < d
    for c in range(2, n):  # c starts from 2 because a < b < c
        for d in range(c + 1, n):
            target = nums[d] - nums[c]  # nums[a] + nums[b] = nums[d] - nums[c]
            if target in sum_pair:
                for a, b in sum_pair[target]:
                    if b < c:  # Ensure a < b < c < d
                        quad_count += 1
    return quad_count
#most optimized way
#Time complexity O(n)^2 and space complexity is O(n)^2 also. 
