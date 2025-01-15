def create_palindrome(n):
    if n <= 0:
        return ''
    alphabet = 'abcdefghijklmnop'
    if n > len(alphabet):
        raise ValueError('n is more than alphbets size')
    
    half = alphabet[:n]
    palindrome = half + half[:-1][::-1]
    return palindrome 
result = create_palindrome(5)
print(result)