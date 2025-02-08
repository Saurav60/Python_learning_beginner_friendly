# Leet code problem number 53
'''Given an integer array nums, find the subarray with the largest sum, and return its sum.
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.'''

#Solution:
#Brute force solution with Time complexity =O(n^2) 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')  # Handle negative values correctly
        n = len(nums)
        for i in range(n):
            curr_sum = 0  # Running sum for subarrays starting at index i
            for j in range(i, n):
                curr_sum += nums[j]  # Add the new element instead of recalculating sum
                max_sum = max(max_sum, curr_sum)  # Update max_sum
        return max_sum
# Most optimized solution with Time complexity = O(n) using Kadane’s Algorithm: which is a dynamic programming technique used to find the maximum sum of a contiguous subarray in an array in O(n) time.
'''It is useful when:
We need to find the maximum subarray sum efficiently.
The input array has both positive and negative numbers.
Brute-force solutions (O(N²) or O(N³)) are too slow and give TLE for large inputs.'''

#Solution 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')  # Maximum sum found so far
        curr_sum = 0  # Current subarray sum
        for num in nums:
            curr_sum = max(num, curr_sum + num)  # Extend or restart subarray
            max_sum = max(max_sum, curr_sum)  # Update global max sum
        return max_sum

