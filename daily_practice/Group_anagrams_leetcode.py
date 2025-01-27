#Q-49. Group Anagrams
'''Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]'''

#Solution
#Best approach using defaultdict with minimum time complexity: O(n⋅klogk)  where where n is the number of strings and k is the average length of the strings.
#space complexity is 𝑂(𝑛⋅𝑘)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)             #so that empty list gets in values for key having no values
        for string in strs:
            sorted_str = ''.join(sorted(string))
            anagrams[sorted_str].append(string)
        return list(anagrams.values())
