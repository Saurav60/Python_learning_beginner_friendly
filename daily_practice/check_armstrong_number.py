"""
Check if a number is an Armstrong number.
"""
def is_armstrong(n):
    digits = [int(x) for x in str(n)]
    return n == sum(d**len(digits) for d in digits)
#Example
print(is_armstrong(153))
