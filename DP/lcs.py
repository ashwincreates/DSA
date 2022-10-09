'''
    LONGEST COMMON SUBSEQUENCE
'''

def longest_common_subsequence(a, b, i, j):
    if i == len(a) or j == len(b):
        return 0
    count = 0
    if a[i] == b[j]:
        count = 1 + longest_common_subsequence(a, b, i + 1, j + 1)
    else:
        count = max(longest_common_subsequence(a, b, i + 1, j), longest_common_subsequence(a, b, i, j + 1))
    return count

def longest_common_subsequence_iter(a, b):
    n = len(a)
    m = len(b)
    dp = [[0 for i in range(m + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]

a = "abcdef"
b = "abc"
print(longest_common_subsequence_iter(a, b))
