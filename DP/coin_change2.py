'''
    COIN CHANGE II
'''


import sys
input = sys.stdin.readline


def coin_change(coins, _sum, i):
    if _sum == 0:
        return 0
    if _sum < 0 or i == len(coins):
        return 1e9
    _min = 1e9
    if coins[i] <= _sum:
        _min = min(
            1 + coin_change(coins, _sum - coins[i], i),
            coin_change(coins, _sum, i + 1)
        )
    else:
        _min = coin_change(coins, _sum, i + 1)
    return _min


def coin_change_iter(coins, _sum):
    n = len(coins)
    m = _sum
    dp = [[int(1e9) for i in range(m + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if coins[i - 1] <= j:
                dp[i][j] = min(1 + dp[i][j - coins[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][m]


n, _sum = list(map(int, input().split(" ")))
coins = list(map(int, input().split()))
print(coin_change_iter(coins, _sum))
