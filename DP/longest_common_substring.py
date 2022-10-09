'''
    LONGEST COMMON SUBSTRING
'''

def longest_common_substring(a, b, i, j):
    if i == len(a) or j == len(b):
        return 0
    count = 0
    if a[i] == b[j]:
        count = 1 + longest_common_substring(a, b, i + 1, j + 1)
    else:
        count = 0 
    return count

print(longest_common_substring("abcfvdef", "def", 0, 0))