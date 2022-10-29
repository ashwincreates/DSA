def subset_sum_recur(array, _sum, i, m={}):
    '''recursive approach'''
    if _sum == 0 or i == len(array):
        return _sum == 0
    if _sum in m:
        return m[_sum]
    result = None
    if array[i] <= _sum:
        result = subset_sum_recur(array, _sum - array[i], i + 1, m) or subset_sum_recur(array, _sum, i + 1, m)
    else:
        result = subset_sum_recur(array, _sum, i + 1, m)
    m[_sum] = result
    return m[_sum]

def subsetSumDP(array, _sum):
    '''tabulation approach'''
    n = len(array)
    m = _sum
    dp = [[False for i in range(m + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if array[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - array[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][m]

arr = [2, 3, 7, 8, 10]
sum = 11
print(subsetSumDP(arr, sum))