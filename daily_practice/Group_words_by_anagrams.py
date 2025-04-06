"""
Group a list of words into anagrams.
"""
from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)
    return list(groups.values())

print(group_anagrams(["bat", "tab", "tap", "pat", "cat"]))
