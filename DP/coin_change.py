'''
    COIN CHANGE

    Given an integer array of coins[ ] of size N representing different types
    of currency and an integer sum, The task is to find the number of ways to
    make sum by using different combinations from coins[].
'''


def coin_change(coins, i, change):
    '''recusrive function for coin change'''
    if change == 0:
        return 1
    if change < 0:
        return 0
    if i == len(coins):
        return 0
    no_of_ways = coin_change(coins, i + 1, change) + coin_change(coins, i, change - coins[i])
    return no_of_ways

print(coin_change([1, 2, 3], 0, 4))
