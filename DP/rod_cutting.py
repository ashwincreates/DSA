'''
    ROD CUTTING PROBLEM
    
    Unbounded Knapsack Variation
'''

def rod_cutting(length, prices, i, total):
    if total <= 0 or i == len(length):
        return 0
    _max = 1e9
    if length[i] <= total:
        _max = max(prices[i] + rod_cutting(length, prices, i, total - length[i]), rod_cutting(length, prices, i + 1, total))
    else:
        _max = rod_cutting(length, prices, i + 1, total)     
    return _max

def rod_cutting(length, prices, total):
    n = len(length)
    m = total 
    dp = [[1e9 for i in range(m + 1)] for i in range(n + 1)]
    for i in range(m + 1):
        dp[0][i] = 0
    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if length[i - 1] <= j: 
                dp[i][j] = max(prices[i - 1] + dp[i][j - length[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][m]
length = [1, 2, 3]
prices = [1, 1, 4]
print(rod_cutting(length, prices, 6))