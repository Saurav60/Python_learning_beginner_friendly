#Leet Code Problem Number 5 -- Longest Plaindromic Substring 
''Given a string s, return the longest palindromic substring in s.
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
  
Example 2:
Input: s = "cbbd"
Output: "bb"'''

#Solution: Using Expand around centre approach as brute force would be of O(n^3) time complexity
class Solution:
    def expand_around_center(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:  
            left -= 1  # Expand left
            right += 1  # Expand right
        return s[left + 1:right]  # Return the palindrome found

    def longestPalindrome(self, s: str) -> str:
        if not s: 
            return ""
        
        longest = ""
        for i in range(len(s)):
            odd_palindrome = self.expand_around_center(s, i, i)
            even_palindrome = self.expand_around_center(s, i, i + 1)
            longest = max(longest, odd_palindrome, even_palindrome, key=len)
        
        return longest

# Example usage:
solution = Solution()
print(solution.longestPalindrome("babad"))  # Output: "bab" or "aba"
print(solution.longestPalindrome("cbbd"))   # Output: "bb"
#Time complexity = O(n^2) and space complexity = O(1)
