def pattern_match(pattern, string):
    words = string.split()
    if len(pattern) != len(words):
        return False
    
    pattern_to_words = {}
    words_to_pattern = {}

    for p,w in zip(pattern, words):
        if p in pattern_to_words:
            if pattern_to_words[p] != w:
                return False
        else:
            pattern_to_words[p] = w
        
        if w in words_to_pattern:
            if words_to_pattern[w] != p:
                return False
            else:
                words_to_pattern[w] = w
    return True 

pattern1 = "abba"
string1 = "dog cat cat dog"
pattern2 = "aba"
string2 = "dog dog cat"

print(pattern_match(pattern1, string1))
print(pattern_match(pattern2, string2))
