#Problem statement
#You are climbing a staircase. It takes n steps to reach the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps'''

#Solution
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n 
        first = 1 #way to climb one step 
        second = 2 #way to climb second step

        for i in range(3, n+1):
            current = first + second
            first = second 
            second = current
        return second 
