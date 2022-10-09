'''
    PRINTING LONGEST SUBSEQUENCE

    Printing LCS
'''

def lcs(a, b):
    n = len(a)
    m = len(b)
    dp = [[0 for i in range(m + 1)] for i in range(n + 1)]
    seq = ""
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    curr = (n, m)
    while curr[0] > 0 and curr[1] > 0:
        if a[curr[0] - 1] == b[curr[1] - 1]:
            seq += a[curr[0] - 1]
            curr = (curr[0] - 1, curr[1] - 1)
        else:
            if dp[curr[0] - 1][curr[1]] > dp[curr[0]][curr[1] - 1]:
                curr = (curr[0] - 1, curr[1])
            else:
                curr = (curr[0], curr[1] - 1)
    return seq[::-1]

a = "abcd"
b = "abcdef"

print(lcs(a, b))
