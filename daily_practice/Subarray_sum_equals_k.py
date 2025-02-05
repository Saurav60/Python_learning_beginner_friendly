#Today I solved Leet code Problem number 560 : Subarray sum equals k
'''Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2'''

#Solution: Brute force 
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):  # Start of subarray
            total = 0
            for j in range(i, len(nums)):  # End of subarray
                total += nums[j]
                if total == k:
                    count += 1
        return count
#Time complexity = O(n^2) , Space Complexity = O(1)

#Solution: optimized it to reduce time complexity 
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        sum_freq = defaultdict(int)  # Hash map to store prefix sum frequency
        sum_freq[0] = 1  # Initialize with 0 to handle cases where prefix_sum itself is k

        for num in nums:
            prefix_sum += num  # Update running sum
            
            if (prefix_sum - k) in sum_freq:  # Check if (prefix_sum - k) exists
                count += sum_freq[prefix_sum - k]  # Add occurrences of (prefix_sum - k)

            sum_freq[prefix_sum] += 1  # Store the prefix sum in the hashmap

        return count
#Now Time complexity = O(n) and space complexity = O(n) since we used hashmap 
