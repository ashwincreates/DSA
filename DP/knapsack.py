'''
    KNAPSACK
    Finding Maximum Profit
'''

weight = [1, 3, 4, 5]
value = [1, 4, 5, 7]
total_weight = 7
m = {}


def knapsack(weight, value, total_weight, n, m):
    if n == 0 or total_weight == 0:
        return 0
    if total_weight in m:
        return m[total_weight]
    max_profit = 0
    if weight[n] <= total_weight:
        max_profit = max(value[n] + knapsack(weight, value, total_weight - weight[n], n - 1, m), knapsack(weight, value, total_weight, n - 1, m))
    else:
        max_profit = knapsack(weight, value, total_weight, n - 1, m)
    m[total_weight] = max_profit
    return m[total_weight]


def knapsack_iter(weight, value, total_weight):
    n = len(weight)
    m = total_weight
    dp = [[0 for i in range(m + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if weight[i - 1] <= j:
                dp[i][j] = max(value[i - 1] + dp[i - 1][j - weight[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][m]


print(knapsack_iter(weight, value, total_weight))
