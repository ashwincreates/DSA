'''
    COIN CHANGE I
'''


def coin_change_recursive(coins, i, remaining):
    if remaining == 0:
        return 1
    if i == len(coins) or remaining < 0:
        return 0
    count = 0
    if coins[i] <= remaining:
        count = coin_change_recursive(coins, i, remaining - coins[i]) + coin_change_recursive(coins, i + 1, remaining)
    else:
        count = coin_change_recursive(coins, i + 1, remaining)
    return count


def coin_change(coins, _sum):
    n = len(coins)
    m = _sum
    dp = [[0 for i in range(m + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if coins[i - 1] <= j:
                dp[i][j] = dp[i][j - coins[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][m]


coins = [1, 2, 3]
_sum = 5
print(coin_change(coins, 5))
