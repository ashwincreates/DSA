'''
    Greatest Common Divisor

    gcd in logarthmic complexity
'''

def gcd(_a, _b):
    """returns greates common divisor."""
    if _b == 0:
        return _a
    return gcd(_b, _a%_b)

print(gcd(1,4))
