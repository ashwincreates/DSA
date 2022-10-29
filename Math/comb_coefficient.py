'''Combinations.'''


def binomial_coefficient(n, k) -> int:
    '''
    returns binomial coefficient of x ^ k in the expansion of (1 + x)^k.

    Optimal Substructure
    C(n, k) = C(n - 1, k - 1) + C(n - 1, k)
    C(n, 0) = C(n, n) = 1

    This also prints the PASCALS's TRIANGLE
    '''
    dp = [[0 for i in range(k + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(k + 1):
            if j in (i, 0):
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    return dp[n][k]
