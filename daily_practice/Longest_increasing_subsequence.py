#leetcode question solved today:
#300. Longest Increasing Subsequence
''Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?'''

# Solution 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binary_search(lis, target):   
            low, high = 0, len(lis) - 1
            while low <= high:
                mid = (low + high) // 2
                if lis[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low  # The position to replace or append
            
        lis = [] #create an list to store longest increasing subsequence
        for num in nums:
            pos = binary_search(lis, num)  # Find the position for the current number using binary search function written above 
            if pos < len(lis):
                lis[pos] = num  # Replace the element at the found position
            else:
                lis.append(num)  # Append the current number if it extends the LIS
        return len(lis)
   
