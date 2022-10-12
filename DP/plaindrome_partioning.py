'''
    Palindrome Partioning
    Minimum palindromes by breaking a palindrome
'''


def is_palindrome(s):
    '''Return is given string is palindrome or not'''
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def palindrome(s: str, i: int, j: int, m={}):
    '''Returns min palindrome obtainable by partioning.'''
    if i > j:
        return 0
    if (i, j) in m:
        return m[(i, j)]
    if is_palindrome(s[i:j]):
        return 0

    _min = 1e9
    for k in range(i, j):
        temp = palindrome(s, i, k) + palindrome(s, k + 1, j) + 1
        _min = min(temp, _min)
        m[(i, j)] = _min

    return _min


s = "reabaeaba"
print(palindrome(s, 0, len(s) - 1))
