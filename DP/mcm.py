'''
    MATRIX CHAIN MULTIPLICATION
'''


def mcm(array, i, j):
    """hello"""
    if i >= j:
        return 0
    _min = 1e9
    for k in range(i, j):
        temp = mcm(array, i, k) + mcm(array, k + 1, j) + array[i - 1] * array[k] * array[j] # cost of the current operation
        _min = min(temp, _min)
    return _min


array = [10, 20, 30]
print(mcm(array, 1, len(array) - 1))
