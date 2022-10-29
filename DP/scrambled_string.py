'''
    SCRAMBLED STRING

    Tell if string a, b are scrambled strings
'''


def is_scrambled(a, b) -> bool:
    '''returns if a, b are srambled string'''
    if a == b:
        return True
    if len(a) != len(b):
        return False
    if len(a) <= 1:
        return False

    for i in range(1, len(a)):
        if is_scrambled(a[:i], b[:i]) and is_scrambled(a[i:], b[i:]):
            return True
        if is_scrambled(a[-i:], b[:i]) and is_scrambled(a[:-i], b[i:]):
            return True

    return False


print(is_scrambled("great", "eatgra"))
